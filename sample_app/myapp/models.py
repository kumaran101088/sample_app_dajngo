from django.db import models

# Create your models here.

class Member(models.Model):
    member_id = models.IntegerField()
    age = models.IntegerField()
    gender = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    st_bp = models.IntegerField()
    dy_bp = models.IntegerField()
    chol = models.IntegerField()
    gluc = models.IntegerField()
    smoke = models.IntegerField()
    alco = models.IntegerField()
    active = models.IntegerField()
    cardio = models.IntegerField()
    medication = models.CharField(max_length=1)
    score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.member_id)

class Activity(models.Model):
    patient = models.ForeignKey(Member, on_delete=models.CASCADE)
    a_date = models.DateField()
    steps = models.IntegerField()

    def __str__(self):
        return f'{str(self.patient.member_id)} - {str(self.a_date)}'
    