from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField(default='')  # add default
    photo = models.ImageField(upload_to='authors/', default='authors/default_author.jpg')  # add default
    removed = models.BooleanField(default=False)  # добавил в 9 лабе

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default='') # add default
    logo = models.ImageField(upload_to='publishers/', default='publishers/default_publisher.png') # add default
    removed = models.BooleanField(default=False)  # добавил в 9 лабе

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    cover = models.ImageField(upload_to='books/covers/', default='books/covers/default_cover.jpg')
    publication_date = models.DateField(blank=True, null=True)
    removed = models.BooleanField(default=False)  # добавил в 9 лабе

    def __str__(self):
        return self.title