from django.db import models

# Create your models here.
class Admin(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def save_admin(self):
        self.save()

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

class Hood(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    image = models.ImageField(upload_to='hood_photo', blank=True, default='hood_photo/hood.jpg')
    pub_date = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'