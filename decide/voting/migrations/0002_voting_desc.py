# Generated by Django 2.0 on 2020-12-31 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]