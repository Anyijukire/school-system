# Generated by Django 3.2.5 on 2021-08-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20210730_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='big_sister',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='class_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='first_name',
            field=models.CharField(help_text='eg Jane', max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='last_name',
            field=models.CharField(help_text='eg Doe', max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='mentor',
            field=models.CharField(blank=True, max_length=29, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='room_number',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]