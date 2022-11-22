from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    GENDER = (
        ('male', 'мужчина'),
        ('female', 'женшина')
    )
    STATUS = (
        ('Готово', 'done'),
        ('Астывна', 'active'),
        ('Отменён', 'block'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    gender = models.CharField(choices=GENDER, max_length=100)
    was_born = models.DateField(default='2004-01-01')
    passport_left = models.FileField(upload_to='document')
    passport_right = models.FileField(upload_to='document')
    recipient_amonatbonck = models.FileField(upload_to='amonatbonck')
    phone = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    status_document = models.CharField(max_length=100, choices=STATUS, default='Астывна')
    message = models.TextField(blank=True, default='Test Message')
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    update_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    email = models.EmailField()
    editable = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"
