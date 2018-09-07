from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from django.contrib.auth.models import User
#from profiles.models import BaseProfile



LANGUAGE_CHOICES = (
("BANGLA", "Bangla"),
("ENGLISH", "English"),
("ARABIC","Arabic"),
("URDU", "Urdu"),
)
CATEGORY_CHOICES = (
("Spirituality", "Spirituality"),
("Tafseer", "Tafseer"),
("Hadith","Hadith"),
("Aqeedah", "Aqeedah"),
)

# Create your models here.
class BookOwner(models.Model):
    name = models.CharField(max_length=32)
    mobile = models.IntegerField()
    address= models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)


class  	Author(models.Model):
    name = models.CharField(max_length=32)
    about = models.TextField()

    def __str__(self):
        return str(self.name)

class Book(models.Model):
    title = models.CharField(max_length=32)
    language = models.CharField(max_length=32,choices=LANGUAGE_CHOICES,default="BANGLA")
    category = models.CharField(max_length=32,choices=CATEGORY_CHOICES,default="Spirituality")
    details = models.TextField()
    mark = models.BooleanField(default=False)
    author = models.ForeignKey('Author',on_delete=models.CASCADE,default=None)
    owner = models.ForeignKey('BookOwner',on_delete=models.CASCADE,default=None)
    image = models.ImageField(null=True,blank=True,default=None)


    def __str__(self):
        return str(self.title)


class BookTransactionModel(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,blank=False, null=False)
    lend_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True)
    lend_from = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    message = models.TextField(blank=True)



class QuotationFromBook(models.Model):
    """
    Class descirbes specific quotation from the book
    saved by specific user
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE ,blank=False, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,blank=False, null=False)
    quotation = models.CharField(max_length=600, null=False, blank=False)
    creation_date = models.DateField(blank=False, null=False)
