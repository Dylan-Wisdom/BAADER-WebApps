# Generated by Django 4.2.2 on 2023-06-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AutoPlot', '0002_delete_autoplot'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoPlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runtime', models.DateField()),
                ('action', models.CharField(max_length=255)),
            ],
        ),
    ]
