class Book:
    def __init__(self, title, author):
        self.title = title  # Título del libro
        self.author = author  # Autor del libro
        self.available = True  # Disponibilidad del libro
    
    def borrow(self):
        if self.available:
            self.available = False  # Marcar el libro como prestado
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no esta disponible")
    
    def return_book(self):
        self.available = True  # Marcar el libro como devuelto
        print(f"El libro {self.title} ha sido devuelto")

class User:
    def __init__(self, name, user_id):
        self.name = name  # Nombre del usuario
        self.user_id = user_id  # ID del usuario
        self.borrowed_books = []  # Lista de libros prestados

    def borrow_book(self, book):
        if book.available:
            book.borrow()  # Prestar el libro
            self.borrowed_books.append(book)  # Añadir el libro a la lista de prestados
        else:
            print(f"El libro {book.title} No esta disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()  # Devolver el libro
            self.borrowed_books.remove(book)  # Remover el libro de la lista de prestados
        else:
            print(f"El libro {book.title} No esta en la lista de prestados")

class library:
    def __init__(self):
        self.books = []  # Lista de libros en la biblioteca
        self.users = []  # Lista de usuarios registrados

    def add_book(self, book):
        self.books.append(book)  # Añadir libro a la biblioteca
        print(f"El libro {book.title} ha sido agregado")

    def register_user(self, user):
        self.users.append(user)  # Registrar usuario en la biblioteca
        print(f"El usuario {user.name} ha sido registrado")

    def show_available_books(self):
        print(f"libros disponibles")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.author}")  # Mostrar libros disponibles

# Crear libros
book1 = Book("El principito", "Antonie de Saint-Exupéry") 
book2 = Book("libro 2", "Alguien")

# Crear usuarios
user1 = User("Joaquin", "001")
user2 = User("Camila", "002")

# Crear biblioteca
library = library()
library.add_book(book1)       
library.add_book(book2)
library.register_user(user1)     

# Mostrar libros disponibles
library.show_available_books()

# Realizar préstamo
user1.borrow_book(book1)
library.show_available_books()
