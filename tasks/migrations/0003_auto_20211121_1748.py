# Generated by Django 3.2.8 on 2021-11-21 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('tasks', '0002_auto_20211121_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.category'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('to do', 'To Do'), ('in progress', 'In Progress'), ('finished', 'Finished')], default='to do', max_length=15),
        ),
    ]
