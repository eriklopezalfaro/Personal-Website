# Generated by Django 3.2.7 on 2022-01-26 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_service_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.CharField(default='Python', max_length=250),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=400),
        ),
    ]
