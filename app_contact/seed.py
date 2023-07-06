from django_seed import Seed
from .models import Contact

def run():
    seeder= Seed.seeder()
    
    
    
    seeder.add_entity(Contact, 1, {
        'location': 'Wonder Street, USA, New York',
        'number': '+01 321 654 214',
        'email': 'hello@xton.com',
    })
    seeder.execute()
    print("contact ok")