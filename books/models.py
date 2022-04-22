from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    country = models.CharField(max_length=100)


    def __str__(self):
        return self.name



class Book(models.Model):
    name = models.CharField(max_length=300)
    isbn = models.CharField(max_length=50)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    stock = models.IntegerField(default=1)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name+" "+self.author.name