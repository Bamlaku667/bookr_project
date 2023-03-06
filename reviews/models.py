from django.db import models
from django.contrib import auth

# Create your models here.
class Publisher(models.Model):
    """A company that publishes books"""
    name = models.CharField(\
        max_length=50, \
            help_text="The name of the publisher")
    
    website = models.URLField(help_text = "the company's website")
    email = models.EmailField(\
        help_text="The publisher's email address.")


class Contributor(models.Model):
    """A contributor of the book eg, author, co-author, editor"""
    first_names = models.CharField(\
        max_length= 50, \
            help_text="The contributor's first name")
    
    last_names = models.CharField(\
        max_length=50, 
        help_text=" the contributors last name.")
    
    email = models.EmailField(\
        help_text="The contact email of the contributor.")

class Book(models.Model):
    """A publishe book """
    title = models.TextField(\
        max_length=70,\
            help_text= "The title of the book.")
    
    publication_date = models.DateField(\
        verbose_name=\
            "Date of the book was published")
    
    isbn = models.CharField(\
        max_length=20, \
            verbose_name="ISBN number of the book."), 

    publisher = models.ForeignKey(\
        Publisher, on_delete= models.CASCADE)
    
    contributor = models.ManyToManyField('Contributor', through="BookContributor")




class BookContributor(models.Model):
    class ContribtionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    contributor = models.ForeignKey(Contributor, on_delete= models.CASCADE)

    role = models.CharField(\
        verbose_name="The role of the contributor for the book", \
            choices= ContribtionRole.choices, max_length= 20)
class Reviews(models.Model):
    content = models.TextField(help_text="The Review text.")
    rating = models.IntegerField(help_text="The rating the reviewer has given")
    date_created = models.DateTimeField(auto_now=True, help_text="The date and time the review was created")
    date_edited = models.DateTimeField(null=True, help_text= " The date and time the review was last edited")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete= models.CASCADE, help_text="The book that this review is for.")


