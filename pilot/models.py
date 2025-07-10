from django.db import models
from universe.models import Universe

class Pilot(models.Model):
    pilot_id = models.AutoField(db_column='pilot_id', primary_key=True)
    pilot_name = models.CharField(db_column='pilot_name', max_length=100, blank=True, null=True)
    pilot_images = models.ImageField(db_column='pilot_images', upload_to='pilot_images/', blank=True, null=True)
    pilot_universe = models.ForeignKey(Universe, db_column='pilot_universe', on_delete=models.SET_NULL, null=True, blank=True, related_name='pilot_in_universe')
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'pilot'

    def __str__(self):
        return self.pilot_name or f"Pilot {self.pilot_id}"
 