from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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

#todo:consider adding a log class to log every activity


class UserManager(BaseUserManager):
    def create_user(self, email, username, password, lastCreation=None, lastEval=None):
        if not email:
            raise ValueError('Users must have an email address')

        if lastCreation is None:
            user = self.model(
                email=self.normalize_email(email),
                username=username
            )
        else:
            user = self.model(
                email=self.normalize_email(email),
                username=username,
                lastmodelcreation=lastCreation,
                lastmodelevaluation=lastEval,
            )

        user.set_password(password)
        user.save(using=self._db)
        print 'created user %s' %username

        return user

    def create_superuser(self, email, username, password, lastCreation=None, lastEval=None):
        user = self.create_user(email=email, username=username, password=password, lastCreation=lastCreation,
                                lastEval=lastEval)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )

    username = models.CharField(
        verbose_name='user name',
        max_length=128,
        unique=True
    )

    lastmodelcreation = models.DateTimeField(
        verbose_name='last creation',
        null=True,
        blank=True
    )
    lastmodelevaluation = models.DateTimeField(
        verbose_name='last evaluation',
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin


class Plan(models.Model):
    name = models.CharField(max_length=128)
    initial_points = models.FloatField()
    additional_points = models.FloatField()
    creation_time = models.DateTimeField()
    geometry = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='plans', blank=True)
    similarity = models.FloatField()
    #fields with relations
    user = models.ForeignKey(myproject.settings.AUTH_USER_MODEL)
    relation = models.ForeignKey('self', related_name='parent', null=True, blank=True)


    def total_points(self):
        return self.additional_points + self.initial_points

    def get_absolute_url(self):
        return '/plan/%i' % self.id

    def __unicode__(self):
        return u'%s:%s' % (self.name, str(self.total_points()))