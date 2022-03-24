from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.http.response import HttpResponseNotModified
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from datetime import datetime
from destination.forms import DestinationForm, RegistrationForm, EditProfileForm
from destination.models import Destination, UserProfile
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm



def index(request):
    context_dict = {}
    return render(request, 'destination/index.html', context=context_dict)
 

def help(request):
    '''
    print(request.method)
    print(request.user)
    visitor_cookie_handler(request)
    '''
    context_dict = {}

    
    return render(request, 'destination/help.html', context_dict)


def destination(request):
    
    context_dict = {}
    return render(request, 'destination/destination.html', context_dict)

def destination_menu(request):
    
    context_dict = {}
    all_destinations = Destination.objects.all()
    context_dict['destinations'] = all_destinations
    return render(request, 'destination/destination_menu.html', context_dict)

def profile(request):
    return render(request, 'destination/profile.html', {})

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect(reverse('destination:profile'))
        
    else:
        form = EditProfileForm(instance=request.user)
        context_dict = {'form': form}
        return render(request, 'destination/edit_profile.html', context=context_dict)
    
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('destination:profile'))
    else:
        form = PasswordChangeForm(user=request.user)
        context_dict = {'form': form}
        return render(request, 'destination/change_password.html', context=context_dict)
        
def show_destination(request, destination_name_slug):
    context_dict = {}
    try:
        destination = Destination.objects.get(slug=destination_name_slug)
        context_dict['destination'] = destination
    except Destination.DoesNotExist:
        context_dict['destination'] = None
        return render(request, 'destination/destination.html', context=context_dict)
    finally:
        return render(request, 'destination/destination.html', context=context_dict)
'''
    if request.session.test_cookie_worked():
        print("TEST COOKIE WORKED!")
        request.session.delete_test_cookie()
'''


@login_required
def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('destination:index'))
        else:
            print(form.errors)
    else:
        form = DestinationForm()
    return render(request, 'destination/add_destination.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('destination:login'))
    else:
        form = RegistrationForm()
        
        context_dict = {'form': form}
        return render(request, 'destination/register.html', context=context_dict)


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


'''
@login_required
def restricted(request):
    return render(request, 'destination/restricted.html')

'''
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('destination:index'))

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