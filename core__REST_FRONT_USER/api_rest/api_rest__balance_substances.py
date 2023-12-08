from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers as rf_serializers

# from pullgerReflection.com_linkedin import models
# from pullgerReflection.com_linkedin import api

# from pullgerInternalControl.pullgerReflection.REST.logging import logger

from .. import serializers
# from .general import CustomPaginator
from core.api import balance_substances
from core.models.balance.balance_general import BalanceSubstancesTotal
from core.models.balance.balance_general import BalanceSubstancesRelations
from core.models.general.substances import Substances


class SubstanceSerializerTest(rf_serializers.ModelSerializer):
    class Meta:
        model = Substances
        fields = ['name', ]

class TotalSerializer(rf_serializers.ModelSerializer):
    class Meta:
        model = BalanceSubstancesRelations
        fields = [ "id", "value" ]


class BalanceSubstancesSerializerItemTest(rf_serializers.ModelSerializer):
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
        fields = ['id', 'moment', 'initial_total', 'final_total', 'substance', 'total',]




class BalanceListView(generics.GenericAPIView,
                   mixins.ListModelMixin,):

    # permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)
    # pagination_class = CustomPaginator
    # queryset = balance_substances.get_all()


    def get(self, request, *args, **kwargs):
        # queryset = balance_substances.get_balances_by_substances()
        # queryset = balance_substances.get_balances_by_substances()
        # queryset = balance_substances.substance_residues()
        # queryset = BalanceSubstancesTotal.objects.get_all()
        queryset = BalanceSubstancesTotal.objects.all()
        # serializer_class = serializers.BalanceSubstancesSerializerItem
        serializer_class = BalanceSubstancesSerializerItemTest

        # try:
        #     returnResponse = self.list(request, *args, **kwargs)
        # except BaseException as e:
        #     pass

        self.serializer_class = serializer_class
        self.queryset = queryset

        # ser = serializer_class(queryset, many=True)
        # return Response(ser.data)

        # ser = serializer_class(queryset, many=True)
        return self.list(request, *args, **kwargs)
