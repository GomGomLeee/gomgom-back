# Generated by Django 4.2.2 on 2023-07-06 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_comment_image_alter_selection_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='heart_count',
            field=models.IntegerField(blank=True, default=0, verbose_name='공감수'),
        ),
        migrations.AlterField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(blank=True, default=0, verbose_name='조회수'),
        ),
    ]