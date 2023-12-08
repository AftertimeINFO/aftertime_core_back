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
from core.models.balance.model_balance_general import BalanceSubstancesTotal
from core.models.balance.model_balance_general import BalanceSubstancesRelationsTo
from core.models.balance.model_balance_general import BalanceSubstancesRelationsFrom
from core.models.general.model_substances import Substances


class SubstanceSerializerTest(rf_serializers.ModelSerializer):
    class Meta:
        model = Substances
        fields = ['name', ]

class SubstanceSerializer(rf_serializers.ModelSerializer):
    model = Substances

    class Meta:
        model = Substances
        fields = ['name', ]


class SubstanceRelatedField(rf_serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return super().get_queryset()

class RelationToSerializer(rf_serializers.ModelSerializer):
    # substance_from = rf_serializers.CharField()
    # substance_to = SubstanceRelatedField(many=True, queryset=Substances.objects.all(), required=False)
    substance_to = SubstanceSerializer(many=False,  read_only=True)

    class Meta:
        model = BalanceSubstancesRelationsFrom
        fields = [ "id", "value", "value_to", "substance_to"]

class RelationFromSerializer(rf_serializers.ModelSerializer):
    class Meta:
        model = BalanceSubstancesRelationsFrom
        fields = [ "id", "value" ]

class BalanceSubstancesRelationsRelatedField(rf_serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return super().get_queryset()


class BalanceSubstancesSerializerItemTest(rf_serializers.ModelSerializer):
    total_to = RelationToSerializer(many=True, read_only=True)
    # total_to = RelationToSerializer(many=True, read_only=True)
    # total_from = RelationFromSerializer(many=True, read_only=True)
    total_from = BalanceSubstancesRelationsRelatedField(many=True, queryset=BalanceSubstancesRelationsFrom.objects.all(), required=False)
    substance = SubstanceSerializerTest(many=False, read_only=True)
    # substance__name = rf_serializers.CharField()

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
        # fields = ['id', 'moment', 'substance__name']
        fields = ['id', 'moment', 'initial_total', 'final_total', 'substance', 'total_to', 'total_from',]




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
        # BalanceSubstancesTotal.objects.prefetch_related("substance")  select_related("BalanceSubstancesRelationsTo").all()
        queryset = BalanceSubstancesTotal.objects.all()
        self.filterset_fields = ["id", ]
        # queryset = BalanceSubstancesTotal.objects.prefetch_related("substance").values("id", "moment", "substance__name")
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
