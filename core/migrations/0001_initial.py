# Generated by Django 4.2.7 on 2023-12-05 16:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceProcess',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField()),
            ],
            options={
                'db_table': 'balance_process',
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=250)),
                ('moment_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('moment_update', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'general_locations',
            },
        ),
        migrations.CreateModel(
            name='Substances',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('moment_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('moment_update', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'general_substances',
            },
        ),
        migrations.CreateModel(
            name='ZoneIndex',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lat_l', models.FloatField()),
                ('lat_g', models.FloatField()),
                ('lon_l', models.FloatField()),
                ('lon_g', models.FloatField()),
            ],
            options={
                'db_table': 'vehicles_zone_index',
            },
        ),
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('P', 'Port')], max_length=1)),
            ],
            options={
                'db_table': 'vehicles_zones',
            },
        ),
        migrations.CreateModel(
            name='ZonePoints',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.zones')),
            ],
            options={
                'db_table': 'vehicles_zone_points',
            },
        ),
        migrations.CreateModel(
            name='ZoneIndexZones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.zones')),
                ('zone_index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.zoneindex')),
            ],
            options={
                'db_table': 'vehicles_zone_index_zones',
            },
        ),
        migrations.CreateModel(
            name='ModelShips',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('id_mt', models.IntegerField()),
                ('name', models.CharField(max_length=250)),
                ('type', models.IntegerField()),
                ('flag', models.CharField(max_length=2)),
                ('lat', models.FloatField(null=True)),
                ('lon', models.FloatField(null=True)),
                ('course', models.IntegerField(null=True)),
                ('heading', models.IntegerField(null=True)),
                ('speed', models.IntegerField(null=True)),
                ('moment', models.DateTimeField(null=True)),
                ('moment_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('moment_update', models.DateTimeField(auto_now=True, null=True)),
                ('zone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.zones')),
            ],
            options={
                'db_table': 'vehicles_ships',
            },
        ),
        migrations.CreateModel(
            name='ModelShipLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('moment', models.DateTimeField()),
                ('type_location', models.IntegerField()),
                ('lat', models.FloatField(null=True)),
                ('lon', models.FloatField(null=True)),
                ('course', models.IntegerField(null=True)),
                ('heading', models.IntegerField(null=True)),
                ('speed', models.IntegerField(null=True)),
                ('ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modelships')),
                ('zone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.zones')),
            ],
            options={
                'db_table': 'vehicles_ships_locations',
            },
        ),
        migrations.CreateModel(
            name='BalanceSubstancesTotal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('moment', models.DateField(null=True)),
                ('initial_total', models.BigIntegerField()),
                ('final_total', models.BigIntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.locations')),
                ('substance', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.substances')),
            ],
            options={
                'db_table': 'balance_substances_total',
            },
        ),
        migrations.CreateModel(
            name='BalanceSubstancesRelationsTo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.BigIntegerField()),
                ('value_from', models.BigIntegerField()),
                ('process_from', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='process_to', to='core.balanceprocess')),
                ('substance_from', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='substance_from', to='core.substances')),
                ('total', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='total_from', to='core.balancesubstancestotal')),
            ],
            options={
                'db_table': 'balance_substances_relations_to',
            },
        ),
        migrations.CreateModel(
            name='BalanceSubstancesRelationsFrom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.BigIntegerField()),
                ('value_from', models.BigIntegerField()),
                ('process_from', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='process_from', to='core.balanceprocess')),
                ('substance_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='substance_to', to='core.substances')),
                ('total_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='total_to', to='core.balancesubstancestotal')),
            ],
            options={
                'db_table': 'balance_substances_relations_from',
            },
        ),
    ]
