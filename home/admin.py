from django.contrib import admin
from .models import Campaign, Member, Task

# Register your models here.
admin.site.register(Campaign)
admin.site.register(Member)
admin.site.register(Task)
