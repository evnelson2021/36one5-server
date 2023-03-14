# Generated by Django 4.1.7 on 2023-03-14 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('hours', models.CharField(max_length=150)),
                ('details', models.CharField(max_length=150)),
                ('coordinates', models.CharField(max_length=150)),
                ('website', models.CharField(max_length=150)),
                ('venue_image', models.CharField(max_length=150)),
                ('admin_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('doors', models.CharField(max_length=150)),
                ('start_time', models.CharField(max_length=150)),
                ('details', models.CharField(max_length=150)),
                ('ticket_link', models.CharField(max_length=150)),
                ('event_image', models.CharField(max_length=150)),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_type', to='backendapi.eventtype')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_venue', to='backendapi.venue')),
            ],
        ),
    ]
