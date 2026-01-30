# import uuid
from django.db import models

# Create your models here.
class Author(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isbn = models.CharField(max_length=40)
    title = models.CharField(max_length=50, primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ManyToManyField(Category, related_name='books')
    available_copies = models.IntegerField()
    published_date = models.DateField()

    def __str__(self):
        return self.title

class Member(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, primary_key=True)

    def __str__(self):
        return self.name
    
class Loan(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loans")
    loaned_to = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="loans")
    loaned_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return f"{self.book} -- {self.loaned_to}"


