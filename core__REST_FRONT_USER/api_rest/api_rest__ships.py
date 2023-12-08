from core.models.vehicles import ModelShips
from core.models.balance import BalanceSubstancesRelationsTo
from core.models.balance import BalanceSubstancesRelationsFrom
from rest_framework import authentication, permissions, serializers, viewsets
from rest_framework.permissions import AllowAny
import django_filters

class ShipsSerializer(serializers.ModelSerializer):
    model = ModelShips

    class Meta:
        model = ModelShips
        fields = ("id", "name", "type", "flag", "lat", "lon")


class ShipsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ModelShips.objects.all()
    serializer_class = ShipsSerializer
    search_fields = ["name"]
    permission_classes = [AllowAny, ]


class BalanceSubstancesRelationsToSerializer(serializers.ModelSerializer):
    model = BalanceSubstancesRelationsTo

    class Meta:
        model = BalanceSubstancesRelationsTo
        fields = ("id", "value", "value_from",)


class BalanceSubstancesRelationsFromSerializer(serializers.ModelSerializer):
    model = BalanceSubstancesRelationsFrom

    class Meta:
        model = BalanceSubstancesRelationsFrom
        fields = ("id", "value",)

class BalanceSubstancesRelationsFromFilterSet(django_filters.FilterSet):
    id = django_filters.Filter(field_name="id", lookup_expr="contains")

    class Meta:
        model = BalanceSubstancesRelationsFrom
        fields = ["id",]

class BalanceSubstancesRelationsFromViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BalanceSubstancesRelationsFrom.objects.all()
    serializer_class = BalanceSubstancesRelationsFromSerializer
    # filterset_class = BalanceSubstancesRelationsFromFilterSet
    filterset_fields = ["id", "value"]
    # search_fields = ["id", "value"]
    permission_classes = [AllowAny, ]

