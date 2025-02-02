class Library:
    def __init__(self):
        self.book_name=input("enter the name of the book : ")
        self.Author=input("enter the name of the author : ")
        self.isbn=input("enter the isbn of the book : ")
    
    def display_book_details(self):
        print(f"name of the book : {self.book_name}""\n"f"Author of the book : {self.Author}""\n"f"ISBN of the book : {self.isbn}")
def main():
    library=Library()
    library.display_book_details()
    
main()