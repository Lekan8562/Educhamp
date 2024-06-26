# Generated by Django 4.2.7 on 2023-12-12 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='course_images/')),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ManyToManyField(related_name='courses', to='tutorial.category')),
            ],
            options={
                'verbose_name': 'Course',
                'ordering': ['-new_price'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('other_names', models.CharField(max_length=150)),
                ('avatar', models.ImageField(null=True, upload_to='avatar/images/')),
                ('courses', models.ManyToManyField(related_name='students', to='tutorial.course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('founded', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='teachers_image/')),
                ('courses', models.ManyToManyField(related_name='tutorials', to='tutorial.course')),
            ],
            options={
                'verbose_name': 'Tutorial',
                'ordering': ['-founded'],
                'get_latest_by': 'name',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('others', models.CharField(max_length=150)),
                ('categories', models.ManyToManyField(related_name='category_teachers', to='tutorial.category')),
                ('students', models.ManyToManyField(related_name='teachers', to='tutorial.student')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('skill_level', models.CharField(choices=[('BG', 'Beginner'), ('AT', 'Amateur'), ('PF', 'Professional')], default='AT', max_length=10)),
                ('students_no', models.IntegerField(default=1)),
                ('assessment', models.BooleanField(default=False)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time_from', models.TimeField(default=django.utils.timezone.now)),
                ('time_to', models.TimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(null=True, upload_to='event_images/')),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('certification', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.category')),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.tutorial')),
            ],
            options={
                'verbose_name': 'Event',
                'ordering': ['-date'],
                'get_latest_by': 'event_name',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.teacher'),
        ),
    ]
