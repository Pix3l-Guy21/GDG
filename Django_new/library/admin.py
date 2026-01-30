from django.contrib import admin
from .models import Book, Category, Author, Member, Loan
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "available_copies")

    list_filter = ("author", "category")

    search_fields = ("title", "isbn")

admin.site.register(Member)
admin.site.register(Loan)
admin.site.register(Category)
admin.site.register(Author)