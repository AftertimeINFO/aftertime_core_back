import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from core.api.zones import zone
from core.models.vehicles import ModelShipLocation

res1 = ModelShipLocation.objects.filter(zone=None)

select_all = ModelShipLocation.objects.filter(zone=None)
for curMSL in select_all:
    zone.get_belong_zone_by_coordinates(curMSL.lat, curMSL.lon)
pass