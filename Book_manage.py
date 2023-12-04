import json
import uuid
import os
class Book:
    
    def __init__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        filename='data_files/book_management.json'
        self.file_path = os.path.join(current_directory, filename)

    def generate_book_id(self):
        return str(uuid.uuid4())
    
    def get_Book(self):
      try:  
        with open(self.file_path, 'r') as file:
                return json.load(file)
      except Exception as e:
          print(e)          

    def save_book_data(self,data):
      try:  
        with open(self.file_path, 'w') as file:
               json.dump(data, file,indent=2)
                
      except Exception as e:
          print(e) 

    def check_id(self,id):
        try:
            self.existing_data=self.get_Book()
            book_data=[book for book in self.existing_data if book['id']==id]
            if book_data:
                return False
            else:
                return True
        except Exception as e:
            print(e)    



    def add_book(self):
        try:
           book_name=input('enter the name of book:')
           book_price=float(input("enter the price of book:"))
           quantity=int(input("enter the quantity of book :"))
           author=input("enter the name of author:") 
           data={
               'id':self.generate_book_id(),
               'name':book_name,
               'price':book_price,
               'quantity':quantity,
               'author':author
               }
           if self.check_id(data['id']):
               self.existing_data=self.get_Book()
               self.existing_data.append(data)    
               self.save_book_data(self.existing_data)
               print('data added successfully')
           else:
               print("Book already present")    
        except Exception as e:
           print(e)

    def display_book(self):
        try:
            self.existing_data=self.get_Book()
            for book in self.existing_data:
                print("id of book:",book['id'])
                print("Name of book:",book['name'])  
                print("Price of book:",book['price'])
                print("Quantity of book:",book['quantity'])
                print("quantity of book:",book['author']) 
                print('--------------------------------------------------')
        except Exception as e:
           print(e)        



