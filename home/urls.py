from django.urls import path, include
from .views import CampaignList, CampaignEdit, MemberEdit, MemberList, TaskEdit, TaskList

urlpatterns = [
    path("campaign/", CampaignList.as_view()),
    path("campaign/<uuid:id>/", CampaignEdit.as_view()),

    path("member/", MemberEdit.as_view()),
    path("member/<uuid:id>/", MemberEdit.as_view()),

    path("task/", TaskList.as_view()),
    path("task/<uuid:id>/", TaskEdit.as_view()),
]
