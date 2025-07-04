from django.db import models
from grade.models import Grade
from universe.models import Universe
from series.models import Series
from pilot.models import Pilot

class Types(models.Model): #ชนิดของโมเดล เช่น "Mobile Suit", "Mobile Armor", "Mobile Fighter", "Support Unit"
    types_id = models.AutoField(db_column='types_id', primary_key=True)
    types_name = models.CharField(db_column='types_name', max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'types'

class Seller(models.Model): #ผู้ผลิต โมเดล
    seller_id = models.AutoField(db_column='seller_id', primary_key=True)
    seller_name = models.CharField(db_column='seller_name', max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'seller'

class ModelData(models.Model):
    model_id = models.AutoField(db_column='model_id', primary_key=True)
    model_name = models.CharField(db_column='model_name', max_length=100, blank=True, null=True)
    model_grade = models.ForeignKey(Grade, db_column='model_grade', on_delete=models.SET_NULL, null=True, blank=True)
    model_type = models.ForeignKey(Types, db_column='model_type', on_delete=models.SET_NULL, null=True, blank=True)
    model_seller = models.ForeignKey(Seller, db_column='model_seller', on_delete=models.SET_NULL, null=True, blank=True)
    model_initial = models.CharField(db_column='model_initial', max_length=100, blank=True, null=True)
    model_length = models.DecimalField(db_column='model_length', max_digits=10, decimal_places=2, null=True, blank=True)
    model_width = models.DecimalField(db_column='model_width', max_digits=10, decimal_places=2, null=True, blank=True)
    model_height = models.DecimalField(db_column='model_height', max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'model_data'

class ModelPilotAssignment(models.Model):
    model = models.ForeignKey(ModelData, on_delete=models.CASCADE, db_column='model_id')
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE, db_column='pilot_id')

    class Meta:
        unique_together = ('model', 'pilot')
        managed = True
        db_table = 'model_pilot_assignment'

class ModelSeriesOccurrence(models.Model):
    model = models.ForeignKey(ModelData, on_delete=models.CASCADE, db_column='model_id')
    series = models.ForeignKey(Series, on_delete=models.CASCADE, db_column='series_id')

    class Meta:
        unique_together = ('model', 'series')
        managed = True
        db_table = 'model_series_occurrence'

class ModelUniverseOccurrence(models.Model):
    model = models.ForeignKey(ModelData, on_delete=models.CASCADE, db_column='model_id')
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE, db_column='universe_id')

    class Meta:
        unique_together = ('model', 'universe')
        managed = True
        db_table = 'model_universe_occurrence'

class ModelImage(models.Model):
    model_data = models.ForeignKey(ModelData, on_delete=models.CASCADE, db_column='model_id', related_name='images')
    image = models.ImageField(upload_to='model_photos/', blank=True, null=True)
    is_main = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'model_image'
        ordering = ['is_main', '-create_date']
        managed = True
