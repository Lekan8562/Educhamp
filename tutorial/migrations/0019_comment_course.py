# Generated by Django 4.1.7 on 2024-02-28 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0018_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_comments', to='tutorial.course'),
        ),
    ]
