import uuid as lib_uuid
import datetime
import decimal

# from .directRequest import direct_request
from django.db import models
from django.db.models import signals
from django.db.models import Avg, Count, Min, Sum, F
from django.dispatch import receiver
from core.models.general.model_substances import *
# from .balance_substances import *
from core.models.general.model_locations import *


class BalanceSubstancesTotalManager(models.Manager):
    def get_all(self):
        return BalanceSubstancesTotal.objects.prefetch_related("substance").values("id", "moment", "initial_total",
                                                                            "final_total", "substance__name")

class BalanceSubstancesTotal(models.Model):
    id = models.AutoField(primary_key=True)
    moment = models.DateField(null=True)
    substance = models.ForeignKey(Substances, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Locations, on_delete=models.DO_NOTHING)

    initial_total = models.BigIntegerField()
    final_total = models.BigIntegerField()

    objects = BalanceSubstancesTotalManager()

    class Meta:
        db_table = "balance_substances_total"

class BalanceProcess(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False)

    class Meta:
        db_table = "balance_process"


class BalanceSubstancesRelationsTo(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.ForeignKey(BalanceSubstancesTotal, related_name='total_from', on_delete=models.DO_NOTHING)
    value = models.BigIntegerField()
    value_from = models.BigIntegerField()
    substance_from = models.ForeignKey(Substances, related_name='substance_from', on_delete=models.DO_NOTHING)
    process_from = models.ForeignKey(BalanceProcess, related_name='process_to', on_delete=models.DO_NOTHING)
    # substance = models.ForeignKey(Substances, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "balance_substances_relations_to"


class BalanceSubstancesRelationsFrom(models.Model):
    id = models.AutoField(primary_key=True)
    total_to = models.ForeignKey(BalanceSubstancesTotal, related_name='total_to', on_delete=models.DO_NOTHING)
    value = models.BigIntegerField()
    value_to = models.BigIntegerField()
    substance_to = models.ForeignKey(Substances, related_name='substance_to', on_delete=models.DO_NOTHING)
    process_from = models.ForeignKey(BalanceProcess, related_name='process_from', on_delete=models.DO_NOTHING)
    # substance = models.ForeignKey(Substances, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "balance_substances_relations_from"