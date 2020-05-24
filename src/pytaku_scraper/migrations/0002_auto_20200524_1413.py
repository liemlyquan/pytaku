# Generated by Django 3.0.5 on 2020-05-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pytaku_scraper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=1024)),
                ('method', models.CharField(default='get', max_length=7)),
                ('resp_body', models.TextField()),
                ('resp_status', models.IntegerField()),
            ],
            options={
                'db_table': 'download_result',
            },
        ),
        migrations.DeleteModel(
            name='ScrapeAttempt',
        ),
        migrations.AddConstraint(
            model_name='downloadresult',
            constraint=models.UniqueConstraint(fields=('url', 'method'), name='unique_url_method'),
        ),
    ]