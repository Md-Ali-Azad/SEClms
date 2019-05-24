# Generated by Django 2.2 on 2019-05-22 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_lms', '0004_headercolor'),
    ]

    operations = [
        migrations.CreateModel(
            name='StuInsert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=100)),
                ('sname', models.CharField(max_length=500)),
                ('sdept', models.CharField(max_length=200)),
                ('ssession', models.CharField(max_length=400)),
                ('saddress', models.CharField(max_length=400)),
                ('scontact', models.CharField(max_length=400)),
                ('semail', models.EmailField(max_length=400)),
                ('sgender', models.CharField(max_length=50)),
                ('screated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'stuinsert',
            },
        ),
    ]
