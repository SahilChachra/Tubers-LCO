# Generated by Django 3.1.4 on 2020-12-22 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0005_baseapp'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseAppModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('fb_link', models.CharField(default='https://facebook.com/', max_length=255)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='BaseApp',
        ),
    ]
