# Generated by Django 4.2.7 on 2024-02-25 05:56

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0015_remove_topic_duration_topic_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='text',
            field=froala_editor.fields.FroalaField(default=0),
            preserve_default=False,
        ),
    ]
