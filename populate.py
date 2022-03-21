import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
import django
django.setup()
from destination.models import Destination

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
    print('Starting Destination population script...')
    populate()

