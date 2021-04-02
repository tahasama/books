import uuid
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    class Meta:
        permissions = [
            ('special_status', 'Can read all books'),
            ('go_list', 'Can see the list of books'),     
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])
    
class Review(models.Model):

    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reviews',)
    review = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    def __str__(self):
        return self.review
    