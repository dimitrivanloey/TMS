# Generated by Django 3.0.5 on 2021-03-04 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arkle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(unique=True)),
                ('date_added', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('In Repair', 'In Repair'), ('Not In Service', 'Not In Service'), ('In Service', 'In Service')], default='In Service', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Denman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(unique=True)),
                ('date_added', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('In Repair', 'In Repair'), ('Not In Service', 'Not In Service'), ('In Service', 'In Service')], default='In Service', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Enable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(unique=True)),
                ('date_added', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('In Repair', 'In Repair'), ('Not In Service', 'Not In Service'), ('In Service', 'In Service')], default='In Service', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Frankel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(unique=True)),
                ('date_added', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('In Repair', 'In Repair'), ('Not In Service', 'Not In Service'), ('In Service', 'In Service')], default='In Service', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Kauto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(unique=True)),
                ('date_added', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('In Repair', 'In Repair'), ('Not In Service', 'Not In Service'), ('In Service', 'In Service')], default='In Service', max_length=15)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(unique=True)),
                ('date_added', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('In Repair', 'In Repair'), ('Not In Service', 'Not In Service'), ('In Service', 'In Service')], default='In Service', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Winx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(unique=True)),
                ('date_added', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('In Repair', 'In Repair'), ('Not In Service', 'Not In Service'), ('In Service', 'In Service')], default='In Service', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Other_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('On Course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair')], default='In Service', max_length=41)),
                ('venue', models.CharField(blank=True, choices=[('Hamilton', 'Hamilton Park'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Aintree', 'Aintree'), ('Cheltenham', 'Cheltenham'), ('Thirsk', 'Thirsk'), ('Leicester', 'Leicester'), ('Chester', 'Chester'), ('Perth', 'Perth'), ('Carlisle', 'Carlisle'), ('Warwick', 'Warwick'), ('Redcar', 'Redcar'), ('Salisbury', 'Salisbury'), ('Sandown Park', 'Sandown Park'), ('Dundalk', 'Dundalk'), ('Beverly', 'Beverly'), ('Nottingham', 'Nottingham'), ('Wincanton', 'Wincanton'), ('Exeter', 'Exeter'), ('Epsom Downs', 'Epsom Downs'), ('Haydock', 'Haydock Park'), ('Pontefract', 'Pontefract'), ('Taunton', 'Taunton'), ('Huntingdon', 'Huntingdon'), ('Goodwood', 'Goodwood'), ('Musselburgh', 'Musselburgh'), ('Market Rasen', 'Market Rasen'), ('Ayr', 'Ayr'), ('Kelso', 'Kelso'), ('Newbury', 'Newbury'), ('Ludlow', 'Ludlow'), ('Newmarket', 'Newmarket'), ('Wetherby', 'Wetherby'), ('York', 'York'), ('Cartmel', 'Cartmel'), ('Kempton Park', 'Kempton Park'), ('Catterick Bridge', 'Catterick Bridge')], default='Kempton Park', max_length=18, null=True)),
                ('comments', models.TextField(blank=True)),
                ('other', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit_logs.Other')),
            ],
            options={
                'verbose_name_plural': 'other entries',
            },
        ),
        migrations.CreateModel(
            name='Kauto_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('On Course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair')], default='In Service', max_length=41)),
                ('venue', models.CharField(blank=True, choices=[('Hamilton', 'Hamilton Park'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Aintree', 'Aintree'), ('Cheltenham', 'Cheltenham'), ('Thirsk', 'Thirsk'), ('Leicester', 'Leicester'), ('Chester', 'Chester'), ('Perth', 'Perth'), ('Carlisle', 'Carlisle'), ('Warwick', 'Warwick'), ('Redcar', 'Redcar'), ('Salisbury', 'Salisbury'), ('Sandown Park', 'Sandown Park'), ('Dundalk', 'Dundalk'), ('Beverly', 'Beverly'), ('Nottingham', 'Nottingham'), ('Wincanton', 'Wincanton'), ('Exeter', 'Exeter'), ('Epsom Downs', 'Epsom Downs'), ('Haydock', 'Haydock Park'), ('Pontefract', 'Pontefract'), ('Taunton', 'Taunton'), ('Huntingdon', 'Huntingdon'), ('Goodwood', 'Goodwood'), ('Musselburgh', 'Musselburgh'), ('Market Rasen', 'Market Rasen'), ('Ayr', 'Ayr'), ('Kelso', 'Kelso'), ('Newbury', 'Newbury'), ('Ludlow', 'Ludlow'), ('Newmarket', 'Newmarket'), ('Wetherby', 'Wetherby'), ('York', 'York'), ('Cartmel', 'Cartmel'), ('Kempton Park', 'Kempton Park'), ('Catterick Bridge', 'Catterick Bridge')], default='Kempton Park', max_length=18, null=True)),
                ('comments', models.TextField(blank=True)),
                ('kauto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit_logs.Kauto')),
            ],
            options={
                'verbose_name_plural': 'kauto entries',
            },
        ),
        migrations.CreateModel(
            name='Frankel_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('On Course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair')], default='In Service', max_length=41)),
                ('venue', models.CharField(blank=True, choices=[('Hamilton', 'Hamilton Park'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Aintree', 'Aintree'), ('Cheltenham', 'Cheltenham'), ('Thirsk', 'Thirsk'), ('Leicester', 'Leicester'), ('Chester', 'Chester'), ('Perth', 'Perth'), ('Carlisle', 'Carlisle'), ('Warwick', 'Warwick'), ('Redcar', 'Redcar'), ('Salisbury', 'Salisbury'), ('Sandown Park', 'Sandown Park'), ('Dundalk', 'Dundalk'), ('Beverly', 'Beverly'), ('Nottingham', 'Nottingham'), ('Wincanton', 'Wincanton'), ('Exeter', 'Exeter'), ('Epsom Downs', 'Epsom Downs'), ('Haydock', 'Haydock Park'), ('Pontefract', 'Pontefract'), ('Taunton', 'Taunton'), ('Huntingdon', 'Huntingdon'), ('Goodwood', 'Goodwood'), ('Musselburgh', 'Musselburgh'), ('Market Rasen', 'Market Rasen'), ('Ayr', 'Ayr'), ('Kelso', 'Kelso'), ('Newbury', 'Newbury'), ('Ludlow', 'Ludlow'), ('Newmarket', 'Newmarket'), ('Wetherby', 'Wetherby'), ('York', 'York'), ('Cartmel', 'Cartmel'), ('Kempton Park', 'Kempton Park'), ('Catterick Bridge', 'Catterick Bridge')], default='Kempton Park', max_length=18, null=True)),
                ('comments', models.TextField(blank=True)),
                ('frankel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit_logs.Frankel')),
            ],
            options={
                'verbose_name_plural': 'frankel entries',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, choices=[('On Course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair')], max_length=41, null=True)),
                ('venue', models.CharField(blank=True, choices=[('Hamilton', 'Hamilton Park'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Aintree', 'Aintree'), ('Cheltenham', 'Cheltenham'), ('Thirsk', 'Thirsk'), ('Leicester', 'Leicester'), ('Chester', 'Chester'), ('Perth', 'Perth'), ('Carlisle', 'Carlisle'), ('Warwick', 'Warwick'), ('Redcar', 'Redcar'), ('Salisbury', 'Salisbury'), ('Sandown Park', 'Sandown Park'), ('Dundalk', 'Dundalk'), ('Beverly', 'Beverly'), ('Nottingham', 'Nottingham'), ('Wincanton', 'Wincanton'), ('Exeter', 'Exeter'), ('Epsom Downs', 'Epsom Downs'), ('Haydock', 'Haydock Park'), ('Pontefract', 'Pontefract'), ('Taunton', 'Taunton'), ('Huntingdon', 'Huntingdon'), ('Goodwood', 'Goodwood'), ('Musselburgh', 'Musselburgh'), ('Market Rasen', 'Market Rasen'), ('Ayr', 'Ayr'), ('Kelso', 'Kelso'), ('Newbury', 'Newbury'), ('Ludlow', 'Ludlow'), ('Newmarket', 'Newmarket'), ('Wetherby', 'Wetherby'), ('York', 'York'), ('Cartmel', 'Cartmel'), ('Kempton Park', 'Kempton Park'), ('Catterick Bridge', 'Catterick Bridge')], max_length=18, null=True)),
                ('comments', models.TextField(blank=True)),
                ('winx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit_logs.Winx')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.CreateModel(
            name='Enable_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('On Course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair')], default='In Service', max_length=41)),
                ('venue', models.CharField(blank=True, choices=[('Hamilton', 'Hamilton Park'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Aintree', 'Aintree'), ('Cheltenham', 'Cheltenham'), ('Thirsk', 'Thirsk'), ('Leicester', 'Leicester'), ('Chester', 'Chester'), ('Perth', 'Perth'), ('Carlisle', 'Carlisle'), ('Warwick', 'Warwick'), ('Redcar', 'Redcar'), ('Salisbury', 'Salisbury'), ('Sandown Park', 'Sandown Park'), ('Dundalk', 'Dundalk'), ('Beverly', 'Beverly'), ('Nottingham', 'Nottingham'), ('Wincanton', 'Wincanton'), ('Exeter', 'Exeter'), ('Epsom Downs', 'Epsom Downs'), ('Haydock', 'Haydock Park'), ('Pontefract', 'Pontefract'), ('Taunton', 'Taunton'), ('Huntingdon', 'Huntingdon'), ('Goodwood', 'Goodwood'), ('Musselburgh', 'Musselburgh'), ('Market Rasen', 'Market Rasen'), ('Ayr', 'Ayr'), ('Kelso', 'Kelso'), ('Newbury', 'Newbury'), ('Ludlow', 'Ludlow'), ('Newmarket', 'Newmarket'), ('Wetherby', 'Wetherby'), ('York', 'York'), ('Cartmel', 'Cartmel'), ('Kempton Park', 'Kempton Park'), ('Catterick Bridge', 'Catterick Bridge')], default='Kempton Park', max_length=18, null=True)),
                ('comments', models.TextField(blank=True)),
                ('enable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit_logs.Enable')),
            ],
            options={
                'verbose_name_plural': 'enable entries',
            },
        ),
        migrations.CreateModel(
            name='Denman_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('On Course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair')], default='In Service', max_length=41)),
                ('venue', models.CharField(blank=True, choices=[('Hamilton', 'Hamilton Park'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Aintree', 'Aintree'), ('Cheltenham', 'Cheltenham'), ('Thirsk', 'Thirsk'), ('Leicester', 'Leicester'), ('Chester', 'Chester'), ('Perth', 'Perth'), ('Carlisle', 'Carlisle'), ('Warwick', 'Warwick'), ('Redcar', 'Redcar'), ('Salisbury', 'Salisbury'), ('Sandown Park', 'Sandown Park'), ('Dundalk', 'Dundalk'), ('Beverly', 'Beverly'), ('Nottingham', 'Nottingham'), ('Wincanton', 'Wincanton'), ('Exeter', 'Exeter'), ('Epsom Downs', 'Epsom Downs'), ('Haydock', 'Haydock Park'), ('Pontefract', 'Pontefract'), ('Taunton', 'Taunton'), ('Huntingdon', 'Huntingdon'), ('Goodwood', 'Goodwood'), ('Musselburgh', 'Musselburgh'), ('Market Rasen', 'Market Rasen'), ('Ayr', 'Ayr'), ('Kelso', 'Kelso'), ('Newbury', 'Newbury'), ('Ludlow', 'Ludlow'), ('Newmarket', 'Newmarket'), ('Wetherby', 'Wetherby'), ('York', 'York'), ('Cartmel', 'Cartmel'), ('Kempton Park', 'Kempton Park'), ('Catterick Bridge', 'Catterick Bridge')], default='Kempton Park', max_length=18, null=True)),
                ('comments', models.TextField(blank=True)),
                ('denman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit_logs.Denman')),
            ],
            options={
                'verbose_name_plural': 'denman entries',
            },
        ),
        migrations.CreateModel(
            name='Arkle_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('On Course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair')], default='In Service', max_length=41)),
                ('venue', models.CharField(blank=True, choices=[('Hamilton', 'Hamilton Park'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Aintree', 'Aintree'), ('Cheltenham', 'Cheltenham'), ('Thirsk', 'Thirsk'), ('Leicester', 'Leicester'), ('Chester', 'Chester'), ('Perth', 'Perth'), ('Carlisle', 'Carlisle'), ('Warwick', 'Warwick'), ('Redcar', 'Redcar'), ('Salisbury', 'Salisbury'), ('Sandown Park', 'Sandown Park'), ('Dundalk', 'Dundalk'), ('Beverly', 'Beverly'), ('Nottingham', 'Nottingham'), ('Wincanton', 'Wincanton'), ('Exeter', 'Exeter'), ('Epsom Downs', 'Epsom Downs'), ('Haydock', 'Haydock Park'), ('Pontefract', 'Pontefract'), ('Taunton', 'Taunton'), ('Huntingdon', 'Huntingdon'), ('Goodwood', 'Goodwood'), ('Musselburgh', 'Musselburgh'), ('Market Rasen', 'Market Rasen'), ('Ayr', 'Ayr'), ('Kelso', 'Kelso'), ('Newbury', 'Newbury'), ('Ludlow', 'Ludlow'), ('Newmarket', 'Newmarket'), ('Wetherby', 'Wetherby'), ('York', 'York'), ('Cartmel', 'Cartmel'), ('Kempton Park', 'Kempton Park'), ('Catterick Bridge', 'Catterick Bridge')], default='Kempton Park', max_length=18, null=True)),
                ('comments', models.TextField(blank=True)),
                ('arkle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit_logs.Arkle')),
            ],
            options={
                'verbose_name_plural': 'arkle entries',
            },
        ),
    ]
