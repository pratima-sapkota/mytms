from rest_framework import serializers
from .models import Campaign, Task, Member

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        exclude = ["id"]

class MemberSerializer(serializers.ModelSerializer):
    campaign = CampaignSerializer(read_only = True)
    class Meta:
        model = Member
        exclude = ["id"]

class TaskSerializer(serializers.ModelSerializer):
    submitted_by = MemberSerializer()
    reviewed_by = MemberSerializer()
    class Meta:
        model = Task
        exclude = ["id"]

