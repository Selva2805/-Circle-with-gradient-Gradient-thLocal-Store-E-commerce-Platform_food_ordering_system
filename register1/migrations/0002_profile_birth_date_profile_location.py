# Generated by Django 5.0.6 on 2024-06-20 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]