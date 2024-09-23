# Generated by Django 5.0.6 on 2024-09-16 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
        ('userAccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='storyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='./file/images/')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='story', to='userAccount.useraccount')),
            ],
        ),
    ]
