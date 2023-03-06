from django.db import models

# Create your models here.
class Publisher(models.Model):
    """A company that publishes books"""
    name = models.CharField(\
        max_length=50, \
            help_text="The name of the publisher")
    
    website = models.URLField(help_text = "the company's website")
    email = models.EmailField(\
        help_text="The publisher's email address.")


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
            verbose_name="ISBN number of the book.")


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


class Reviews(models.Model):
    ...

