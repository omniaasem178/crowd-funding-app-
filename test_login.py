#!/usr/bin/env python
"""
Test script to help troubleshoot login issues
"""
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def test_user_creation():
    """Test creating a user and authenticating"""
    print("Testing user creation and authentication...")
    
    # Check if test user exists
    username = 'testuser'
    password = 'TestPass123!'
    email = 'test@example.com'
    
    # Delete existing test user if it exists
    try:
        existing_user = User.objects.get(username=username)
        existing_user.delete()
        print(f"Deleted existing user: {username}")
    except User.DoesNotExist:
        pass
    
    # Create new test user
    try:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        print(f"Created user: {username}")
        print(f"User ID: {user.id}")
        print(f"User is active: {user.is_active}")
        print(f"User is staff: {user.is_staff}")
        print(f"User is superuser: {user.is_superuser}")
        
        # Test authentication
        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user:
            print("✅ Authentication successful!")
            print(f"Authenticated user: {authenticated_user.username}")
        else:
            print("❌ Authentication failed!")
            
    except Exception as e:
        print(f"❌ Error creating user: {e}")

def list_users():
    """List all users in the database"""
    print("\nListing all users in database:")
    users = User.objects.all()
    if users:
        for user in users:
            print(f"- {user.username} (ID: {user.id}, Active: {user.is_active})")
    else:
        print("No users found in database")

if __name__ == '__main__':
    print("=== Django Login Test Script ===\n")
    
    # List existing users
    list_users()
    
    # Test user creation
    test_user_creation()
    
    # List users again
    list_users()
    
    print("\n=== Test Complete ===")