# Generated by Django 4.2 on 2023-09-02 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0009_remove_result_result_result_result"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="result",
            name="result",
        ),
        migrations.AddField(
            model_name="result",
            name="isi",
            field=models.TextField(default="a"),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name="result",
            name="namaProject",
        ),
        migrations.AddField(
            model_name="result",
            name="namaProject",
            field=models.ManyToManyField(related_name="results", to="projects.proyek"),
        ),
    ]
