from core.models.vehicles import ModelShips
from core.models.balance_general import BalanceSubstancesTotal
from rest_framework import authentication, permissions, serializers, viewsets
from rest_framework.permissions import AllowAny
from core.api import balance_substances

class BalanceSubstanceSerializer(serializers.ModelSerializer):
    model = BalanceSubstancesTotal

    class Meta:
        model = BalanceSubstancesTotal
        fields = ("id", "moment", "initial_total", "final_total", "substance__name")


class BalanceSubstanceViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = balance_substances.substance_residues()
    queryset = BalanceSubstancesTotal.objects.get_all()
    serializer_class = BalanceSubstanceSerializer
    # search_fields = ["name"]
    permission_classes = [AllowAny, ]