from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Hood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Notices)
admin.site.register(Establishment)