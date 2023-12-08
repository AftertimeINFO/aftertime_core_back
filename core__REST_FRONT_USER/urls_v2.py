from rest_framework.routers import DefaultRouter, SimpleRouter
from core__REST_FRONT_USER.api_rest import ShipsViewSet
from core__REST_FRONT_USER.api_rest import BalanceSubstancesRelationsFromViewSet
from core__REST_FRONT_USER.api_rest import BalanceSubstanceViewSet
from django.urls import path
from . import api_rest

router = SimpleRouter()

router.register("ships", ShipsViewSet)
router.register("relations_from", BalanceSubstancesRelationsFromViewSet)
# router.register("substances", BalanceSubstanceViewSet)


urlpatterns = [
    path('substances/', api_rest.BalanceListView.as_view()),
              ] + router.urls