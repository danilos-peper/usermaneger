import django_setup

from user_control.models import Role, User
from django.core.exceptions import ObjectDoesNotExist

#admin_role = Role.objects.create(name = "admin")
#user_role = Role.objects.create(name = "user")

def create_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    role_name = input("Enter your role (admin or user): ")
    try:
        role = Role.objects.get(name = role_name)
        user = User.objects.create(name = name, email = email, role = role)
        print(f"User {user.name} created succesfully!")
    except ObjectDoesNotExist:
        print(f"Role does not exists")
    except Exception as e:
        print(f"Error: {e}")

def list_users():
    users = User.objects.all()
    #print(users)
    if users:
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}, Role: {user.role.name}")
    else:
        print("No users found!")

def update_user():
    email = input("enter user email to update: ")
    try:
        user = User.objects.get(email = email)
        new_name = input("enter your new name (leave blank to keep current):")
        if new_name:
            user.name = new_name
        user.save()
        print("User updated succesfully!")
    except ObjectDoesNotExist:
        print(f"User does not exists")
    except Exception as e:
        print(f"Error: {e}")

def delete_user():
    email = input("enter user email to delete: ")
    try:
        user = User.objects.get(email = email)
        user.delete()
        print("User deleted succesfully!")
    except ObjectDoesNotExist:
        print(f"User does not exists")
    except Exception as e:
        print(f"Error: {e}")

def list_admin_users():
    admins = User.objects.filter(role__name = "admin")
    if admins:
        for user in admins:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}, Role: {user.role.name}")
    else:
        print("No admins found!")

while 1:
    print("\nOptions:")
    print("1. Create user")
    print("2. List all users")
    print("3. Update user")
    print("4. Delate user")
    print("5. List admin users")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 6:
        break
    elif choice == 1:
        create_user()
    elif choice == 2:
        list_users()
    elif choice == 3:
        update_user()
    elif choice == 4:
        delete_user()
    elif choice == 5:
        list_admin_users()
    else:
        print("Invalid choice. Try again!")










