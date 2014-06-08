from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import myproject.settings

from datetime import datetime, timedelta

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, password, lastCreation=None, lastEval=None):
        if not email:
            raise ValueError('Users must have an email address')

        if lastCreation is None:
            user = self.model(
                email=self.normalize_email(email),
                username=username,
                lastmodelcreation=datetime.now() - timedelta(minutes=31),
                lastmodelevaluation=datetime.now() - timedelta(minutes=6)
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
        print 'created user %s' % username

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
    )
    lastmodelevaluation = models.DateTimeField(
        verbose_name='last evaluation',
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

    def next_creation(self):
        threshold = 30  #mintues
        seconds_past = (datetime.utcnow() - self.lastmodelcreation.replace(tzinfo=None)).total_seconds()

        seconds_untill = threshold * 60 - seconds_past

        if seconds_untill < 0:
            return 0
        else:
            return seconds_untill


    def next_evaluation(self):
        threshold = 5  # minutes

        seconds_past = (datetime.utcnow() - self.lastmodelevaluation.replace(tzinfo=None)).total_seconds()

        seconds_untill = threshold * 60 - seconds_past
        if seconds_untill < 0:
            return 0
        else:
            return seconds_untill


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


def tree_search(_array, _plan):
    for a in _array:
        if a['id'] == _plan.relation.id:
            a['children'].append(
                {'id': _plan.id, 'name': _plan.name, 'parent': _plan.relation.id, 'geometry': _plan.geometry,
                 'children': []})
        else:
            tree_search(a['children'], _plan)