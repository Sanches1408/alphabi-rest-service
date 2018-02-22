from django.db import models


class AlphaBIData(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    measure = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        db_table = 'data'
