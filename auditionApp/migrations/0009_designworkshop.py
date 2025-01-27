# Generated by Django 4.0.1 on 2024-02-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditionApp', '0008_remove_auditionportal_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignWorkshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('roll_no', models.CharField(max_length=50, null=True)),
                ('contact_number', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('department', models.CharField(max_length=200, null=True)),
                ('year', models.CharField(max_length=200, null=True)),
                ('payment_proof', models.ImageField(blank=True, null=True, upload_to='payment_images/')),
            ],
        ),
    ]
