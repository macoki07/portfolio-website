# Generated by Django 4.2.1 on 2023-07-03 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_section_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.TextField(),
        ),
    ]
