from django.http import JsonResponse,HttpResponse
from .models import Book, Author, Category


def home(request):
    return HttpResponse("<h1>Welcome to the Library System</h1>")


def book_list(request):
    books = Book.objects.all().values('id', 'title', 'author__name', 'category__name')
    return JsonResponse(list(books), safe=False)

def author_list(request):
    authors = Author.objects.all().values('id', 'name')
    return JsonResponse(list(authors), safe=False)

def category_list(request):
    categories = Category.objects.all().values('id', 'name')
    return JsonResponse(list(categories), safe=False)
