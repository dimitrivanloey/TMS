# Generated by Django 3.0.5 on 2021-01-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_logs', '0014_auto_20210108_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arkle',
            name='status',
            field=models.CharField(choices=[('Not In Service', 'Not In Service'), ('In Repair', 'In Repair'), ('In Service', 'In Service')], default='In Service', max_length=15),
        ),
        migrations.AlterField(
            model_name='arkle_entry',
            name='status',
            field=models.CharField(choices=[('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('On Course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem')], default='In Service', max_length=41),
        ),
        migrations.AlterField(
            model_name='arkle_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Ayr', 'Ayr'), ('Chester', 'Chester'), ('Musselburgh', 'Musselburgh'), ('Wincanton', 'Wincanton'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Newbury', 'Newbury'), ('Newmarket', 'Newmarket'), ('Hamilton', 'Hamilton Park'), ('Nottingham', 'Nottingham'), ('Warwick', 'Warwick'), ('Kempton Park', 'Kempton Park'), ('Salisbury', 'Salisbury'), ('Goodwood', 'Goodwood'), ('Wetherby', 'Wetherby'), ('Epsom Downs', 'Epsom Downs'), ('Cheltenham', 'Cheltenham'), ('Huntingdon', 'Huntingdon'), ('Taunton', 'Taunton'), ('Haydock', 'Haydock Park'), ('Aintree', 'Aintree'), ('Thirsk', 'Thirsk'), ('Cartmel', 'Cartmel'), ('Ludlow', 'Ludlow'), ('Perth', 'Perth'), ('York', 'York'), ('Carlisle', 'Carlisle'), ('Leicester', 'Leicester'), ('Exeter', 'Exeter'), ('Kelso', 'Kelso'), ('Beverly', 'Beverly'), ('Redcar', 'Redcar'), ('Catterick Bridge', 'Catterick Bridge'), ('Market Rasen', 'Market Rasen'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='denman',
            name='status',
            field=models.CharField(choices=[('Not In Service', 'Not In Service'), ('In Repair', 'In Repair'), ('In Service', 'In Service')], default='In Service', max_length=15),
        ),
        migrations.AlterField(
            model_name='denman_entry',
            name='status',
            field=models.CharField(choices=[('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('On Course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem')], default='In Service', max_length=41),
        ),
        migrations.AlterField(
            model_name='denman_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Ayr', 'Ayr'), ('Chester', 'Chester'), ('Musselburgh', 'Musselburgh'), ('Wincanton', 'Wincanton'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Newbury', 'Newbury'), ('Newmarket', 'Newmarket'), ('Hamilton', 'Hamilton Park'), ('Nottingham', 'Nottingham'), ('Warwick', 'Warwick'), ('Kempton Park', 'Kempton Park'), ('Salisbury', 'Salisbury'), ('Goodwood', 'Goodwood'), ('Wetherby', 'Wetherby'), ('Epsom Downs', 'Epsom Downs'), ('Cheltenham', 'Cheltenham'), ('Huntingdon', 'Huntingdon'), ('Taunton', 'Taunton'), ('Haydock', 'Haydock Park'), ('Aintree', 'Aintree'), ('Thirsk', 'Thirsk'), ('Cartmel', 'Cartmel'), ('Ludlow', 'Ludlow'), ('Perth', 'Perth'), ('York', 'York'), ('Carlisle', 'Carlisle'), ('Leicester', 'Leicester'), ('Exeter', 'Exeter'), ('Kelso', 'Kelso'), ('Beverly', 'Beverly'), ('Redcar', 'Redcar'), ('Catterick Bridge', 'Catterick Bridge'), ('Market Rasen', 'Market Rasen'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='enable',
            name='status',
            field=models.CharField(choices=[('Not In Service', 'Not In Service'), ('In Repair', 'In Repair'), ('In Service', 'In Service')], default='In Service', max_length=15),
        ),
        migrations.AlterField(
            model_name='enable_entry',
            name='status',
            field=models.CharField(choices=[('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('On Course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem')], default='In Service', max_length=41),
        ),
        migrations.AlterField(
            model_name='enable_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Ayr', 'Ayr'), ('Chester', 'Chester'), ('Musselburgh', 'Musselburgh'), ('Wincanton', 'Wincanton'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Newbury', 'Newbury'), ('Newmarket', 'Newmarket'), ('Hamilton', 'Hamilton Park'), ('Nottingham', 'Nottingham'), ('Warwick', 'Warwick'), ('Kempton Park', 'Kempton Park'), ('Salisbury', 'Salisbury'), ('Goodwood', 'Goodwood'), ('Wetherby', 'Wetherby'), ('Epsom Downs', 'Epsom Downs'), ('Cheltenham', 'Cheltenham'), ('Huntingdon', 'Huntingdon'), ('Taunton', 'Taunton'), ('Haydock', 'Haydock Park'), ('Aintree', 'Aintree'), ('Thirsk', 'Thirsk'), ('Cartmel', 'Cartmel'), ('Ludlow', 'Ludlow'), ('Perth', 'Perth'), ('York', 'York'), ('Carlisle', 'Carlisle'), ('Leicester', 'Leicester'), ('Exeter', 'Exeter'), ('Kelso', 'Kelso'), ('Beverly', 'Beverly'), ('Redcar', 'Redcar'), ('Catterick Bridge', 'Catterick Bridge'), ('Market Rasen', 'Market Rasen'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.CharField(blank=True, choices=[('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('On Course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem')], max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Ayr', 'Ayr'), ('Chester', 'Chester'), ('Musselburgh', 'Musselburgh'), ('Wincanton', 'Wincanton'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Newbury', 'Newbury'), ('Newmarket', 'Newmarket'), ('Hamilton', 'Hamilton Park'), ('Nottingham', 'Nottingham'), ('Warwick', 'Warwick'), ('Kempton Park', 'Kempton Park'), ('Salisbury', 'Salisbury'), ('Goodwood', 'Goodwood'), ('Wetherby', 'Wetherby'), ('Epsom Downs', 'Epsom Downs'), ('Cheltenham', 'Cheltenham'), ('Huntingdon', 'Huntingdon'), ('Taunton', 'Taunton'), ('Haydock', 'Haydock Park'), ('Aintree', 'Aintree'), ('Thirsk', 'Thirsk'), ('Cartmel', 'Cartmel'), ('Ludlow', 'Ludlow'), ('Perth', 'Perth'), ('York', 'York'), ('Carlisle', 'Carlisle'), ('Leicester', 'Leicester'), ('Exeter', 'Exeter'), ('Kelso', 'Kelso'), ('Beverly', 'Beverly'), ('Redcar', 'Redcar'), ('Catterick Bridge', 'Catterick Bridge'), ('Market Rasen', 'Market Rasen'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract')], max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='frankel',
            name='status',
            field=models.CharField(choices=[('Not In Service', 'Not In Service'), ('In Repair', 'In Repair'), ('In Service', 'In Service')], default='In Service', max_length=15),
        ),
        migrations.AlterField(
            model_name='frankel_entry',
            name='status',
            field=models.CharField(choices=[('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('On Course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem')], default='In Service', max_length=41),
        ),
        migrations.AlterField(
            model_name='frankel_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Ayr', 'Ayr'), ('Chester', 'Chester'), ('Musselburgh', 'Musselburgh'), ('Wincanton', 'Wincanton'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Newbury', 'Newbury'), ('Newmarket', 'Newmarket'), ('Hamilton', 'Hamilton Park'), ('Nottingham', 'Nottingham'), ('Warwick', 'Warwick'), ('Kempton Park', 'Kempton Park'), ('Salisbury', 'Salisbury'), ('Goodwood', 'Goodwood'), ('Wetherby', 'Wetherby'), ('Epsom Downs', 'Epsom Downs'), ('Cheltenham', 'Cheltenham'), ('Huntingdon', 'Huntingdon'), ('Taunton', 'Taunton'), ('Haydock', 'Haydock Park'), ('Aintree', 'Aintree'), ('Thirsk', 'Thirsk'), ('Cartmel', 'Cartmel'), ('Ludlow', 'Ludlow'), ('Perth', 'Perth'), ('York', 'York'), ('Carlisle', 'Carlisle'), ('Leicester', 'Leicester'), ('Exeter', 'Exeter'), ('Kelso', 'Kelso'), ('Beverly', 'Beverly'), ('Redcar', 'Redcar'), ('Catterick Bridge', 'Catterick Bridge'), ('Market Rasen', 'Market Rasen'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='kauto',
            name='status',
            field=models.CharField(choices=[('Not In Service', 'Not In Service'), ('In Repair', 'In Repair'), ('In Service', 'In Service')], default='In Service', max_length=15),
        ),
        migrations.AlterField(
            model_name='kauto_entry',
            name='status',
            field=models.CharField(choices=[('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('On Course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem')], default='In Service', max_length=41),
        ),
        migrations.AlterField(
            model_name='kauto_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Ayr', 'Ayr'), ('Chester', 'Chester'), ('Musselburgh', 'Musselburgh'), ('Wincanton', 'Wincanton'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Newbury', 'Newbury'), ('Newmarket', 'Newmarket'), ('Hamilton', 'Hamilton Park'), ('Nottingham', 'Nottingham'), ('Warwick', 'Warwick'), ('Kempton Park', 'Kempton Park'), ('Salisbury', 'Salisbury'), ('Goodwood', 'Goodwood'), ('Wetherby', 'Wetherby'), ('Epsom Downs', 'Epsom Downs'), ('Cheltenham', 'Cheltenham'), ('Huntingdon', 'Huntingdon'), ('Taunton', 'Taunton'), ('Haydock', 'Haydock Park'), ('Aintree', 'Aintree'), ('Thirsk', 'Thirsk'), ('Cartmel', 'Cartmel'), ('Ludlow', 'Ludlow'), ('Perth', 'Perth'), ('York', 'York'), ('Carlisle', 'Carlisle'), ('Leicester', 'Leicester'), ('Exeter', 'Exeter'), ('Kelso', 'Kelso'), ('Beverly', 'Beverly'), ('Redcar', 'Redcar'), ('Catterick Bridge', 'Catterick Bridge'), ('Market Rasen', 'Market Rasen'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='winx',
            name='status',
            field=models.CharField(choices=[('Not In Service', 'Not In Service'), ('In Repair', 'In Repair'), ('In Service', 'In Service')], default='In Service', max_length=15),
        ),
    ]
