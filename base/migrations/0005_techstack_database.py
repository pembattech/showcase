# Generated by Django 5.0 on 2023-12-10 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_techstack_tech_stack_techstack_framework_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='techstack',
            name='database',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
