# Generated by Django 4.2 on 2023-09-02 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0008_delete_isiresult"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="result",
            name="result",
        ),
        migrations.AddField(
            model_name="result",
            name="result",
            field=models.ManyToManyField(related_name="results", to="projects.proyek"),
        ),
    ]
