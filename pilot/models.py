from django.db import models

class Pilot(models.Model):
    pilot_id = models.AutoField(db_column='pilot_id', primary_key=True)
    pilot_name = models.CharField(db_column='pilot_name', max_length=100, blank=True, null=True)
    pilot_image = models.ImageField(db_column='pilot_images', upload_to='pilot_images/', blank=True, null=True)
    pilot_vehicle = models.CharField(db_column='pilot_vehicle', max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'pilot'
