# Generated by Django 3.2.7 on 2022-04-02 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20220126_0413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='url',
            new_name='github_repo_url',
        ),
        migrations.AddField(
            model_name='project',
            name='website_url',
            field=models.URLField(blank=True),
        ),
    ]
