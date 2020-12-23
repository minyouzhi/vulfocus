# Generated by Django 2.2.10 on 2020-12-17 19:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('layout_image', '0005_auto_20201217_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layout',
            name='layout_id',
            field=models.UUIDField(default=uuid.UUID('5ffabb95-6a0e-4f88-a98c-625e0d730e2e'), editable=False, primary_key=True, serialize=False, verbose_name='编排UUID'),
        ),
        migrations.AlterField(
            model_name='layoutdata',
            name='layout_user_id',
            field=models.UUIDField(default=uuid.UUID('9234521a-9e3f-478d-8119-94690c318ca7'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservice',
            name='service_id',
            field=models.UUIDField(default=uuid.UUID('33ecb5ec-ddbd-474b-a6ca-2e8b587aa92b'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservicecontainer',
            name='service_container_id',
            field=models.UUIDField(default=uuid.UUID('89d3791c-ef1a-4f65-bdd3-24093c53274e'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservicenetwork',
            name='layout_service_network_id',
            field=models.UUIDField(default=uuid.UUID('64338057-0b26-4500-a290-74389511a422'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='LayoutServiceContainerScore',
            fields=[
                ('layout_service_container_score_id', models.UUIDField(default=uuid.UUID('af22864c-5eca-466b-a94d-70698fc111b4'), editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='用户ID')),
                ('flag', models.CharField(max_length=255, verbose_name='flag')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间，默认为当前时间')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('layout_data_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layout_image.LayoutData', verbose_name='编排 ID')),
                ('layout_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layout_image.Layout', verbose_name='编排 ID')),
                ('service_container_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='layout_image.LayoutServiceContainer', verbose_name='编排 ID')),
            ],
            options={
                'db_table': 'layout_service_container_score',
            },
        ),
    ]