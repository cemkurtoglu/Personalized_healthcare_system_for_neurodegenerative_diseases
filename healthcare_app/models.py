import django
from django.conf import settings
from django.db import models
from django.utils.timezone import now


# Create your models here.


class Health_Record(models.Model):
    gender_choices = [('Male', 'Male'), ('Female', 'Female')]
    marital_choices = [('Never Married', 'Never Married'), ('Married', 'Married'), ('Widowed', 'Widowed'),
                       ('Divorced', 'Divorced')]
    disease_choices = [('0', 'MCI'), ('1', 'AD')]

    rid = models.IntegerField(blank=False, null=False)
    first_name = models.CharField(max_length=250, blank=False, null=False)
    last_name = models.CharField(max_length=250, blank=False, null=False)
    birth_date = models.DateField(default=now)
    gender = models.CharField(max_length=250, choices=gender_choices)
    marital_status = models.CharField(max_length=250, choices=marital_choices)
    exam_date = models.DateField(default=now)
    cdrsb = models.FloatField(max_length=250, blank=False, null=False)
    adas11 = models.IntegerField(blank=False, null=False)
    adas13 = models.IntegerField(blank=False, null=False)
    mmse = models.IntegerField(blank=False, null=False)
    ravlt_immediate = models.IntegerField(blank=False, null=False)
    ravlt_learning = models.IntegerField(blank=False, null=False)
    ravlt_forgetting = models.IntegerField(blank=False, null=False)
    faq = models.IntegerField(blank=False, null=False)
    ventricles = models.IntegerField(blank=False, null=False)
    hippocampus = models.IntegerField(blank=False, null=False)
    whole_brain = models.IntegerField(blank=False, null=False)
    entorhinal = models.IntegerField(blank=False, null=False)
    fusiform = models.IntegerField(blank=False, null=False)
    mid_temp = models.IntegerField(blank=False, null=False)
    icv = models.IntegerField(blank=False, null=False)
    diagnosis = models.CharField(max_length=250, blank=False, null=False)

    prediction = models.CharField(max_length=250, choices=disease_choices, blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)

    def get_prediction(self):
        return dict(self.disease_choices).get(self.prediction)

    def __str__(self):
        return str(self.id) + "-" + str(self.rid)
