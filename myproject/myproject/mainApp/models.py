from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    points = models.FloatField()
    avatar = models.ImageField(upload_to='avatar',blank=True)
    last_creation = models.DateTimeField()
    last_evaluation = models.DateTimeField()


    def get_absolute_url(self):
        return '/user/%i' %self.id

    def __unicode__(self):
        return u'%s' %self.name


class Plan(models.Model):
    name = models.CharField(max_length=128)
    initial_points = models.FloatField()
    additional_points  = models.FloatField()
    creation_time = models.DateTimeField()
    geometry = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='plans',blank=True)
    similarity = models.FloatField()
    #fields with relations
    user = models.ForeignKey(User)
    relation = models.ForeignKey('self',related_name='parent',null=True,blank=True)


    def total_points(self):
        return self.additional_points + self.initial_points

    def get_absolute_url(self):
        return '/plan/%i' %self.id

    def __unicode__(self):
        return u'%s:%s' %(self.name,str(self.total_points()))