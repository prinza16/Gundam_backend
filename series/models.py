from django.db import models
from universe.models import Universe

class Series(models.Model):
    series_id = models.AutoField(db_column='series_id', primary_key=True)
    series_name = models.CharField(db_column='series_name', max_length=100, blank=True, null=False)
    series_image = models.ImageField(db_column='series_image', upload_to='series_images/', blank=True, null=True)
    series_universe = models.ForeignKey(Universe, db_column='series_universe', on_delete=models.SET_NULL, null=True, blank=True, related_name='series_in_universe')
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'series'

    def __str__(self):
        return self.series_name or f"Series {self.series_id}"
