# Generated by Django 5.1 on 2024-09-02 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_alter_campaign_options_alter_member_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="campaign",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="TaskCampaign",
                to="home.campaign",
            ),
        ),
        migrations.AlterField(
            model_name="member",
            name="campaign",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="AssignedCampaign",
                to="home.campaign",
            ),
        ),
    ]
