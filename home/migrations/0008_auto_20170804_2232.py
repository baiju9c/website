# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0039_collectionviewrestriction'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('home', '0007_auto_20170804_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='RichTextOnly',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='outreachyhomepage',
            name='page_ptr',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(default='<p>Outreachy provides three-month, paid, remote internships for people traditionally underrepresented in tech. Individual donors and corporate sponsors provide funding for the program, and interns are often hired by our sponsors! Interns work directly with mentors from Free and Open Source (FOSS) communities on projects ranging from programming, user experience, documentation, illustration and graphical design, and data science.</p><p>Outreachy internships are open internationally to women (cis and trans), trans men, and genderqueer people. Internships are also open to residents and nationals of the United States of any gender who are Black/African American, Hispanic/Latin@, American Indian, Alaska Native, Native Hawaiian, or Pacific Islander. We are planning to expand the program to more participants from underrepresented backgrounds in the future.</p><p>Outreachy internships run twice a year.</p>'),
        ),
        migrations.DeleteModel(
            name='OutreachyHomePage',
        ),
    ]
