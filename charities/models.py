from django.db import models
from accounts.models import User

EXPERIENCE = (
    (0, 'Elementary'),
    (1, 'Intermediate'),
    (2, 'Professional'),
)

STATE = (
    ('A', 'Assigned'),
    ('P', 'Pending'),
    ('W', 'Waiting'),
    ('D', 'Done'),
)
GENDER = (
    ('F', 'Female'),
    ('M', 'Male')
)


class Benefactor(models.Model):
    user = models.OneToOneField('accounts.User', verbose_name='user', on_delete=models.CASCADE)
    experience = models.SmallIntegerField('experience', choices=EXPERIENCE, default=0)
    free_time_per_week = models.PositiveSmallIntegerField('free time', default=0)


class Charity(models.Model):
    user = models.OneToOneField('accounts.User', verbose_name='user', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=50)
    reg_number = models.CharField('register number', max_length=10)


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return self.filter(charity__user=user)

    def related_tasks_to_benefactor(self, user):
        return self.filter(assigned_benefactor__user=user)

    def all_related_tasks_to_user(self, user):
        return self.all()


class Task(models.Model):
    assigned_benefactor = models.ForeignKey(Benefactor, verbose_name='benefactor', on_delete=models.SET_NULL, null=True)
    charity = models.ForeignKey(Charity, verbose_name='charity', on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(null=True, blank=True)
    age_limit_to = models.IntegerField(null=True, blank=True)
    date = models.DateField('date', null=True, blank=True)
    description = models.TextField('description', null=True, blank=True)
    gender_limit = models.CharField('gender limit', choices=GENDER, max_length=1, null=True, blank=True)
    state = models.CharField('state', choices=STATE, default='P', max_length=1)
    title = models.CharField('title', max_length=100)
    objects = TaskManager()
