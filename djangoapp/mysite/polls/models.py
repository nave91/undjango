from django.db import models

# Create your models here.
from django.db import models

import datetime
from django.utils.timezone import now

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return now() - datetime.timedelta(days=1) <= self.pub_date <= now()


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text