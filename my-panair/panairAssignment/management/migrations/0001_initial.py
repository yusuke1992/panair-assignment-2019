# Generated by Django 2.2 on 2019-05-06 13:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='カリキュラム名')),
                ('basic_charge', models.IntegerField(verbose_name='基本料金')),
                ('metered_charge', models.IntegerField(verbose_name='従量料金')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('age', models.IntegerField(verbose_name='年齢')),
                ('gender', models.IntegerField(choices=[(1, '男性'), (2, '女性')], default=1, verbose_name='性別')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='受講日')),
                ('time', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='受講時間')),
                ('charge', models.IntegerField(default=0, verbose_name='支払い金額')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Curriculum', verbose_name='カリキュラム')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.User', verbose_name='ユーザー')),
            ],
        ),
    ]
