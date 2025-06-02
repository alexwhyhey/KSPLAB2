from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, ConfirmationForm, AuthorForm, PublisherForm
from .models import Author, Publisher, Book
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Book
from django.contrib import messages


def add_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST, request.FILES)
        confirmation_form = ConfirmationForm(request.POST)
        if book_form.is_valid() and confirmation_form.is_valid():
            book = book_form.save(commit=False)

            if 'author' in book_form.cleaned_data:
                book.author = book_form.cleaned_data['author']
            if 'publisher' in book_form.cleaned_data:
                book.publisher = book_form.cleaned_data['publisher']

            book.save()
            return redirect('book_list')
    else:
        book_form = BookForm()
        confirmation_form = ConfirmationForm()

    context = {
        'book_form': book_form,
        'confirmation_form': confirmation_form
    }
    return render(request, 'books/add_book.html', context)


def add_author(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST, request.FILES)
        if author_form.is_valid():
            author_form.save()
            return redirect('book_list')
    else:
        author_form = AuthorForm()
    return render(request, 'books/add_author.html', {'author_form': author_form})

#10 работа модальное окно
def add_publisher(request):
    if request.method == 'POST':
        publisher_form = PublisherForm(request.POST, request.FILES)
        if publisher_form.is_valid():
            name = publisher_form.cleaned_data['name']
            # Проверяем, существует ли издательство с таким именем
            if Publisher.objects.filter(name=name).exists():
                publisher_form.add_error('name', 'Издательство с таким названием уже существует.')
                return render(request, 'books/add_publisher.html', {'publisher_form': publisher_form, 'show_modal': True, 'error_message': publisher_form.errors['name'][0]})
            else:
                publisher_form.save()
                return redirect('book_list')  # Перенаправляем на список книг
        else:
            return render(request, 'books/add_publisher.html', {'publisher_form': publisher_form})
    else:
        publisher_form = PublisherForm()
    return render(request, 'books/add_publisher.html', {'publisher_form': publisher_form})


def book_list(request):
    books = Book.objects.filter(removed=False)
    authors = Author.objects.filter(removed=False)
    publishers = Publisher.objects.filter(removed=False)
    return render(request, 'books/book_list.html', {'books': books, 'authors': authors, 'publishers': publishers})


def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.removed = True
    book.save()
    messages.success(request, 'Книга удалена.')
    return redirect('book_list')


def author_delete(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    author.removed = True
    author.save()
    messages.success(request, 'Автор удален.')
    return redirect('book_list')


def publisher_delete(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    publisher.removed = True
    publisher.save()
    messages.success(request, 'Издательство удалено.')
    return redirect('book_list')




#добавил в 9 лабе
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book_detail.html', {'book': book})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'books/author_detail.html', {'author': author})


def publisher_detail(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    return render(request, 'books/publisher_detail.html', {'publisher': publisher})

def book_edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book_form = BookForm(request.POST, request.FILES, instance=book)
        if book_form.is_valid():
            # Проверяем, не занято ли название
            title = book_form.cleaned_data['title']
            try:
                existing_book = Book.objects.exclude(pk=book_id).get(title=title) #Исключаем текущую книгу
                book_form.add_error('title', 'Книга с таким названием уже существует.') # Добавляем ошибку в форму
                return render(request, 'books/book_edit.html', {'book_form': book_form, 'book': book}) # Возвращаем форму с ошибкой

            except Book.DoesNotExist:
                book_form.save()
                # return redirect('book_detail', book_id=book.id)
                return render(request, 'books/book_edit.html', {'book_form': book_form, 'book': book, 'success_message': 'Книга успешно сохранена!'})
        else:
            return render(request, 'books/book_edit.html', {'book_form': book_form, 'book': book}) # Возвращаем форму с ошибками
    else:
        book_form = BookForm(instance=book)
    return render(request, 'books/book_edit.html', {'book_form': book_form, 'book': book})


def author_edit(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        author_form = AuthorForm(request.POST, request.FILES, instance=author)
        if author_form.is_valid():
            author_form.save()
            return redirect('author_detail', author_id=author.id)
    else:
        author_form = AuthorForm(instance=author)
    return render(request, 'books/author_edit.html', {'author_form': author_form, 'author': author})


def publisher_edit(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    if request.method == 'POST':
        publisher_form = PublisherForm(request.POST, request.FILES, instance=publisher)
        if publisher_form.is_valid():
            publisher_form.save()
            return redirect('publisher_detail', publisher_id=publisher.id)
    else:
        publisher_form = PublisherForm(instance=publisher)
    return render(request, 'books/publisher_edit.html', {'publisher_form': publisher_form, 'publisher': publisher})


#10-11 лабораторная (проверяет доступность названия книги возвращает JSON-ответ с результатом.)
def check_book_title(request, book_id=None):
    title = request.GET.get('title') # Получаем название из GET-параметра
    if not title:
        return JsonResponse({'available': True, 'message': 'Название не указано'})
    try:
        # Ищем книгу с таким названием
        book = Book.objects.get(title=title)
        if book_id and book.id == int(book_id): # Если редактируем текущую книгу, название доступно
            return JsonResponse({'available': True, 'message': 'Название доступно'})
        else:
            return JsonResponse({'available': False, 'message': 'Название уже занято'})
    except Book.DoesNotExist:
        # Книги с таким названием не существует, название доступно
        return JsonResponse({'available': True, 'message': 'Название доступно'})


def image_page(request):
    return render(request, 'books/image_change.html')
