# Generated by Django 5.0.6 on 2024-07-18 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('c_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('c_name', models.CharField(default='', max_length=50)),
                ('enrollment', models.ManyToManyField(blank='True', to='exp7.student')),
            ],
        ),
    ]
