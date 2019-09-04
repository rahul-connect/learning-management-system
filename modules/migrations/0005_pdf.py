# Generated by Django 2.2.2 on 2019-08-21 07:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0004_auto_20190819_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('created_on', models.DateTimeField(default=datetime.datetime.now)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.Section')),
            ],
        ),
    ]