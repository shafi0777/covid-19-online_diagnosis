from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager


# Create your models here.

class CovidiaAppUserManager(BaseUserManager):
    def create_user(self,email,username,password = None):
       
        if not username: 
            raise ValueError("Users must have an username")
        if not email:
            raise ValueError("Users must have an email address")
       
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CovidiaAppUser(AbstractBaseUser):
    username = models.CharField(max_length=100,blank=False,unique=True)
    email = models.EmailField(verbose_name='email',max_length=100,unique=True)
    password = models.CharField(max_length=50,null=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = CovidiaAppUserManager()

    def __str__(self):          
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_lable):
        return True


