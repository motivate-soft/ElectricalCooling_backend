# Generated by Django 3.1.6 on 2021-02-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210215_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.IntegerField(blank=True, max_length=150),
        ),
    ]