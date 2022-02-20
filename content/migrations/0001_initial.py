# Generated by Django 2.2.27 on 2022-02-20 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content_order', models.PositiveSmallIntegerField(choices=[(1, 'By order'), (2, 'Mix')], default=1)),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('counter', models.PositiveIntegerField(default=0)),
                ('order', models.PositiveIntegerField(default=0)),
                ('video_url', models.URLField()),
                ('subtitle_file_url', models.URLField()),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='content.Page')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('counter', models.PositiveIntegerField(default=0)),
                ('order', models.PositiveIntegerField(default=0)),
                ('text', models.TextField()),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texts', to='content.Page')),
            ],
            options={
                'verbose_name': 'Text',
                'verbose_name_plural': 'Texts',
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('counter', models.PositiveIntegerField(default=0)),
                ('order', models.PositiveIntegerField(default=0)),
                ('bitrate', models.PositiveIntegerField(verbose_name='Bitrate (bit/s)')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audios', to='content.Page')),
            ],
            options={
                'verbose_name': 'Audio',
                'verbose_name_plural': 'Audios',
            },
        ),
    ]
