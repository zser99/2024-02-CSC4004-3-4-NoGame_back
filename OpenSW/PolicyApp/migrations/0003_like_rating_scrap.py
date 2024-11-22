# Generated by Django 5.1.3 on 2024-11-20 14:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PolicyApp', '0002_policyimage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='PolicyApp.policy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'policy')},
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=1, max_digits=3)),
                ('review', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='PolicyApp.policy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'policy')},
            },
        ),
        migrations.CreateModel(
            name='Scrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scraps', to='PolicyApp.policy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scraps', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'policy')},
            },
        ),
    ]