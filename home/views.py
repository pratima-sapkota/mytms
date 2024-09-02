from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Campaign, Member, Task
from .serializers import MemberSerializer, TaskSerializer, CampaignSerializer
import datetime
from rest_framework.response import Response

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


class FetchTasks(ListAPIView):
    """
    Requests

    Get: Takes a date parameter (required format yyyy-mm-dd) and returns the tasks created from the date provided till 6 days later (Both inclusive) i.e. a week
    returns empty value if the format of the date is not as expected
    """
    serializer_class = TaskSerializer

    def get_queryset(self, **kwargs):
        start_date =  self.kwargs.get('date', None)
        if start_date:
            try:
                start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            except Exception:
                return []
                # return Response("Invalid date format. Format should be yyyy-mm-dd.", status = 400)
            
            end_date = start_date + datetime.timedelta(days = 6)
            queryset = Task.objects.filter(created__gte = start_date, created__lte = end_date)
            return queryset
        return []