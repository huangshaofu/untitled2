# Generated by Django 2.0.4 on 2018-05-02 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'User2',
            },
        ),
    ]
