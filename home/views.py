from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from .models import Campaign, Member, Task
from .serializers import MemberSerializer, TaskSerializer, CampaignSerializer
import datetime

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

    
    Get: Provides the details of the campaign whose uuid is provided in the url
    
    Put: Edits the retrieved campaign details
    
    Delete: Deletes the retrieved campaign
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    lookup_field = 'id'

# Create your views here.
class TaskList(ListCreateAPIView):
    """
    Requests

    
    Get: Lists all the available tasks

    Post: Creates a new task, should provide name, status
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskEdit(RetrieveUpdateDestroyAPIView):
    """
    Requests

    
    Get: Provides the details of the task whose uuid is provided in the url
    
    Put: Edits the retrieved task details
    
    Delete: Deletes the retrieved task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'

# Create your views here.
class MemberList(ListCreateAPIView):
    """
    Requests

    
    Get: Lists all the available members
    
    Post: Creates a new campaign, should provide name, role, campaign id
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberEdit(RetrieveUpdateDestroyAPIView):
    """
    Requests

    
    Get: Provides the details of the member whose email is provided in the url
    
    Put: Edits the retrieved member details
    
    Delete: Deletes the retrieved member
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'email'


class FetchTasks(GenericAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self, **kwargs):
        start_date =  self.request.query_params.get('date')
        start_date = ""
        return None