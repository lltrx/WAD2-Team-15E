from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http.response import HttpResponseNotModified
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from datetime import datetime
from destination.forms import DestinationForm, RegistrationForm, EditProfileForm, UserProfileForm, UserProfileChangeForm, CommentForm
from destination.models import Destination, UserProfile, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm



def index(request):
    context_dict = {}
    most_liked = sorted(Destination.objects.all(), key=lambda x: - x.total_likes())[:3]
    context_dict['most_liked'] = most_liked
    best_rated = sorted(Destination.objects.all(), key=lambda x: - x.total_rating())[:3]
    context_dict['best_rated'] = best_rated
    return render(request, 'destination/index.html', context=context_dict)
 

def help(request):
    '''
    print(request.method)
    print(request.user)
    visitor_cookie_handler(request)
    '''
    context_dict = {}

    
    return render(request, 'destination/help.html', context_dict)

def destination_menu(request):
    
    context_dict = {}
    all_destinations = Destination.objects.all()
    context_dict['destinations'] = all_destinations
    return render(request, 'destination/destination_menu.html', context_dict)

@login_required
def my_profile(request):
    context_dict = {}
    context_dict['user_destinations'] = Destination.objects.filter(author=request.user)
    context_dict['user_profile'] = UserProfile.objects.get_or_create(user=request.user)[0]
    return render(request, 'destination/profile.html', context_dict)

@login_required
def edit_profile(request):
    edited = False
    userprofile = UserProfile.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user.save()
            profile = user_profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            edited = True
            return redirect(reverse('destination:my_profile'))
        else:
            print(user_form.errors, user_profile_form.errors)
                    
    else:
        user_form = EditProfileForm(instance=request.user)
        user_profile_form = UserProfileChangeForm(instance=request.user.userprofile)
    return render(request, 'destination/edit_profile.html', {'user_form': user_form, 'user_profile_form': user_profile_form, 'edited': edited})

def user_profile(request, username):
    context_dict = {}
    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get_or_create(user=user)[0]
    user_destinations = Destination.objects.filter(author=user)
    context_dict['target_user'] = user
    context_dict['user_profile'] = user_profile
    context_dict['user_destinations'] = user_destinations
    return render(request, 'destination/user_profile.html', context_dict)

def register(request):
    registered = False
    context_dict = {}
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        user_profile_form = UserProfileForm(request.POST, request.FILES )
        
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user = user_form.save()
            profile = user_profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()
            registered = True
            
            return redirect(reverse('destination:login'))
        
            
        else:
            print(user_form.errors, user_profile_form.errors)
            context_dict['user_error'] = user_form.errors
            context_dict['user_profile_error'] = user_profile_form.errors
    else:
        user_form = RegistrationForm()
        user_profile_form = UserProfileForm()

    context_dict['user_form'] = user_form
    context_dict['user_profile_form'] = user_profile_form
    context_dict['registered'] = registered
    return render(request, 'destination/register.html', context_dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('destination:index'))
            else:
                return HttpResponse("Your destination account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'destination/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('destination:index'))

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('destination:my_profile'))
    else:
        form = PasswordChangeForm(user=request.user)
        context_dict = {'form': form}
        return render(request, 'destination/change_password.html', context=context_dict)
        

def show_destination(request, destination_name_slug):
    context_dict = {}
    try:
        destination = Destination.objects.get(slug=destination_name_slug)
        context_dict['destination'] = destination
        
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.destination = destination
                comment.user = request.user
                comment.save()
        
        form = CommentForm()
        
        total_likes = destination.total_likes()
        context_dict['total_likes'] = total_likes
        
        total_rating = destination.total_rating()
        if total_rating == 0:
            total_rating = "No ratings yet"
        context_dict['total_rating'] = total_rating
        
        liked = False
        if request.user.is_authenticated:
            if request.user in destination.likes.all():
                liked = True
        
                 
        context_dict['liked'] = liked
        
        context_dict['form'] = form 
            
    except Destination.DoesNotExist:
        context_dict['destination'] = None
        return render(request, 'destination/destination.html', context=context_dict)
    finally:
        return render(request, 'destination/destination.html', context=context_dict)


@login_required
def add_destination(request):
    context_dict = {}
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(request, commit=True)
            return redirect(reverse('destination:show_destination', kwargs={'destination_name_slug':new.slug}))
        else:
            print(form.errors)
            context_dict['error'] = form.error
    else:
        form = DestinationForm()
    context_dict['form'] = form
    return render(request, 'destination/add_destination.html', context_dict)

@login_required
def edit_destination(request, destination_name_slug):
    context_dict = {}

    destination = Destination.objects.get(slug=destination_name_slug)
    context_dict['instance'] = destination
    print(destination.destination_type)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination, initial={'destination_type': destination.destination_type })
        
        if form.is_valid():
            new = form.save(request)
            return redirect(reverse('destination:show_destination', kwargs={'destination_name_slug':new.slug}))
        
    else:
        form = DestinationForm(request.FILES, instance=destination, initial={'destination_type': destination.destination_type })
        context_dict['form'] = form
        return render(request, 'destination/edit_destination.html', context=context_dict)

@login_required
def like_destination(request, destination_name_slug):
    destination = Destination.objects.get(slug=destination_name_slug)
    liked = False
    if request.user in destination.likes.all():
        destination.likes.remove(request.user)
        liked = False
    else:
        destination.likes.add(request.user)
        liked = True
    return redirect(reverse('destination:show_destination', kwargs={'destination_name_slug':destination_name_slug}))

@login_required
def delete_destination(request, destination_name_slug):
    destination = Destination.objects.get(slug=destination_name_slug)
    destination.delete()
    return redirect(reverse('destination:destination_menu'))

@login_required
def comment_destination(request, destination_name_slug):
    destination = Destination.objects.get(slug=destination_name_slug)
    print(destination)
    return redirect(reverse('destination:show_destination', kwargs={'destination_name_slug':destination_name_slug}))

@login_required
def delete_comment(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    destination = comment.destination
    destination_name_slug = destination.slug
    comment.delete()
    return redirect(reverse('destination:show_destination', kwargs={'destination_name_slug':destination_name_slug}))

'''
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,'last_visit',str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
        
    request.session['visits'] = visits
'''