# Generated by Django 3.0.4 on 2020-04-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200318_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cimg',
            field=models.ImageField(default='p.jpg', upload_to='login/images/'),
        ),
    ]
