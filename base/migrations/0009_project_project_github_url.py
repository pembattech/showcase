# Generated by Django 5.0 on 2023-12-14 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_userprofile_github_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_github_url',
            field=models.URLField(max_length=255, null=True),
        ),
    ]
