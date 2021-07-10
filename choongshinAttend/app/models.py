from django.db import models

# Create your models here.


class Child(models.Model):
    name = models.CharField(max_length=200, null=False, default='')
    classname = models.CharField(max_length=200, null=False, default='')
    grade = models.IntegerField(null=False, default='')

    def __str__(self):
        return self.classname + " " + self.name

    class Meta:
        ordering = ['classname']


class Attend(models.Model):
    child_id = models.ForeignKey(Child, on_delete=models.CASCADE, default='')
    att_worship = models.BooleanField(default='')
    att_zoom = models.BooleanField(default='')
    att_date = models.DateField(default='')
    recode_date = models.DateField(default='')
    att_memo = models.CharField(
        help_text="Comment contents", max_length=200, default='', blank=True)

    def __str__(self):
        return str(self.att_date) + " " + "출석"
