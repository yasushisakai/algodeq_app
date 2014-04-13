from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models
import myproject.settings

# Create your models here.


# class User(models.Model):
#     name = models.CharField(max_length=128)
#     email = models.EmailField()
#     password = models.CharField(max_length=50)
#     points = models.FloatField()
#     avatar = models.ImageField(upload_to='avatar',blank=True)
#     last_creation = models.DateTimeField()
#     last_evaluation = models.DateTimeField()
#
#
#     def get_absolute_url(self):
#         return '/user/%i' %self.id
#
#     def __unicode__(self):
#         return u'%s' %self.name


class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = UserManager.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_admin=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=40,unique=True,db_index=True)
    email = models.EmailField(max_length=254,unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Plan(models.Model):
    name = models.CharField(max_length=128)
    initial_points = models.FloatField()
    additional_points  = models.FloatField()
    creation_time = models.DateTimeField()
    geometry = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='plans',blank=True)
    similarity = models.FloatField()
    #fields with relations
    user = models.ForeignKey(myproject.settings.AUTH_USER_MODEL)
    relation = models.ForeignKey('self',related_name='parent',null=True,blank=True)


    def total_points(self):
        return self.additional_points + self.initial_points

    def get_absolute_url(self):
        return '/plan/%i' %self.id

    def __unicode__(self):
        return u'%s:%s' %(self.name,str(self.total_points()))