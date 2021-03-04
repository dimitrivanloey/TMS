# Generated by Django 3.0.5 on 2021-03-04 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_logs', '0002_auto_20210304_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='kauto',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='arkle',
            name='status',
            field=models.CharField(choices=[('In Service', 'In Service'), ('In Repair', 'In Repair'), ('Not In Service', 'Not In Service')], default='In Service', max_length=15),
        ),
        migrations.AlterField(
            model_name='arkle_entry',
            name='status',
            field=models.CharField(choices=[('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Racing: Not to course', 'On course - racing: Not to course')], default='In Service', max_length=41),
        ),
        migrations.AlterField(
            model_name='arkle_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Wincanton', 'Wincanton'), ('Huntingdon', 'Huntingdon'), ('Market Rasen', 'Market Rasen'), ('Nottingham', 'Nottingham'), ('Newbury', 'Newbury'), ('Goodwood', 'Goodwood'), ('Carlisle', 'Carlisle'), ('Kelso', 'Kelso'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Redcar', 'Redcar'), ('Hamilton', 'Hamilton Park'), ('Warwick', 'Warwick'), ('Exeter', 'Exeter'), ('Cartmel', 'Cartmel'), ('Wetherby', 'Wetherby'), ('Kempton Park', 'Kempton Park'), ('Ayr', 'Ayr'), ('Ludlow', 'Ludlow'), ('Salisbury', 'Salisbury'), ('Musselburgh', 'Musselburgh'), ('Thirsk', 'Thirsk'), ('Perth', 'Perth'), ('Chester', 'Chester'), ('Epsom Downs', 'Epsom Downs'), ('Taunton', 'Taunton'), ('Aintree', 'Aintree'), ('Catterick Bridge', 'Catterick Bridge'), ('Haydock', 'Haydock Park'), ('Beverly', 'Beverly'), ('Leicester', 'Leicester'), ('Newmarket', 'Newmarket'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('York', 'York'), ('Dundalk', 'Dundalk'), ('Cheltenham', 'Cheltenham')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='denman',
            name='status',
            field=models.CharField(choices=[('In Service', 'In Service'), ('In Repair', 'In Repair'), ('Not In Service', 'Not In Service')], default='In Service', max_length=15),
        ),
        migrations.AlterField(
            model_name='denman_entry',
            name='status',
            field=models.CharField(choices=[('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Racing: Not to course', 'On course - racing: Not to course')], default='In Service', max_length=41),
        ),
        migrations.AlterField(
            model_name='denman_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Wincanton', 'Wincanton'), ('Huntingdon', 'Huntingdon'), ('Market Rasen', 'Market Rasen'), ('Nottingham', 'Nottingham'), ('Newbury', 'Newbury'), ('Goodwood', 'Goodwood'), ('Carlisle', 'Carlisle'), ('Kelso', 'Kelso'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Redcar', 'Redcar'), ('Hamilton', 'Hamilton Park'), ('Warwick', 'Warwick'), ('Exeter', 'Exeter'), ('Cartmel', 'Cartmel'), ('Wetherby', 'Wetherby'), ('Kempton Park', 'Kempton Park'), ('Ayr', 'Ayr'), ('Ludlow', 'Ludlow'), ('Salisbury', 'Salisbury'), ('Musselburgh', 'Musselburgh'), ('Thirsk', 'Thirsk'), ('Perth', 'Perth'), ('Chester', 'Chester'), ('Epsom Downs', 'Epsom Downs'), ('Taunton', 'Taunton'), ('Aintree', 'Aintree'), ('Catterick Bridge', 'Catterick Bridge'), ('Haydock', 'Haydock Park'), ('Beverly', 'Beverly'), ('Leicester', 'Leicester'), ('Newmarket', 'Newmarket'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('York', 'York'), ('Dundalk', 'Dundalk'), ('Cheltenham', 'Cheltenham')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='enable',
            name='status',
            field=models.CharField(choices=[('In Service', 'In Service'), ('In Repair', 'In Repair'), ('Not In Service', 'Not In Service')], default='In Service', max_length=15),
        ),
        migrations.AlterField(
            model_name='enable_entry',
            name='status',
            field=models.CharField(choices=[('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Racing: Not to course', 'On course - racing: Not to course')], default='In Service', max_length=41),
        ),
        migrations.AlterField(
            model_name='enable_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Wincanton', 'Wincanton'), ('Huntingdon', 'Huntingdon'), ('Market Rasen', 'Market Rasen'), ('Nottingham', 'Nottingham'), ('Newbury', 'Newbury'), ('Goodwood', 'Goodwood'), ('Carlisle', 'Carlisle'), ('Kelso', 'Kelso'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Redcar', 'Redcar'), ('Hamilton', 'Hamilton Park'), ('Warwick', 'Warwick'), ('Exeter', 'Exeter'), ('Cartmel', 'Cartmel'), ('Wetherby', 'Wetherby'), ('Kempton Park', 'Kempton Park'), ('Ayr', 'Ayr'), ('Ludlow', 'Ludlow'), ('Salisbury', 'Salisbury'), ('Musselburgh', 'Musselburgh'), ('Thirsk', 'Thirsk'), ('Perth', 'Perth'), ('Chester', 'Chester'), ('Epsom Downs', 'Epsom Downs'), ('Taunton', 'Taunton'), ('Aintree', 'Aintree'), ('Catterick Bridge', 'Catterick Bridge'), ('Haydock', 'Haydock Park'), ('Beverly', 'Beverly'), ('Leicester', 'Leicester'), ('Newmarket', 'Newmarket'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('York', 'York'), ('Dundalk', 'Dundalk'), ('Cheltenham', 'Cheltenham')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.CharField(blank=True, choices=[('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Racing: Not to course', 'On course - racing: Not to course')], max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Wincanton', 'Wincanton'), ('Huntingdon', 'Huntingdon'), ('Market Rasen', 'Market Rasen'), ('Nottingham', 'Nottingham'), ('Newbury', 'Newbury'), ('Goodwood', 'Goodwood'), ('Carlisle', 'Carlisle'), ('Kelso', 'Kelso'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Redcar', 'Redcar'), ('Hamilton', 'Hamilton Park'), ('Warwick', 'Warwick'), ('Exeter', 'Exeter'), ('Cartmel', 'Cartmel'), ('Wetherby', 'Wetherby'), ('Kempton Park', 'Kempton Park'), ('Ayr', 'Ayr'), ('Ludlow', 'Ludlow'), ('Salisbury', 'Salisbury'), ('Musselburgh', 'Musselburgh'), ('Thirsk', 'Thirsk'), ('Perth', 'Perth'), ('Chester', 'Chester'), ('Epsom Downs', 'Epsom Downs'), ('Taunton', 'Taunton'), ('Aintree', 'Aintree'), ('Catterick Bridge', 'Catterick Bridge'), ('Haydock', 'Haydock Park'), ('Beverly', 'Beverly'), ('Leicester', 'Leicester'), ('Newmarket', 'Newmarket'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('York', 'York'), ('Dundalk', 'Dundalk'), ('Cheltenham', 'Cheltenham')], max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='frankel',
            name='status',
            field=models.CharField(choices=[('In Service', 'In Service'), ('In Repair', 'In Repair'), ('Not In Service', 'Not In Service')], default='In Service', max_length=15),
        ),
        migrations.AlterField(
            model_name='frankel_entry',
            name='status',
            field=models.CharField(choices=[('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Racing: Not to course', 'On course - racing: Not to course')], default='In Service', max_length=41),
        ),
        migrations.AlterField(
            model_name='frankel_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Wincanton', 'Wincanton'), ('Huntingdon', 'Huntingdon'), ('Market Rasen', 'Market Rasen'), ('Nottingham', 'Nottingham'), ('Newbury', 'Newbury'), ('Goodwood', 'Goodwood'), ('Carlisle', 'Carlisle'), ('Kelso', 'Kelso'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Redcar', 'Redcar'), ('Hamilton', 'Hamilton Park'), ('Warwick', 'Warwick'), ('Exeter', 'Exeter'), ('Cartmel', 'Cartmel'), ('Wetherby', 'Wetherby'), ('Kempton Park', 'Kempton Park'), ('Ayr', 'Ayr'), ('Ludlow', 'Ludlow'), ('Salisbury', 'Salisbury'), ('Musselburgh', 'Musselburgh'), ('Thirsk', 'Thirsk'), ('Perth', 'Perth'), ('Chester', 'Chester'), ('Epsom Downs', 'Epsom Downs'), ('Taunton', 'Taunton'), ('Aintree', 'Aintree'), ('Catterick Bridge', 'Catterick Bridge'), ('Haydock', 'Haydock Park'), ('Beverly', 'Beverly'), ('Leicester', 'Leicester'), ('Newmarket', 'Newmarket'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('York', 'York'), ('Dundalk', 'Dundalk'), ('Cheltenham', 'Cheltenham')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='kauto',
            name='status',
            field=models.CharField(choices=[('In Service', 'In Service'), ('In Repair', 'In Repair'), ('Not In Service', 'Not In Service')], default='In Service', max_length=15),
        ),
        migrations.AlterField(
            model_name='kauto_entry',
            name='status',
            field=models.CharField(choices=[('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Racing: Not to course', 'On course - racing: Not to course')], default='In Service', max_length=41),
        ),
        migrations.AlterField(
            model_name='kauto_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Wincanton', 'Wincanton'), ('Huntingdon', 'Huntingdon'), ('Market Rasen', 'Market Rasen'), ('Nottingham', 'Nottingham'), ('Newbury', 'Newbury'), ('Goodwood', 'Goodwood'), ('Carlisle', 'Carlisle'), ('Kelso', 'Kelso'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Redcar', 'Redcar'), ('Hamilton', 'Hamilton Park'), ('Warwick', 'Warwick'), ('Exeter', 'Exeter'), ('Cartmel', 'Cartmel'), ('Wetherby', 'Wetherby'), ('Kempton Park', 'Kempton Park'), ('Ayr', 'Ayr'), ('Ludlow', 'Ludlow'), ('Salisbury', 'Salisbury'), ('Musselburgh', 'Musselburgh'), ('Thirsk', 'Thirsk'), ('Perth', 'Perth'), ('Chester', 'Chester'), ('Epsom Downs', 'Epsom Downs'), ('Taunton', 'Taunton'), ('Aintree', 'Aintree'), ('Catterick Bridge', 'Catterick Bridge'), ('Haydock', 'Haydock Park'), ('Beverly', 'Beverly'), ('Leicester', 'Leicester'), ('Newmarket', 'Newmarket'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('York', 'York'), ('Dundalk', 'Dundalk'), ('Cheltenham', 'Cheltenham')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='other',
            name='status',
            field=models.CharField(choices=[('In Service', 'In Service'), ('In Repair', 'In Repair'), ('Not In Service', 'Not In Service')], default='In Service', max_length=15),
        ),
        migrations.AlterField(
            model_name='other_entry',
            name='status',
            field=models.CharField(choices=[('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Racing: Not to course', 'On course - racing: Not to course')], default='In Service', max_length=41),
        ),
        migrations.AlterField(
            model_name='other_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Wincanton', 'Wincanton'), ('Huntingdon', 'Huntingdon'), ('Market Rasen', 'Market Rasen'), ('Nottingham', 'Nottingham'), ('Newbury', 'Newbury'), ('Goodwood', 'Goodwood'), ('Carlisle', 'Carlisle'), ('Kelso', 'Kelso'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Redcar', 'Redcar'), ('Hamilton', 'Hamilton Park'), ('Warwick', 'Warwick'), ('Exeter', 'Exeter'), ('Cartmel', 'Cartmel'), ('Wetherby', 'Wetherby'), ('Kempton Park', 'Kempton Park'), ('Ayr', 'Ayr'), ('Ludlow', 'Ludlow'), ('Salisbury', 'Salisbury'), ('Musselburgh', 'Musselburgh'), ('Thirsk', 'Thirsk'), ('Perth', 'Perth'), ('Chester', 'Chester'), ('Epsom Downs', 'Epsom Downs'), ('Taunton', 'Taunton'), ('Aintree', 'Aintree'), ('Catterick Bridge', 'Catterick Bridge'), ('Haydock', 'Haydock Park'), ('Beverly', 'Beverly'), ('Leicester', 'Leicester'), ('Newmarket', 'Newmarket'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('York', 'York'), ('Dundalk', 'Dundalk'), ('Cheltenham', 'Cheltenham')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='winx',
            name='status',
            field=models.CharField(choices=[('In Service', 'In Service'), ('In Repair', 'In Repair'), ('Not In Service', 'Not In Service')], default='In Service', max_length=15),
        ),
    ]
