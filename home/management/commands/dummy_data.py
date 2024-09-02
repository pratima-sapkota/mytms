import factory
import factory.fuzzy
from factory.django import DjangoModelFactory
from django.core.management.base import BaseCommand
from ...models import Campaign, Member, Task

class CampaignFactory(DjangoModelFactory):
    class Meta:
        model = Campaign

    name = factory.Faker("sentence", nb_words = 4, variable_nb_words= True)

class MemberFactory(DjangoModelFactory):
    class Meta:
        model = Member

    name = factory.Faker("name")
    email = factory.Faker("email")
    role = factory.fuzzy.FuzzyChoice(['trainer', 'lead'])
    campaign = factory.fuzzy.FuzzyChoice(list(Campaign.objects.all()))
    
class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task

    name = factory.Faker("sentence", nb_words = 4, variable_nb_words= True)
    status = factory.fuzzy.FuzzyChoice(['choices', 'simple life cycle'])
    campaign = factory.fuzzy.FuzzyChoice(list(Campaign.objects.all()))
    submitted_by = factory.fuzzy.FuzzyChoice(list(Member.objects.all()))
    reviewed_by = factory.fuzzy.FuzzyChoice(list(Member.objects.all()))


class Command(BaseCommand):
    help = "Creates Dummy data for all models"

    def handle(self, *args, **kwargs):
        CampaignFactory.create_batch(20)
        MemberFactory.create_batch(20)
        TaskFactory.create_batch(30)