from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book-list'),
    path('<int:pk>/', views.book_detail, name='book-detail'),
    path('create/', views.create_book, name='create-book'),
    path('user/<int:user_id>/books/', views.user_books, name='user-books'),
]
