from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Campaign, Member, Task
from .serializers import MemberSerializer, TaskSerializer, CampaignSerializer

# Create your views here.
class CampaignList(ListCreateAPIView):
    """
    Requests

    Get: Lists all the available campaigns
    Post: Creates a new campaign, should provide name
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CampaignEdit(RetrieveUpdateDestroyAPIView):
    """
    Requests

    Get: Provides the details of the campaign whose uuid is porovided in the url
    Put: Edits the retrieved campaign details
    Delete: Deletes the retrieved campaign
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

