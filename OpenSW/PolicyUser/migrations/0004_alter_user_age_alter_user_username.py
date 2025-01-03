# Generated by Django 5.1.3 on 2024-11-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PolicyUser', '0003_user_access_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
