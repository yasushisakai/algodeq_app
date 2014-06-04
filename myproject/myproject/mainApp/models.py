from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import myproject.settings
import json

from datetime import datetime


class UserManager(BaseUserManager):
    """
    manager class that manipulates Users
    """

    def create_user(self, email, username, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            model_creation_time=datetime.now(),
            model_evaluation_time=datetime.now()
        )

        user.set_password(password)
        user.save(using=self._db)

        print '***added user %s.***' % username

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    """
    user class that participates making, evaluate models.
    """

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    username = models.CharField(
        verbose_name='user name',
        max_length=255,
        unique=True
    )
    model_creation_time = models.DateTimeField(
        verbose_name='last model creation time',
    )
    model_evaluation_time = models.DateTimeField(
        verbose_name='last model evaluation time',
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)  # weather its accessible to the admin site.

    objects = UserManager()  # meta class for creating users or get as a whole

    USERNAME_FIELD = 'email'  # email works as the id to login
    REQUIRED_FIELDS = ['username']  # mandatory fields to create

    # ------------------------------------------------------------------------------------------

    def __unicode__(self):
        return str(self.id) + '_' + self.username

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.get_full_name()

    def is_staff(self):
        return self.is_admin

    def update_evaluation_time(self):
        self.model_evaluation_time = datetime.now()
        self.save()

    def update_creation_time(self):
        self.model_creation_time = datetime.now()
        self.save()

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True


class Plan(models.Model):
    """
    single plan data
    """

    # general info
    name = models.CharField(max_length=128, unique=True)
    creation_time = models.DateTimeField()
    image_file = models.ImageField(upload_to='plans', blank=True)
    geometry = models.CharField(max_length=5000)
    similarity = models.FloatField()

    # points
    points_inborn = models.FloatField()  # points inherited by parent Plan
    points_acquired = models.FloatField()  # points acquired by voting

    # foreign keys
    architect = models.ForeignKey(myproject.settings.AUTH_USER_MODEL)
    parent_plan = models.ForeignKey('self', related_name='parent model', null=True, blank=True)

    # ------------------------------------------------------------------------------------------

    def __unicode__(self):
        return self.name

    def get_total_points(self):
        return self.points_inborn + self.points_acquired

    def get_absolute_url(self):
        return '/plan/%s' % self.name

    def get_dict(self):

        parent_plan = self.parent_plan

        if self.parent_plan is None:
            parent_plan_name = ''
        else:
            parent_plan_name = parent_plan.name

        dict_format = {
            'id': self.id,
            'name': self.name,
            'creation_time': self.creation_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'image_file': self.image_file.name,
            'geometry': self.geometry,
            'similarity': self.similarity,
            'points_inborn': self.points_inborn,
            'points_acquired': self.points_acquired,
            'architect': self.architect.username,
            'parent_plan': parent_plan_name
        }

        return dict_format

    def get_json(self):
        dict_format = self.get_dict()

        if dict_format['image_file'] is None:
            dict_format['image_file'] = ''

        return json.dumps(dict_format)

    def add_points(self):
        self.points_acquired += 10.0
        # todo: add points to parent model

        self.save()

    def validate_new_plan(
            self,
            new_plan_name,
            new_plan_geometry,
            new_plan_similarity):

        if self.geometry is new_plan_geometry:
            return {'is_validation': False, 'message': 'geometry same as parent'}

        if new_plan_similarity >= 1.0:
            return {'is_validation': False, 'message': 'similarity is 1.0'}

        is_unique = False
        try:
            Plan.objects.get(name=new_plan_name)
        except:
            return {'is_validation': True, 'message': ''}

        return {'is_validation': False, 'message': 'model name not unique'}

    @classmethod
    def tree_search(cls, _array, _plan):
        for a in _array:
            if a['id'] == _plan.parent_plan.id:

                a['children'].append(
                    {'id': _plan.id,
                     'name': _plan.name,
                     'url': _plan.get_absolute_url(),
                     'parent': _plan.parent_plan.id,
                     'geometry': _plan.geometry,
                     'children': []
                    }
                )
            else:
                Plan.tree_search(a['children'], _plan)


class Log(models.Model):
    """
    simple activity log throughout process
    """

    is_creation = models.BooleanField()
    # True if the activity is creating(adding models),
    # False if its a evaluation
    when = models.DateTimeField(auto_now=True)

    # foreign keys
    who = models.ForeignKey(myproject.settings.AUTH_USER_MODEL)
    what = models.ForeignKey(Plan)

    #------------------------------------------------------------------------------------------

    def __unicode__(self):
        activity = 'Ev'
        if self.is_creation:
            activity = 'Mk'

        return '[%s: %i -> %i]' % (activity, self.who.id, self.what.id)












