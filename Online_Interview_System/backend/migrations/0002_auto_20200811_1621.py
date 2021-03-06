# Generated by Django 3.1 on 2020-08-11 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interviewee',
            fields=[
                ('name', models.CharField(max_length=128)),
                ('mobile', models.CharField(default='11111111111', max_length=20)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('accept', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'interviewee_message',
                'verbose_name_plural': 'interviewee_message',
            },
        ),
        migrations.RemoveField(
            model_name='hr',
            name='identity',
        ),
        migrations.RemoveField(
            model_name='interviewer',
            name='identity',
        ),
        migrations.RemoveField(
            model_name='room',
            name='accept',
        ),
        migrations.RemoveField(
            model_name='room',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='room',
            name='id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='record',
        ),
        migrations.RemoveField(
            model_name='super',
            name='identity',
        ),
        migrations.AddField(
            model_name='room',
            name='remark',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='interviewer',
            name='free1',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='interviewer',
            name='free2',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='interviewer',
            name='free3',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='finaleval',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='roomid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='tempeval',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='interviewee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.interviewee'),
        ),
    ]
