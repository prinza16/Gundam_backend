from django.db import models

class Universe(models.Model):
    universe_id = models.AutoField(db_column='universe_id', primary_key=True)
    universe_name = models.CharField(db_column='universe_name', max_length=100, blank=True, null=False)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'universe'

    def __str__(self):
        return self.universe_name or f"Universe {self.universe_id}"
