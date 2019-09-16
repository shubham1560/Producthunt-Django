from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    # def __str__(self):
    #     return self.title, self.url


class ProductAttribute(models.Model):
    vote = models.BooleanField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    voting_time = models.DateTimeField()


class ProductFeedback(models.Model):
    comment = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    commentedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    createdOn = models.DateTimeField()
    useful = models.BooleanField(default=True)
