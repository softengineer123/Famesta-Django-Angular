# Generated by Django 3.0.4 on 2020-04-26 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=post.models.upload_user_post_path, verbose_name='file')),
                ('post_info', models.CharField(blank=True, max_length=300, null=True, verbose_name='post_info')),
                ('post_time_stamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='post_time_stamp')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
