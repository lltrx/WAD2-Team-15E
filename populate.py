import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Destination

def populate():
    destinations = {
        'Glasgow Necropolis': {'description': """The Glasgow Necropolis is a Victorian cementary in Glasgow, Scotland.
                                          It is on a low, but very prominent hill to the east of Glasgow Central."""},
        'Edinburght City Centre': {'description': """Edinburgh's busy city centre is ranked amongst the most attractive in the world.

                                                Exploring the medieval Old Town, you will discover the secrets of Edinburgh's past 
                                                and can visit some of the city's top attractions, including Edinburgh Castle.
                                                Venture on to bustling Princes Street and New Town to shop until you drop,
                                                 taking in the architectural grandeur of the Capital and its landmarks."""}
    }

    for dest, dest_info in destinations.items():
        add_destination(dest, dest_info['description'])
        print(dest)



def add_destination(name, description):
    d = Destination.objects.get_or_create(name=name)[0]
    d.description = description
    d.save()

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()

'''
def populate():
    python_pages = [
        # We can add some example of places here 
        # Also views and comment
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/',
         'views':10},

        {'title': 'How to Think like a Computer Scientist',
          'url': 'http://www.greenteapress.com/thinkpython/','views':25},

         {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/','views':30}]

    django_pages = [
        {'title': 'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/','views':24},

         {'title': 'Django Rocks',
        'url': 'http://www.djangorocks.com/','views':68},

         {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/','views':78}]

    other_pages = [
        {'title': 'Bottle',
        'url':'http://bottlepy.org/docs/dev/',
         'views':276},

        {'title': 'Flask',
        'url': 'http://flask.pocoo.org',
         'views':425}]


    cats = {'Python': {'pages': python_pages,'views':128,'likes':64},'Django': {'pages': django_pages,'views':64,'likes':32},'Other Frameworks': {'pages': other_pages,'views':32,'likes':16}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])




    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')




def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name,views,likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c
'''