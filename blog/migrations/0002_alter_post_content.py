# Generated by Django 4.1.4 on 2023-02-01 15:45

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
