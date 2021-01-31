# Generated by Django 3.1.5 on 2021-01-29 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_auto_20210121_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abusereports',
            old_name='text',
            new_name='title',
        ),
        migrations.AddField(
            model_name='abusereports',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='abusereports',
            name='status',
            field=models.TextField(default='open'),
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dialog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.abusereports')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
