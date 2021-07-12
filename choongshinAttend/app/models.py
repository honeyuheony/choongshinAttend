from django.db import models

# Create your models here.


class Child(models.Model):
    name = models.CharField(max_length=200, null=False, default='')
    classname = models.CharField(max_length=200, null=False, default='')
    grade = models.IntegerField(null=False, default='')

    def __str__(self):
        return self.name

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
        return str(self.child_id) + " " + str(self.att_date) + " " + "출석"

    def to_json(self):
        return{
            'child_id': self.child_id,
            'att_worship': self.att_worship,
            'att_zoom': self.att_zoom,
            'att_date': self.att_date,
            'recode_date': self.recode_date,
            'att_memo': self.att_memo
        }
