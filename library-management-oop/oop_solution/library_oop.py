class Book:
    def __init__(self, id, title, author, total_copies):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies


class Member:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books_list = []


class Library:
    def __init__(self):
        self.books_collection = []
        self.members = []
        self.borrowed_books = []
    

    def add_books(self, book_id, title, author, available_copies):
        book = Book(book_id, title, author, available_copies,)
        self.books_collection.append(book)
        print(f"Book '{book.title}' added succesfully!")

    def add_member(self, memeber_id, name, email):
        member = Member(memeber_id, name, email)
        self.members.append(member)
        print(f"Member '{member.name}' registered successfully!")


    def find_book(self, book_id):
        for book in self.books_collection:
            if book.id == book_id:
                return book
            
        return None
    

    def find_member(self, member_id):
        for member in self. members:
            if member.id == member_id:
                return member
        return None
            

    def borrow_books(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print("Error: Member not found!")
            return False
        
        if not book:
            print("Error: Book not found!")
            return False
        
        if book.available_copies <= 0:
            print("Error: No copies available!")
            return False
        
        if len(member.borrowed_books_list) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False
        
        book.available_copies -= 1
        member.borrowed_books_list.append(book_id)

        transaction = {
        'member_id': member_id,
        'book_id': book_id,
        'member_name': member.name,
        'book_title': book.title
    }
        self.borrowed_books.append(transaction)
    
        print(f"{member.name} borrowed '{book.title}'")
        return True 


    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member or not book:
            print("Error: Member or book not found!")
            return False
        
        if book_id not in member.borrowed_books_list:
            print("Error: This member hasn't borrowed this book!")
            return False
        
        book.available_copies += 1
        member.borrowed_books_list.remove(book_id)
        
        # Remove from borrowed_books list
        for i, transaction in enumerate(self.borrowed_books):
            if transaction['member_id'] == member.id and transaction['book_id'] == book.id:
                self.borrowed_books.pop(i)
                break
        
        print(f"{member.name} returned '{book.title}'")
        return True


    def display_available_books(self):
        print("\n=== Available Books ===")
        for book in self.books:
            if book.available_copies > 0:
                print(f"{book.title} by {book['author']} - {book.available_copies} copies available")


    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        
        print(f"\n=== Books borrowed by {member['name']} ===")
        if not member.borrowed_books_list:
            print("No books currently borrowed")
        else:
            for book_id in member.borrowed_books_list:
                book = self.find_book(book_id)
                if book:
                    print(f"- {book.title} by {book.author}")