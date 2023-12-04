from add_new_user import LibraryManagementSystem
from Book_manage import Book
from datetime import datetime
import json
import uuid
import os
class Book_rent:
    def __init__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        filename='data_files/book_rent.json'
        self.file_path = os.path.join(current_directory, filename)
        self.User=LibraryManagementSystem()
        self.book=Book()
        self.rent_data=[]

    def generate_bookrent_id(self):
        return str(uuid.uuid4())  
    
    def get_Bookrent_data(self):
      try:  
        with open(self.file_path, 'r') as file:
                self.rent_data=json.load(file)
      except Exception as e:
          print(e) 

    def save_bookrent_data(self,data):
      try:  
        with open(self.file_path, 'w') as file:
               json.dump(data, file,indent=2)
               
      except Exception as e:
          print(e)       
      

    def Book_borrows(self):
      try:   
        user_id=input("enter the id of Student")
        book_id=input("enter the id of book:")
        self.users=self.User.load_users()
        self.books= self.book.get_Book()
        user=[User for User in self.users if user_id == User['member_id']]
        book=[book_detail for book_detail in self.books if book_id == book_detail['id']]
        g=False
        if user and book:
            if user[0]['book_taken']>=0 and user[0]['book_taken']<3:
             if book[0]['quantity'] > 0:
               today = datetime.today()
               formatted_date = today.strftime('%Y-%m-%d')
               data={
                 'id':self.generate_bookrent_id(),
                 'user_id':user[0]['member_id'],
                 'book_id':book[0]['id'],
                 'Username':user[0]['full_name'],
                 'bookname':book[0]['name'],
                 'Date':formatted_date,
                 }
               self.get_Bookrent_data()
               self.rent_data.append(data)
               self.save_bookrent_data(self.rent_data)
               print("book given succuessfully")
               g=True
             else:
                print("Stuck completed") 
            else:
               print("you cannot take for than 3 book:")     
        else:
            print("User or book id not matched") 

        t=False 
        s=False          
        if g==True:
          for book in self.books:
              if book_id == book['id']:
                  book['quantity']-=1
                  t=True
          for user1 in self.users:
             if user1['member_id']==user_id:
                user1['book_taken']+=1
                s=True

                    
        if t==True:
            self.book.save_book_data(self.books) 
        if s==True:
           self.User.save_users(self.users)     

      except Exception as e:
        print(e)

    def book_return(self):
      try:  
        user_id=input("enter the id of Student")
        book_id=input("enter the id of book:")
        today = datetime.today()
        formatted_date = today.strftime('%Y-%m-%d')
        date1 = datetime.strptime(formatted_date, '%Y-%m-%d')
        self.get_Bookrent_data()
        g=False
        for data in self.rent_data:
            if data['user_id'] ==user_id and data['book_id']==book_id:
                dat2=data['Date']
                date2 = datetime.strptime(dat2, '%Y-%m-%d')
                date_difference = (date2 - date1).days
                if date_difference>15:
                    print("please pay the fine you cross limit time:")
                    choice=input("enter the [Y] key to denote the paid fine:")
                    if choice.lower() == 'y':
                        self.rent_data.remove(data)
                        self.save_bookrent_data(self.rent_data)
                        print("Return book success")
                        g=True
                else:        
                    self.rent_data.remove(data)
                    self.save_bookrent_data(self.rent_data)
                    print("Return book success")
                    g=True

            t=True
            s=False
            if g==True:
              self.books= self.book.get_Book()
              self.users=self.User.load_users()
              for book in self.books: 
                  if book['id'] ==book_id:
                    if book['quantity']>0:
                       book['quantity']+=1 
                       t=True 
              for user1 in self.users:
                if user1['member_id']==user_id:
                  user1['book_taken']-=1
                  s=True        

            if t==True:
              self.book.save_book_data(self.books)
            if s==True:
               self.User.save_users(self.users)  
      except Exception as e:
        print(e)      








       


              

           




