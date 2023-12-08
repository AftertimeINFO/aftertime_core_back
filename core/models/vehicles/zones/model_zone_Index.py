from django.db import models
from .model_zones import *


class ZoneIndexManager(models.Manager):
    pass


class ZoneIndex(models.Model):
    id = models.AutoField(primary_key=True)
    lat_l = models.FloatField(blank=False, null=False)
    lat_g = models.FloatField(blank=False, null=False)
    lon_l = models.FloatField(blank=False, null=False)
    lon_g = models.FloatField(blank=False, null=False)

    objects = ZoneIndexManager()


class ZoneIndexZone(models.Manager):
    pass

class ZoneIndexZones(models.Model):
    id = models.AutoField(primary_key=True)
    zone_index = models.ForeignKey(ZoneIndex, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zones, on_delete=models.CASCADE)

    objects = ZoneIndexZone()

    class Meta:
        db_table = "vehicles_zone_index"




