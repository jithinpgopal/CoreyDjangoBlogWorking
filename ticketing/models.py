from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
STATUS_CHOICES = (
    ('new','NEW'),
    ('accepted', 'ACCEPTED'),
    ('completed','COMPLETED'),
    ('overdue','OVERDUE'),

)

class Delivery_group(models.Model):
    group_name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.group_name

class Casefile(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='new')
    due_date = models.DateTimeField(default=(timezone.now() + timezone.timedelta(30)))
    del_group = models.ForeignKey(Delivery_group, on_delete=models.SET(1) , default=1)

    def __str__(self):
        return self.title

class Comment(models.Model):
    CaseFile = models.ForeignKey(Casefile, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.SET('USER DELETED'))
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
