from django.contrib import admin
from .models import Casefile , Delivery_group, Comment

# Register your models here.

admin.site.register(Casefile)
admin.site.register(Delivery_group)
admin.site.register(Comment)