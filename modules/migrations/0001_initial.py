# Generated by Django 2.2.2 on 2019-08-09 10:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enquiry', '0003_auto_20190809_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(default=datetime.datetime.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquiry.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(default=datetime.datetime.now)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.Module')),
            ],
        ),
    ]
