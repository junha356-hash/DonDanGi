# user/models.py

from django.db import models
from django.contrib.auth.models import User
from products.models import DepositProducts, SavingProducts

RISK_CHOICES = [
    ('aggressive', '공격적'),
    ('defensive', '방어적'),
    ('balanced', '균형적'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', '남성'), ('F', '여성')], null=True, blank=True)
    risk_profile = models.CharField(
        max_length=20,
        choices=RISK_CHOICES,
        null=True,
        blank=True
    )
    liquid_assets = models.PositiveIntegerField(null=True, blank=True)
    annual_income = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    my_deposits = models.ManyToManyField(DepositProducts, blank=True, related_name='users_with_deposit')
    my_savings = models.ManyToManyField(SavingProducts, blank=True, related_name='users_with_saving')

    def __str__(self):
        return f"{self.user.username}님의 프로필"
