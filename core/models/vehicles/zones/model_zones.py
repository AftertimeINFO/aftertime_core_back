from django.db import models

class ZonesManager(models.Manager):
    pass

class Zones(models.Model):
    ZONE_TYPES = (
        ("P", "Port"),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=False, null=False)
    type = models.CharField(max_length=1, blank=False, null=False, choices=ZONE_TYPES)

    objects = ZonesManager()

    class Meta:
        db_table = "vehicles_zones"


class ZonePointsManager(models.Manager):
    pass


class ZonePoints(models.Model):
    id = models.AutoField(primary_key=True)
    zone = models.ForeignKey(Zones, on_delete=models.CASCADE)
    lat = models.FloatField(blank=False, null=False)
    lon = models.FloatField(blank=False, null=False)

    objects = ZonePointsManager()

    class Meta:
        db_table = "vehicles_zone_points"