# Generated by Django 3.0.5 on 2020-11-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qing', '0002_defore_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mistakes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mistakes', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Mistakes',
                'managed': True,
            },
        ),
    ]
