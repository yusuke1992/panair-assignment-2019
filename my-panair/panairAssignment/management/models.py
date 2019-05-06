from django.db import models
import math
from django.db.models import Sum
from django.utils import timezone
from collections import Counter
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    name = models.CharField('名前', max_length = 20)
    age = models.IntegerField('年齢')
    gender = models.IntegerField('性別', choices= ((1,'男性'), (2,'女性')),
    default = 1)

    def __str__(self):
        return self.name

class Curriculum(models.Model):
    name = models.CharField('カリキュラム名', max_length = 20)
    basic_charge = models.IntegerField ('基本料金')
    metered_charge = models.IntegerField ('従量料金')

    def __str__(self):
        return self.name

class Record(models.Model):
    user = models.ForeignKey(User, verbose_name = 'ユーザー', on_delete = models.CASCADE)
    curriculum = models.ForeignKey(Curriculum,verbose_name = 'カリキュラム',on_delete = models.CASCADE)
    date = models.DateField('受講日',default = timezone.now)
    time = models.IntegerField('受講時間', validators = [MinValueValidator(1),
    MaxValueValidator(12)])
    charge = models.IntegerField('支払い金額',default = 0)

class Invoice:
    def __init__(self, user):
        self.user = user
        self.records = user.record_set.filter()

    def curriculum_list(self):
        curriculum_list = []
        for record in self.records:
            curriculum_list.append(record.curriculum.name)
            curriculum_counting = Counter(curriculum_list)
            
        return curriculum_counting, 

    # def counting_subjects(self, curriculum_list):
    #     (curriculum_list)
    #     return curriculum_list.count("英語")

    def charge(self):
        return sum([ record.charge for record in self.records ])

class Report:
    records_ally = []

    def __init__(self, **kwargs):
        self.records_ally = [ record for record in Record.objects.filter(**kwargs) ]

    def records_count(self):
        return len(self.records_ally)

    def curriculums(self):
        return list(set([ record.curriculum for record in self.records_ally ]))

    @property
    def users(self):
        return list(set([ record.user for record in self.records_ally ]))

    def users_count(self):
        return len(self.users)

    def sum_charge(self):
        return sum([ record.charge for record in self.records_ally ])

