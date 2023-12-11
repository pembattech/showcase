# Generated by Django 5.0 on 2023-12-10 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_techstack_tech_stack'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techstack',
            name='tech_stack',
        ),
        migrations.AddField(
            model_name='techstack',
            name='framework',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='techstack',
            name='language',
            field=models.CharField(max_length=255, null=True),
        ),
    ]