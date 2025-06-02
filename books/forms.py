from django import forms
from .models import Author, Publisher, Book

class AuthorForm(forms.ModelForm):
    # noinspection LanguageDetectionInspection
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'biography', 'photo']
        labels = {
            'first_name': 'Имя:',
            'last_name': 'Фамилия:',
            'biography': 'Биография:',
            'photo': 'Фото:'
        }

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address', 'logo']
        labels = {
            'name': 'Название:',
            'address': 'Адрес:',
            'logo': 'Логотип:'
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'cover', 'publication_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # получаем только не удаленных авторов и издателей
        authors = Author.objects.filter(removed=False)
        publishers = Publisher.objects.filter(removed=False)

        if not authors.exists():
            # если нет не удаленных авторов, удаляем поле из формы
            del self.fields['author']
        else:
            # если есть авторы, устанавливаем queryset для поля
            self.fields['author'].queryset = authors

        if not publishers.exists():
            # если нет не удаленных издателей, удаляем поле из формы
            del self.fields['publisher']
        else:
            # если есть издатели, устанавливаем queryset для поля
            self.fields['publisher'].queryset = publishers

class ConfirmationForm(forms.Form):
    confirm_title = forms.CharField(label="Подтвердите название книги:", max_length=200)

    def clean_confirm_title(self):  # валидация
        confirm_title = self.cleaned_data['confirm_title']
        if len(confirm_title) < 3:
            raise forms.ValidationError("Название должно содержать не менее 3 символов")
        return confirm_title