# Generated by Django 3.2.7 on 2022-01-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_skill_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=35),
        ),
    ]