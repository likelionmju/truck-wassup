from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, user_id, username, password):
        user = self.model(
            user_id=user_id,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class MasterUser(AbstractBaseUser):
    username = models.CharField(max_length=30, verbose_name='푸드트럭명')
    id = models.CharField(max_length=16, unique=True, verbose_name='아이디', primary_key=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    CHOICES_CATEGORY = (
        ('치킨', '치킨'),
        ('햄버거', '햄버거'),
    )

    category = models.CharField(max_length=10, choices=CHOICES_CATEGORY)
    
    # 유저 매니저 연결
    objects = UserManager()

    def __str__(self):
        return self.username