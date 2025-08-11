from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class Command(BaseCommand):
    help = 'Create a test user for login testing'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='testuser',
            help='Username for the test user'
        )
        parser.add_argument(
            '--password',
            type=str,
            default='TestPass123!',
            help='Password for the test user'
        )
        parser.add_argument(
            '--email',
            type=str,
            default='test@example.com',
            help='Email for the test user'
        )

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        email = options['email']

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'User "{username}" already exists. Deleting...')
            )
            User.objects.filter(username=username).delete()

        # Create new user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created user "{username}"')
            )
            self.stdout.write(f'User ID: {user.id}')
            self.stdout.write(f'Email: {user.email}')
            self.stdout.write(f'Is active: {user.is_active}')

            # Test authentication
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user:
                self.stdout.write(
                    self.style.SUCCESS('✅ Authentication test successful!')
                )
            else:
                self.stdout.write(
                    self.style.ERROR('❌ Authentication test failed!')
                )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating user: {e}')
            )