# Generated by Django 3.0.4 on 2020-03-12 03:58

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('home', '0004_homepage_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorksPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(choices=[('dt', 'Downloadable Templates'), ('il', 'Illustrations'), ('cp', 'Client Projects')], default='DOWNLOADABLE', max_length=2)),
                ('date', models.DateField(verbose_name='Post date')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='category',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='date',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='description',
        ),
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]