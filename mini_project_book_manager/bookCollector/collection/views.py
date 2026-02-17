from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from .models import Book, Author
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class BookView(View):
    def get(self, request, book_id=None):
        if book_id:
            book = get_object_or_404(Book, id=book_id)
            return JsonResponse({"title": book.title, "author": book.author.name, "pulished data": book.published_date.isoformat(), "isbn": book.isbn})
        books = Book.objects.all()
        return JsonResponse([{"title": book.title, "author": book.author.name} for book in books], safe=False)
    
    def put(self, request, book_id=None):
        book = get_object_or_404(Book, id=book_id)
        data = json.loads(request.body)
        book.title = data.get('title', book.title)
        book.published_date = data.get('published_date', book.published_date.isoformat())
        book.isbn = data.get('isbn', book.isbn)
        return JsonResponse({"message": "Book updated"})
    
    def post(self, request):
        data = json.loads(request.body)
        try:
            author_obj = Author.objects.get(id=data['author'])
            book = Book.objects.create(
                title=data['title'], 
                author=author_obj, 
                published_date=data['published_date'], 
                isbn=data['isbn']
            )
        except Author.DoesNotExist:
            return JsonResponse({"error": "Author not found"}, status=404)
        except KeyError as e:
            return JsonResponse({"error": f"Missing field: {str(e)}"}, status=400)
        
        return JsonResponse({"message": "Book created", "id": book.id}, status=201)
    
    def delete(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return JsonResponse({"message": "Book deleted"}, status=204)

@method_decorator(csrf_exempt, name='dispatch')
class AuthorView(View):
    def get(self, request, author_id=None):
        if author_id:
            author = get_object_or_404(Author, id=author_id)
            return JsonResponse({"name": author.name, "bio": author.bio})
        authors = Author.objects.all()
        return JsonResponse([{"id": a.id, "name": a.name} for a in authors], safe=False)
    
    def post(self, request):
        data = json.loads(request.body)
        author = Author.objects.create(name = data['name'], bio = data['bio'])
        return JsonResponse({"message": "author created", "id": author.id}, status=201)
    
    def put(self, request, author_id=None):
        author = get_object_or_404(Author, id=author_id)
        data = json.loads(request.body)
        author.name = data.get('name', author.name)
        author.bio = data.get('bio', author.bio)
        return JsonResponse({"message": "Author updated"})
    
    def delete(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)
        author.delete()
        return JsonResponse({"message": "Author removed"}, status=204)