import json

import django
import os
from rest_framework import serializers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

# from core.api.zones import zone
# from core.models.vehicles import ModelShipLocation
from core.models.balance_general import BalanceSubstancesTotal
from core.models.balance_general import BalanceSubstancesRelations
from core.models.substances import Substances


class SubstanceSerializerTest(serializers.ModelSerializer):
    class Meta:
        model = Substances
        fields = ['name', ]

class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceSubstancesRelations
        fields = [ "id", "value" ]


class BalanceSubstancesSerializerItemTest(serializers.ModelSerializer):
    total = TotalSerializer(many=True, read_only=True)
    substance = SubstanceSerializerTest(many=False, read_only=True)
    # total = serializers.StringRelatedField(many=True)
    # substance = SubstanceSerializer(many=False, read_only=True)
    # substance = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    # id = serializers.IntegerField()
    # moment = serializers.CharField()
    # substance__name = serializers.CharField()
    # initial_total = serializers.IntegerField()
    # final_total = serializers.IntegerField()

    class Meta:
        model = BalanceSubstancesTotal
        fields = ['id','moment', 'substance', 'total',]

# allSimple = BalanceSubstancesTotal.objects.prefetch_related("substance").values("id","moment","initial_total","final_total","substance","substance__name")
# allSimple = BalanceSubstancesTotal.objects.select_related("substance").values("id","moment","initial_total","final_total","substance__name")

allSimple = BalanceSubstancesTotal.objects.all()
sz = BalanceSubstancesSerializerItemTest(allSimple, many=True)
# print(sz.data)
print(json.dumps(sz.data))
# print(BalanceSubstancesSerializerItem(allSimple, many=True).data)

# allSimple
#
#
#
# all = BalanceSubstancesTotal.objects.select_related("substance")\
    # .values("id","moment","initial_total","final_total","substance__name")
# res1 = ModelShipLocation.objects.filter(zone=None)
#
# select_all = ModelShipLocation.objects.filter(zone=None)
# for curMSL in select_all:
#     zone.get_belong_zone_by_coordinates(curMSL.lat, curMSL.lon)
# pass