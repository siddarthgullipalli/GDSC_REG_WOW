# Generated by Django 4.0.6 on 2023-03-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=228)),
                ('last_name', models.CharField(max_length=228)),
                ('ph_number', models.IntegerField()),
                ('email', models.CharField(max_length=228)),
                ('college', models.CharField(max_length=228)),
                ('branch', models.CharField(max_length=228)),
                ('member', models.BooleanField(default=False)),
                ('address', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]