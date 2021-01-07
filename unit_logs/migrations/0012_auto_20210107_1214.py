# Generated by Django 3.0.5 on 2021-01-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_logs', '0011_auto_20210107_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arkle',
            name='status',
            field=models.CharField(choices=[('IN SERVICE', 'In Service'), ('NOT IN SERVICE', 'Not In Service'), ('IN REPAIR', 'In Repair')], default='IN SERVICE', max_length=15),
        ),
        migrations.AlterField(
            model_name='arkle_entry',
            name='status',
            field=models.CharField(choices=[('On course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb: Fixed and returning to course', 'In Refurb: Fixed and returning to course'), ('In Refurb: Send for mechanical repair', 'In Refurb: Send for mechanical repair'), ('On course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb: No reply from modem', 'In Refurb: No reply from modem'), ('On course - Test: No Orange', 'On course - Test: No Orange'), ('On course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On course - Test: No Red', 'On course - Test: No Red'), ('On course - Test: No Solid White', 'On course - Test: No Solid White'), ('In Refurb: Broken beyond repair', 'In Refurb: Broken beyond repair'), ('Out of Service and returned for Refurb', 'Out of Service and returned for Refurb')], default='In Service', max_length=40),
        ),
        migrations.AlterField(
            model_name='arkle_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Wincanton', 'Wincanton'), ('Haydock', 'Haydock Park'), ('Epsom Downs', 'Epsom Downs'), ('Salisbury', 'Salisbury'), ('Redcar', 'Redcar'), ('Huntingdon', 'Huntingdon'), ('Kempton Park', 'Kempton Park'), ('Catterick Bridge', 'Catterick Bridge'), ('Chester', 'Chester'), ('Goodwood', 'Goodwood'), ('Cheltenham', 'Cheltenham'), ('Hamilton', 'Hamilton Park'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Newbury', 'Newbury'), ('Leicester', 'Leicester'), ('Ludlow', 'Ludlow'), ('Kelso', 'Kelso'), ('Market Rasen', 'Market Rasen'), ('Newmarket', 'Newmarket'), ('Thirsk', 'Thirsk'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Ayr', 'Ayr'), ('York', 'York'), ('Exeter', 'Exeter'), ('Perth', 'Perth'), ('Cartmel', 'Cartmel'), ('Aintree', 'Aintree'), ('Taunton', 'Taunton'), ('Beverly', 'Beverly'), ('Wetherby', 'Wetherby'), ('Carlisle', 'Carlisle'), ('Nottingham', 'Nottingham'), ('Warwick', 'Warwick'), ('Musselburgh', 'Musselburgh')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='denman',
            name='status',
            field=models.CharField(choices=[('IN SERVICE', 'In Service'), ('NOT IN SERVICE', 'Not In Service'), ('IN REPAIR', 'In Repair')], default='IN SERVICE', max_length=15),
        ),
        migrations.AlterField(
            model_name='denman_entry',
            name='status',
            field=models.CharField(choices=[('On course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb: Fixed and returning to course', 'In Refurb: Fixed and returning to course'), ('In Refurb: Send for mechanical repair', 'In Refurb: Send for mechanical repair'), ('On course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb: No reply from modem', 'In Refurb: No reply from modem'), ('On course - Test: No Orange', 'On course - Test: No Orange'), ('On course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On course - Test: No Red', 'On course - Test: No Red'), ('On course - Test: No Solid White', 'On course - Test: No Solid White'), ('In Refurb: Broken beyond repair', 'In Refurb: Broken beyond repair'), ('Out of Service and returned for Refurb', 'Out of Service and returned for Refurb')], default='In Service', max_length=40),
        ),
        migrations.AlterField(
            model_name='denman_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Wincanton', 'Wincanton'), ('Haydock', 'Haydock Park'), ('Epsom Downs', 'Epsom Downs'), ('Salisbury', 'Salisbury'), ('Redcar', 'Redcar'), ('Huntingdon', 'Huntingdon'), ('Kempton Park', 'Kempton Park'), ('Catterick Bridge', 'Catterick Bridge'), ('Chester', 'Chester'), ('Goodwood', 'Goodwood'), ('Cheltenham', 'Cheltenham'), ('Hamilton', 'Hamilton Park'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Newbury', 'Newbury'), ('Leicester', 'Leicester'), ('Ludlow', 'Ludlow'), ('Kelso', 'Kelso'), ('Market Rasen', 'Market Rasen'), ('Newmarket', 'Newmarket'), ('Thirsk', 'Thirsk'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Ayr', 'Ayr'), ('York', 'York'), ('Exeter', 'Exeter'), ('Perth', 'Perth'), ('Cartmel', 'Cartmel'), ('Aintree', 'Aintree'), ('Taunton', 'Taunton'), ('Beverly', 'Beverly'), ('Wetherby', 'Wetherby'), ('Carlisle', 'Carlisle'), ('Nottingham', 'Nottingham'), ('Warwick', 'Warwick'), ('Musselburgh', 'Musselburgh')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='enable',
            name='status',
            field=models.CharField(choices=[('IN SERVICE', 'In Service'), ('NOT IN SERVICE', 'Not In Service'), ('IN REPAIR', 'In Repair')], default='IN SERVICE', max_length=15),
        ),
        migrations.AlterField(
            model_name='enable_entry',
            name='status',
            field=models.CharField(choices=[('On course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb: Fixed and returning to course', 'In Refurb: Fixed and returning to course'), ('In Refurb: Send for mechanical repair', 'In Refurb: Send for mechanical repair'), ('On course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb: No reply from modem', 'In Refurb: No reply from modem'), ('On course - Test: No Orange', 'On course - Test: No Orange'), ('On course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On course - Test: No Red', 'On course - Test: No Red'), ('On course - Test: No Solid White', 'On course - Test: No Solid White'), ('In Refurb: Broken beyond repair', 'In Refurb: Broken beyond repair'), ('Out of Service and returned for Refurb', 'Out of Service and returned for Refurb')], default='In Service', max_length=40),
        ),
        migrations.AlterField(
            model_name='enable_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Wincanton', 'Wincanton'), ('Haydock', 'Haydock Park'), ('Epsom Downs', 'Epsom Downs'), ('Salisbury', 'Salisbury'), ('Redcar', 'Redcar'), ('Huntingdon', 'Huntingdon'), ('Kempton Park', 'Kempton Park'), ('Catterick Bridge', 'Catterick Bridge'), ('Chester', 'Chester'), ('Goodwood', 'Goodwood'), ('Cheltenham', 'Cheltenham'), ('Hamilton', 'Hamilton Park'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Newbury', 'Newbury'), ('Leicester', 'Leicester'), ('Ludlow', 'Ludlow'), ('Kelso', 'Kelso'), ('Market Rasen', 'Market Rasen'), ('Newmarket', 'Newmarket'), ('Thirsk', 'Thirsk'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Ayr', 'Ayr'), ('York', 'York'), ('Exeter', 'Exeter'), ('Perth', 'Perth'), ('Cartmel', 'Cartmel'), ('Aintree', 'Aintree'), ('Taunton', 'Taunton'), ('Beverly', 'Beverly'), ('Wetherby', 'Wetherby'), ('Carlisle', 'Carlisle'), ('Nottingham', 'Nottingham'), ('Warwick', 'Warwick'), ('Musselburgh', 'Musselburgh')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.CharField(blank=True, choices=[('On Course - Test: No Solid White', 'On course - Test: No Solid White'), ('On Course - Test: No Red', 'On Course - Test: No Red'), ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'), ('On Course - Test: No Orange', 'On course - Test: No Orange'), ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'), ('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'), ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'), ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair'), ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'), ('On Course - Racing: Not to course', 'On course - racing: Not to course'), ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track')], max_length=41, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Wincanton', 'Wincanton'), ('Haydock', 'Haydock Park'), ('Epsom Downs', 'Epsom Downs'), ('Salisbury', 'Salisbury'), ('Redcar', 'Redcar'), ('Huntingdon', 'Huntingdon'), ('Kempton Park', 'Kempton Park'), ('Catterick Bridge', 'Catterick Bridge'), ('Chester', 'Chester'), ('Goodwood', 'Goodwood'), ('Cheltenham', 'Cheltenham'), ('Hamilton', 'Hamilton Park'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Newbury', 'Newbury'), ('Leicester', 'Leicester'), ('Ludlow', 'Ludlow'), ('Kelso', 'Kelso'), ('Market Rasen', 'Market Rasen'), ('Newmarket', 'Newmarket'), ('Thirsk', 'Thirsk'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Ayr', 'Ayr'), ('York', 'York'), ('Exeter', 'Exeter'), ('Perth', 'Perth'), ('Cartmel', 'Cartmel'), ('Aintree', 'Aintree'), ('Taunton', 'Taunton'), ('Beverly', 'Beverly'), ('Wetherby', 'Wetherby'), ('Carlisle', 'Carlisle'), ('Nottingham', 'Nottingham'), ('Warwick', 'Warwick'), ('Musselburgh', 'Musselburgh')], max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='frankel',
            name='status',
            field=models.CharField(choices=[('IN SERVICE', 'In Service'), ('NOT IN SERVICE', 'Not In Service'), ('IN REPAIR', 'In Repair')], default='IN SERVICE', max_length=15),
        ),
        migrations.AlterField(
            model_name='frankel_entry',
            name='status',
            field=models.CharField(choices=[('On course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb: Fixed and returning to course', 'In Refurb: Fixed and returning to course'), ('In Refurb: Send for mechanical repair', 'In Refurb: Send for mechanical repair'), ('On course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb: No reply from modem', 'In Refurb: No reply from modem'), ('On course - Test: No Orange', 'On course - Test: No Orange'), ('On course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On course - Test: No Red', 'On course - Test: No Red'), ('On course - Test: No Solid White', 'On course - Test: No Solid White'), ('In Refurb: Broken beyond repair', 'In Refurb: Broken beyond repair'), ('Out of Service and returned for Refurb', 'Out of Service and returned for Refurb')], default='In Service', max_length=40),
        ),
        migrations.AlterField(
            model_name='frankel_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Wincanton', 'Wincanton'), ('Haydock', 'Haydock Park'), ('Epsom Downs', 'Epsom Downs'), ('Salisbury', 'Salisbury'), ('Redcar', 'Redcar'), ('Huntingdon', 'Huntingdon'), ('Kempton Park', 'Kempton Park'), ('Catterick Bridge', 'Catterick Bridge'), ('Chester', 'Chester'), ('Goodwood', 'Goodwood'), ('Cheltenham', 'Cheltenham'), ('Hamilton', 'Hamilton Park'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Newbury', 'Newbury'), ('Leicester', 'Leicester'), ('Ludlow', 'Ludlow'), ('Kelso', 'Kelso'), ('Market Rasen', 'Market Rasen'), ('Newmarket', 'Newmarket'), ('Thirsk', 'Thirsk'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Ayr', 'Ayr'), ('York', 'York'), ('Exeter', 'Exeter'), ('Perth', 'Perth'), ('Cartmel', 'Cartmel'), ('Aintree', 'Aintree'), ('Taunton', 'Taunton'), ('Beverly', 'Beverly'), ('Wetherby', 'Wetherby'), ('Carlisle', 'Carlisle'), ('Nottingham', 'Nottingham'), ('Warwick', 'Warwick'), ('Musselburgh', 'Musselburgh')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='kauto',
            name='status',
            field=models.CharField(choices=[('IN SERVICE', 'In Service'), ('NOT IN SERVICE', 'Not In Service'), ('IN REPAIR', 'In Repair')], default='IN SERVICE', max_length=15),
        ),
        migrations.AlterField(
            model_name='kauto_entry',
            name='status',
            field=models.CharField(choices=[('On course - Racing: Good Performance', 'On course - racing: Good Performance'), ('On course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb: Fixed and returning to course', 'In Refurb: Fixed and returning to course'), ('In Refurb: Send for mechanical repair', 'In Refurb: Send for mechanical repair'), ('On course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb: No reply from modem', 'In Refurb: No reply from modem'), ('On course - Test: No Orange', 'On course - Test: No Orange'), ('On course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On course - Test: No Red', 'On course - Test: No Red'), ('On course - Test: No Solid White', 'On course - Test: No Solid White'), ('In Refurb: Broken beyond repair', 'In Refurb: Broken beyond repair'), ('Out of Service and returned for Refurb', 'Out of Service and returned for Refurb')], default='In Service', max_length=40),
        ),
        migrations.AlterField(
            model_name='kauto_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Wincanton', 'Wincanton'), ('Haydock', 'Haydock Park'), ('Epsom Downs', 'Epsom Downs'), ('Salisbury', 'Salisbury'), ('Redcar', 'Redcar'), ('Huntingdon', 'Huntingdon'), ('Kempton Park', 'Kempton Park'), ('Catterick Bridge', 'Catterick Bridge'), ('Chester', 'Chester'), ('Goodwood', 'Goodwood'), ('Cheltenham', 'Cheltenham'), ('Hamilton', 'Hamilton Park'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Newbury', 'Newbury'), ('Leicester', 'Leicester'), ('Ludlow', 'Ludlow'), ('Kelso', 'Kelso'), ('Market Rasen', 'Market Rasen'), ('Newmarket', 'Newmarket'), ('Thirsk', 'Thirsk'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Ayr', 'Ayr'), ('York', 'York'), ('Exeter', 'Exeter'), ('Perth', 'Perth'), ('Cartmel', 'Cartmel'), ('Aintree', 'Aintree'), ('Taunton', 'Taunton'), ('Beverly', 'Beverly'), ('Wetherby', 'Wetherby'), ('Carlisle', 'Carlisle'), ('Nottingham', 'Nottingham'), ('Warwick', 'Warwick'), ('Musselburgh', 'Musselburgh')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='winx',
            name='status',
            field=models.CharField(choices=[('IN SERVICE', 'In Service'), ('NOT IN SERVICE', 'Not In Service'), ('IN REPAIR', 'In Repair')], default='IN SERVICE', max_length=15),
        ),
    ]
