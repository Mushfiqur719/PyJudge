# Generated by Django 3.1.7 on 2021-05-05 15:21

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('institution', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(default='default-profile.png', null=True, upload_to='Profile_Pictures')),
                ('user_type', models.CharField(choices=[('Contestant', 'Contestant'), ('Judge', 'Judge')], max_length=20, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
