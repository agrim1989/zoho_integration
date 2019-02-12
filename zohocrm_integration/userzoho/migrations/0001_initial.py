# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-02-02 05:50
from __future__ import unicode_literals

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
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('sequence', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('flag', models.CharField(blank=True, max_length=100, null=True)),
                ('id_string', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': 'Milestone',
                'verbose_name_plural': 'Milestone',
            },
        ),
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portal_id', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': 'Portal',
                'verbose_name_plural': 'Portal',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('owner_name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('task_count_open', models.IntegerField(default=0)),
                ('milestone_count_open', models.IntegerField(default=0)),
                ('task_count_close', models.IntegerField(default=0)),
                ('milestone_count_close', models.IntegerField(default=0)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('created_date_format', models.DateField(blank=True, null=True)),
                ('start_date_format', models.DateField(blank=True, null=True)),
                ('folder_url', models.URLField(blank=True, null=True)),
                ('milestone_url', models.URLField(blank=True, null=True)),
                ('forum_url', models.URLField(blank=True, null=True)),
                ('document_url', models.URLField(blank=True, null=True)),
                ('status_url', models.URLField(blank=True, null=True)),
                ('event_url', models.URLField(blank=True, null=True)),
                ('task_url', models.URLField(blank=True, null=True)),
                ('bug_url', models.URLField(blank=True, null=True)),
                ('self_url', models.URLField(blank=True, null=True)),
                ('timesheet_url', models.URLField(blank=True, null=True)),
                ('user_url', models.URLField(blank=True, null=True)),
                ('tasklist_url', models.URLField(blank=True, null=True)),
                ('activity_url', models.URLField(blank=True, null=True)),
                ('end_date_format', models.DateField(blank=True, null=True)),
                ('id_bug_enabled', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': 'Projects',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milestone_id', models.CharField(max_length=100)),
                ('self_url', models.URLField(blank=True, null=True)),
                ('timesheet_url', models.URLField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('duration', models.CharField(blank=True, max_length=100, null=True)),
                ('task_id', models.CharField(max_length=1000, unique=True)),
                ('task_key', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_person', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_time', models.DateField(blank=True, null=True)),
                ('subtasks', models.CharField(blank=True, max_length=100, null=True)),
                ('work', models.CharField(blank=True, max_length=100, null=True)),
                ('completed', models.CharField(blank=True, max_length=1000, null=True)),
                ('percent_complete', models.CharField(blank=True, max_length=1000, null=True)),
                ('last_updated_time', models.DateField(blank=True, null=True)),
                ('task_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('tasklist_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.CharField(blank=True, max_length=1000, null=True)),
                ('color_code', models.CharField(blank=True, max_length=1000, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userzoho.Projects')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': 'Tasks',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified_date', models.DateField(blank=True, null=True)),
                ('bill_status', models.CharField(blank=True, max_length=100, null=True)),
                ('time_sheet_id', models.CharField(blank=True, max_length=100, null=True)),
                ('owner_name', models.CharField(blank=True, max_length=100, null=True)),
                ('hours', models.CharField(blank=True, max_length=100, null=True)),
                ('total_minutes', models.CharField(blank=True, max_length=100, null=True)),
                ('hours_display', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userzoho.Projects')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userzoho.Tasks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': 'Time Sheet',
                'verbose_name_plural': 'Time Sheet',
            },
        ),
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.TextField(max_length=100)),
                ('code', models.TextField(max_length=100)),
                ('refresh_token', models.TextField(max_length=100)),
                ('created_at', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': 'Tokens',
                'verbose_name_plural': 'Tokens',
            },
        ),
        migrations.CreateModel(
            name='ZohoAllUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': 'All Users',
                'verbose_name_plural': 'All Users',
            },
        ),
        migrations.CreateModel(
            name='ZohoUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=1000)),
                ('username', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('tasks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userzoho.Tasks')),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': 'Zoho Users',
                'verbose_name_plural': 'Zoho Users',
            },
        ),
        migrations.AddField(
            model_name='milestone',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userzoho.Projects'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
