# Generated by Django 4.2.7 on 2024-02-25 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0013_alter_content_options_alter_topic_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='topics',
        ),
    ]
