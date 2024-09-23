# Generated by Django 5.0.6 on 2024-09-23 06:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friend', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='RequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_status', models.BooleanField(default=False)),
                ('requested_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='requested_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]