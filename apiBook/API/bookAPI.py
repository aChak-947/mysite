from .. models import Book
from rest_framework.response import Response

def upsertBook(self, request):

    try:
        book = Book.objects.get(id = request["id"])
        book.name = request["name"]
        book.author = request["author"]
        book.genre = request["genre"]
        book.save()

        book_details = {"id": book.id, 
        "name": book.name, 
        "author": book.author, 
        "genre": book.genre}

        return Response({'Message':'Book Updated', 'Book':book_details})

    except:
        Book.objects.create(
            id = request["id"],
            name = request["name"],
            author = request["author"],
            genre = request["genre"],
        )

        book = Book.objects.all().filter(id=request["id"]).values()
        return Response({'Message':'New Book added', 'Book': book})



def deleteBook(self, request): 

    book = Book.objects.get(id=request['id'])
    book.delete()
    
    return Response({'Message':'Book Removed'})



def listBooks(self, request): 

    if "id" in request:
        book = Book.objects.get(id=request["id"])
        
        book_details = {"id": book.id, 
        "name":book.name, 
        "author":book.author, 
        "genre":book.genre}

        return Response({'Message':'Book', 'Book':book_details})

    else:
        allBooks = Book.objects.all().values()
        return Response({'Message':'List of Books', 'Book List':allBooks})