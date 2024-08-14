# Generated by Django 5.0.7 on 2024-08-06 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('english_certificate', models.BooleanField(default=False)),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
    ]
