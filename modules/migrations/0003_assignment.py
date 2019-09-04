# Generated by Django 2.2.2 on 2019-08-19 07:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modules', '0002_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='assignments/')),
                ('submitted_on', models.DateTimeField(default=datetime.datetime.now)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.Section')),
                ('student', models.ForeignKey(limit_choices_to={'role': '3'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]