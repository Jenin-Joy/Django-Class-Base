# Generated by Django 5.1.4 on 2024-12-18 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0005_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(help_text='Enter Shop Name', max_length=30)),
                ('shop_contact', models.CharField(help_text='Enter Shop Contact', max_length=30)),
                ('shop_email', models.EmailField(help_text='Enter Shop Email', max_length=30)),
                ('shop_address', models.TextField(help_text='Enter Shop Address', max_length=50)),
                ('shop_logo', models.FileField(upload_to='Assets/Shop/Logo/')),
                ('shop_proof', models.FileField(upload_to='Assets/Shop/Proof')),
                ('shop_password', models.CharField(help_text='Enter your password', max_length=30)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.place')),
            ],
        ),
    ]
