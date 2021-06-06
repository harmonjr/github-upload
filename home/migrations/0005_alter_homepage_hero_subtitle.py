# Generated by Django 3.2.3 on 2021-06-01 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_hero_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='hero_subtitle',
            field=models.CharField(blank=True, help_text='Subtitle text displayed in the hero section over the background.', max_length=150),
        ),
    ]
