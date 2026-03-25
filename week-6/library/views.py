import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Book, Loan, Member
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def get_all_books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        res = []
        for book in books:
            res.append({"title": book.title, "author": book.author.name, "category": book.category.name})
        return JsonResponse(res, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class LoanView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        id = data.get("id")
        loaned_to = Member.objects.get(name=data.get("loaned_to"))
        loaned_date = data.get("loaned_date")
        due_date = data.get("due_date")
        book = Book.objects.get(title=data.get("book"))
        new_loan = Loan.objects.create(id = id, book = book, loaned_to = loaned_to, loaned_date = loaned_date, due_date = due_date)
        return JsonResponse({
            "message": "Loan recorded",
            "Loan id": new_loan.id 
        })