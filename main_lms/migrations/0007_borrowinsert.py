# Generated by Django 2.2 on 2019-05-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_lms', '0006_studept_stusession'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowInsert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brsid', models.CharField(max_length=100)),
                ('brsname', models.CharField(max_length=500)),
                ('brbname', models.CharField(max_length=500)),
                ('brdate', models.DateField(auto_now_add=True)),
                ('brreturn', models.DateField()),
            ],
            options={
                'db_table': 'borrowinsert',
            },
        ),
    ]
