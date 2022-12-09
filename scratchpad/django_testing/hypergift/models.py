from django.db import models

TITLE_CHOICES = [
   ('MR', 'Mr.'),
   ('MRS', 'Mrs.'),
   ('MS', 'Ms.'),
]


class PostcardModel(models.Model):
    address = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    compliment = models.CharField(max_length=1024)
    usage = models.CharField(max_length=3, choices=TITLE_CHOICES)
    delivery_date = models.DateField(blank=True, null=True)
    email = models.EmailField()
