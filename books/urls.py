from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list, name='book_list'),  # пустой путь тк мы уже в /books/
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('<int:book_id>/edit/', views.book_edit, name='book_edit'),
    path('<int:book_id>/delete/', views.book_delete, name='book_delete'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('authors/<int:author_id>/edit/', views.author_edit, name='author_edit'),
    path('authors/<int:author_id>/delete/', views.author_delete, name='author_delete'),
    path('publishers/<int:publisher_id>/', views.publisher_detail, name='publisher_detail'),
    path('publishers/<int:publisher_id>/edit/', views.publisher_edit, name='publisher_edit'),
    path('publishers/<int:publisher_id>/delete/', views.publisher_delete, name='publisher_delete'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_publisher/', views.add_publisher, name='add_publisher'),
    path('check_book_title/<int:book_id>/', views.check_book_title, name='check_book_title'), #  URL для проверки (с book_id)
    path('check_book_title/', views.check_book_title, name='check_book_title_new'), # URL для проверки при добавлении новой книги
]