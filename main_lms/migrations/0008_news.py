# Generated by Django 2.2 on 2019-08-07 11:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_lms', '0007_borrowinsert'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ndetails', ckeditor.fields.RichTextField()),
                ('ncreated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]
