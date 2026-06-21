from django.db import models
from django.contrib.auth import get_user_model
from author.models import Author

User = get_user_model()

class Book(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    count = models.PositiveIntegerField(default=10)
    authors = models.ManyToManyField(Author, related_name='books')
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='borrowed_books')

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Count: {self.count}"

    def __repr__(self):
        return f"Book(id={self.id})"

    @staticmethod
    def get_by_id(book_id):
        try:
            return Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return None

    @staticmethod
    def delete_by_id(book_id):
        count, _ = Book.objects.filter(pk=book_id).delete()
        return count > 0

    @classmethod
    def create(cls, name, description, count=10, authors=None):
        book = cls.objects.create(name=name, description=description, count=count)
        if authors:
            book.authors.set(authors)
        return book

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'count': self.count,
            'authors': [author.name for author in self.authors.all()]
        }

    def update(self, name=None, description=None, count=None):
        if name: self.name = name
        if description: self.description = description
        if count is not None: self.count = count
        self.save()

    def add_authors(self, authors):
        self.authors.add(*authors)

    def remove_authors(self, authors):
        self.authors.remove(*authors)

    @staticmethod
    def get_all():
        return Book.objects.all()