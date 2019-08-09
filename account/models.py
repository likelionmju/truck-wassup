from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    AREA_CHOICES = (
        ("서울", "서울"), ("부산", "부산"),("대구", "대구"),
        ("인천", "인천"), ("광주", "광주") , ("대전", "대전"),
        ("울산", "울산"), ("세종", "세종"), ("경기도", "경기도"),
        ("강원도", "강원도"), ("충청북도", "충청북도"),("충청남도", "충청남도"),
        ("전라북도", "전라북도"), ("전라남도", "전라남도"), ("경상북도", "경상북도"),
        ("경상남도", "경상남도"), ("제주도", "제주도"),
    )
    area = models.CharField(max_length=5, choices=AREA_CHOICES)

    master = models.BooleanField()
    company = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username

    