from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    def __str__(self):
        return self.name

class Title(models.Model):
    name = models.CharField(max_length=50)
    my_title = models.TextField()
    def __str__(self):
        return self.name

class About(models.Model):
    name = models.CharField(max_length=50)
    About_me = models.TextField()
    def __str__(self):
        return self.name

class Modeling(models.Model):
    name = models.CharField(max_length=50)
    Model_img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name

class Art(models.Model):
    name = models.CharField(max_length=50)
    art_img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name

class Coading(models.Model):
    name = models.CharField(max_length=50)
    code_img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name

class Aprojects(models.Model):
    name = models.CharField(max_length=50)
    aproject_img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name

class Work_des(models.Model):
    name = models.CharField(max_length=50)
    des = models.TextField()
    def __str__(self):
        return self.name