from django.db import models
import uuid

# Create your models here.
class Campaign(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False, help_text="Name of the Campaign")
    created = models.DateTimeField(auto_now_add=True, help_text="When the campaign was created")
    modified = models.DateTimeField(auto_now=True, help_text="When the campaign was modified")

    class Meta:
        ordering = ['-created']
        verbose_name = "Campaign"

    def __str__(self):
        return f"{self.name}"

class Member(models.Model):
    CHOICES = ('trainer', 'trainer'), ('lead', 'lead')
    
    email = models.EmailField(primary_key=True, null=False, blank=False)
    role = models.CharField(choices=CHOICES, default='trainer', max_length=50, null=False, blank=False)
    name =  models.CharField(max_length=250, null=False, blank=False, help_text="full name of the member")
    created = models.DateTimeField(auto_now_add=True, help_text="When the member was created")
    modified = models.DateTimeField(auto_now=True, help_text="When the member details was modified")
    campaign =  models.ForeignKey(Campaign, on_delete=models.PROTECT, related_name="Campaign", null=True)
    
    class Meta:
        ordering = ['-created']
        verbose_name = "Member"

    def __str__(self):
        return f"{self.name} : Role {self.role}"


class Task(models.Model):
    CHOICES = ('choices', 'choices'), ('simple life cycle', 'simple life cycle')

    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False, null=False, blank=False)
    name =  models.CharField(max_length=250, null=False, blank=False, help_text="Task name")
    status = models.CharField(choices=CHOICES, default='choices', max_length=50, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, help_text="When the task was created")
    modified = models.DateTimeField(auto_now=True, help_text="When the task was modified")
    submitted_by = models.ForeignKey(Member, on_delete=models.PROTECT, related_name="Trainer", null=True)
    reviewed_by = models.ForeignKey(Member, on_delete=models.PROTECT, related_name="Lead", null=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "Task"

    def __str__(self):
        return f"{self.name} : Status {self.status}"

