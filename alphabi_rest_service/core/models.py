from django.db import models


class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    measure = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        db_table = 'data'
        permissions = (
            ("view_data", "Can see data"),
        )
