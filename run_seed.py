import django
django.setup()

from app_contact.seed import run

if __name__ == '__main__':
    run()