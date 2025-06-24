from django.db import models

class Grade(models.Model):
    grade_id = models.AutoField(db_column='grade_id', primary_key=True)
    grade_name = models.CharField(db_column='grade_name', max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'grade'
