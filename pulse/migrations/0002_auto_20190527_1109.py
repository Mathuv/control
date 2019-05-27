# Generated by Django 2.2.1 on 2019-05-27 11:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pulse', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pulse',
            options={'verbose_name': 'pulse', 'verbose_name_plural': 'pulses'},
        ),
        migrations.AddField(
            model_name='pulse',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pulse',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
