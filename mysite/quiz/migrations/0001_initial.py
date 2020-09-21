# Generated by Django 2.2 on 2020-09-19 12:32

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
            name='Contests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('rules', models.CharField(max_length=1000)),
                ('question_count', models.IntegerField(default=0)),
                ('c_type', models.IntegerField(default=2)),
                ('penalty', models.FloatField(default=0)),
                ('end_time', models.DateTimeField(null=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('d_day', models.CharField(max_length=2, null=True)),
                ('d_hour', models.CharField(max_length=2, null=True)),
                ('d_minute', models.CharField(max_length=2, null=True)),
                ('total_score', models.FloatField(default=0)),
                ('contestants', models.IntegerField(null=True)),
                ('prizes', models.CharField(max_length=1000, null=True)),
                ('contest_admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Contests')),
                ('captain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='captain', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.IntegerField(default=0)),
                ('finished', models.BooleanField(default=False)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Contests')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Team')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=1000, null=True)),
                ('problem_type', models.BooleanField(default=True)),
                ('options1', models.CharField(max_length=1000, null=True)),
                ('options2', models.CharField(max_length=1000, null=True)),
                ('options3', models.CharField(max_length=1000, null=True)),
                ('options4', models.CharField(max_length=1000, null=True)),
                ('options5', models.CharField(max_length=1000, null=True)),
                ('problem_statement', models.CharField(max_length=2000)),
                ('announcement', models.CharField(max_length=2000)),
                ('score', models.FloatField(default=0)),
                ('option', models.CharField(max_length=1000, null=True)),
                ('negative', models.FloatField(null=True)),
                ('contest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Contests')),
            ],
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempts', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('C', 'Correct'), ('W', 'Wrong')], max_length=10)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Contests')),
                ('q_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Questions')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]