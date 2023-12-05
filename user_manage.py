import json
import uuid
from datetime import datetime
import os
class LibraryManagementSystem:
    def __init__(self):
        self.users = []
        current_directory = os.path.dirname(os.path.abspath(__file__))
        filename='data_files/add_new_users_config.json'
        self.users_file_path = os.path.join(current_directory, filename)
        

    def load_users(self):
        try:
            with open(self.users_file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # Initialize with an empty list if the file doesn't exist
            self.users = []

    def save_users(self,data):
        with open(self.users_file_path, 'w') as file:
            json.dump(data, file, indent=2)

    def generate_user_id(self):
        return str(uuid.uuid4())

    def add_user(self):
        print("=== Add New User ===")
        full_name = input("Enter full name: ")
        contact_number = input("Enter contact number: ")

        # Generate a unique user ID outside the if statement
        member_id = self.generate_user_id()

        self.users=self.load_users()

        # Check for duplicate member ID or contact number
        if any(user['contact_number'] == contact_number or user['member_id'] == member_id for user in self.users):
            print("Error: User with the same member ID or contact number already exists.")
            return

        # Create a new user dictionary
        new_user = {
            'member_id': member_id,
            'full_name': full_name,
            'contact_number': contact_number,
            'book_taken':0,
            'join_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Add the new user to the list
        self.users.append(new_user)

        print("User added successfully!")
        print(f"Member ID: {member_id}")
        self.save_users(self.users)

    def display_users(self):
        print("=== User List ===")

        self.users=self.load_users()

        for user in self.users:
            print(f"Member ID: {user['member_id']}, Full Name: {user['full_name']}, Contact Number: {user['contact_number']}")
            print(f"Join Date: {user['join_date']}")
            print("-" * 30)

