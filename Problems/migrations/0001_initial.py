# Generated by Django 3.1.7 on 2021-03-27 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Contestant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_id', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=15)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('code', models.FileField(upload_to='Documents/Solution')),
                ('solver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contestant.contestant')),
            ],
        ),
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('input', models.FileField(upload_to='Documents/TestCase/Input')),
                ('output', models.FileField(upload_to='Documents/TestCase/Output')),
                ('problem_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('problem_name', models.CharField(max_length=30)),
                ('Problem_text', models.FileField(upload_to='Documents/Problem')),
                ('category', models.CharField(max_length=20)),
                ('level', models.CharField(max_length=10)),
                ('solver', models.ForeignKey(default='Did not solve', on_delete=django.db.models.deletion.SET_DEFAULT, to='Contestant.contestant')),
            ],
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=10)),
                ('message', models.TextField()),
                ('dicussant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contestant.contestant')),
                ('problem_id', models.ForeignKey(default='Problem Removed', on_delete=django.db.models.deletion.SET_DEFAULT, to='Problems.problems')),
            ],
        ),
    ]