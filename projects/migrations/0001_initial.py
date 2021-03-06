# Generated by Django 4.0.3 on 2022-03-19 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colors', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['countries'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='avatars/')),
                ('description', tinymce.models.HTMLField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.countries')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('landing_page', models.ImageField(upload_to='landingpage/')),
                ('description', tinymce.models.HTMLField()),
                ('link', models.CharField(max_length=255)),
                ('screenshot1', models.ImageField(upload_to='screenshots/')),
                ('screenshot2', models.ImageField(upload_to='screenshots/')),
                ('screenshot3', models.ImageField(upload_to='screenshots/')),
                ('screenshot4', models.ImageField(upload_to='screenshots/')),
                ('design', models.IntegerField(blank=True, default=0)),
                ('usability', models.IntegerField(blank=True, default=0)),
                ('creativity', models.IntegerField(blank=True, default=0)),
                ('content', models.IntegerField(blank=True, default=0)),
                ('overall_score', models.IntegerField(blank=True, default=0)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.ImageField(upload_to='avatars/')),
                ('categories', models.ManyToManyField(to='projects.categories')),
                ('colors', models.ManyToManyField(to='projects.colors')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.countries')),
            ],
        ),
        migrations.CreateModel(
            name='technologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technologies', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.IntegerField(blank=True, default=0)),
                ('usability', models.IntegerField(blank=True, default=0)),
                ('creativity', models.IntegerField(blank=True, default=0)),
                ('content', models.IntegerField(blank=True, default=0)),
                ('overall_score', models.IntegerField(blank=True, default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.profile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='projects.technologies'),
        ),
        migrations.AddField(
            model_name='project',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
