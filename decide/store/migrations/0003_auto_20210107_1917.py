# Generated by Django 2.0 on 2021-01-07 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_vote_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='a',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='b',
        ),
    ]