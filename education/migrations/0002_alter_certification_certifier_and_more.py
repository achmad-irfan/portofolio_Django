# Generated by Django 4.2 on 2023-08-12 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("education", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certification",
            name="certifier",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="certification",
            name="major",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="certification",
            name="year",
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name="school",
            name="college",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="school",
            name="major",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="school",
            name="year",
            field=models.CharField(max_length=15),
        ),
    ]
