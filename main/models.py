from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=255)


class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    english_certificate = models.BooleanField(default=False)
    phone = models.CharField(max_length=13)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name='teachers')

    def __str__(self):
        return self.full_name