# Generated by Django 4.2.7 on 2023-11-28 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_remove_new_filed_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='field_name',
            field=models.ImageField(upload_to='images'),
        ),
    ]