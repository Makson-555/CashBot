# Generated by Django 3.1.1 on 2024-02-21 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Start',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Старт')),
            ],
            options={
                'db_table': 'start',
            },
        ),
    ]
