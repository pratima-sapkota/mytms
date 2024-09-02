from django.urls import path, include
from .views import CampaignList

urlpatterns = [
    path("campaign/list/", CampaignList.as_view()),
    path("campaign/<uuid:id>/", CampaignList.as_view()),
]
