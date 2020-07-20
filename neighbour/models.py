from django.db import models
import datetime as dt

# Create your models here.
#class Admin(models.Model):
 #   first_name = models.CharField(max_length =30)
  #  last_name = models.CharField(max_length =30)
   # email = models.EmailField()

#    def __str__(self):
#        return self.first_name

#    def save_admin(self):
#        self.save()

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.username

    def save_user(self):
        self.save()


# class Author(models.Model):
#     first_name = models.CharField(max_length =30)
#     last_name = models.CharField(max_length =30)
#     email = models.EmailField()

#     def __str__(self):
#         return self.author

#     def save_author(self):
#         self.save()

class Mwenyeji(models.Model):
    first_name = models.CharField(max_length =30)     
    def __str__(self):
        return self.name

    def save_mwenyeji(self):
        self.save()

class Hood(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    image = models.ImageField(upload_to='hood_photo', blank=True, default='hood/hood.jpg')
    pub_date = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_photo', blank=True, default='profile_photo/profile.jpg')
    bio = models.CharField(max_length=255, blank=True)
    contacts = models.CharField(max_length=200)
    join_date = models.DateTimeField(auto_now_add=True)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile' 

# class Establishment(models.Model):
#     name = models.CharField(max_length=20)
#     location = models.CharField(max_length=20)
#     contact = models.CharField(max_length=30)
#     image = models.ImageField(upload_to='facilities', blank=True, default='establishment/sample.jpg')
#     pub_date = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     hood = models.ForeignKey(Hood, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.name}'