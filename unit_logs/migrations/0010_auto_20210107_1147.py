# Generated by Django 3.0.5 on 2021-01-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_logs', '0009_auto_20210107_1143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['status'], 'verbose_name_plural': 'entries'},
        ),
        migrations.AlterField(
            model_name='arkle',
            name='status',
            field=models.CharField(choices=[('IN SERVICE', 'In Service'), ('NOT IN SERVICE', 'Not In Service'), ('IN REPAIR', 'In Repair')], default='IN SERVICE', max_length=15),
        ),
        migrations.AlterField(
            model_name='arkle_entry',
            name='status',
            field=models.CharField(choices=[('In Repair', 'In Repair'), ('Never Worked', 'Refurb'), ('Connector Broken', 'Connector Broken'), ('Missing', 'Missing'), ('Failed', 'Failed'), ('No Solid White', 'No Solid White'), ('Damaged Case', 'Damaged Case'), ('No Solid Orange', 'No Solid Orange'), ('Refurb', 'Refurb'), ('Good Performance', 'Good Performance'), ('Failed Battery', 'Failed Battery'), ('Switch Broken', 'Switch Broken'), ('Returned for Investigation', 'Returned for Investigation'), ('Stick', 'Stick')], default='In Service', max_length=30),
        ),
        migrations.AlterField(
            model_name='arkle_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Hamilton', 'Hamilton Park'), ('Pontefract', 'Pontefract'), ('Chester', 'Chester'), ('Wetherby', 'Wetherby'), ('Newbury', 'Newbury'), ('Kempton Park', 'Kempton Park'), ('Market Rasen', 'Market Rasen'), ('Kelso', 'Kelso'), ('Aintree', 'Aintree'), ('Newmarket', 'Newmarket'), ('Redcar', 'Redcar'), ('Goodwood', 'Goodwood'), ('Beverly', 'Beverly'), ('Epsom Downs', 'Epsom Downs'), ('Cartmel', 'Cartmel'), ('York', 'York'), ('Exeter', 'Exeter'), ('Taunton', 'Taunton'), ('Musselburgh', 'Musselburgh'), ('Huntingdon', 'Huntingdon'), ('Salisbury', 'Salisbury'), ('Haydock', 'Haydock Park'), ('Catterick Bridge', 'Catterick Bridge'), ('Leicester', 'Leicester'), ('Thirsk', 'Thirsk'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Wincanton', 'Wincanton'), ('Cheltenham', 'Cheltenham'), ('Warwick', 'Warwick'), ('Ludlow', 'Ludlow'), ('Ayr', 'Ayr'), ('Sandown Park', 'Sandown Park'), ('Perth', 'Perth'), ('Nottingham', 'Nottingham'), ('Carlisle', 'Carlisle')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='denman',
            name='status',
            field=models.CharField(choices=[('IN SERVICE', 'In Service'), ('NOT IN SERVICE', 'Not In Service'), ('IN REPAIR', 'In Repair')], default='IN SERVICE', max_length=15),
        ),
        migrations.AlterField(
            model_name='denman_entry',
            name='status',
            field=models.CharField(choices=[('In Repair', 'In Repair'), ('Never Worked', 'Refurb'), ('Connector Broken', 'Connector Broken'), ('Missing', 'Missing'), ('Failed', 'Failed'), ('No Solid White', 'No Solid White'), ('Damaged Case', 'Damaged Case'), ('No Solid Orange', 'No Solid Orange'), ('Refurb', 'Refurb'), ('Good Performance', 'Good Performance'), ('Failed Battery', 'Failed Battery'), ('Switch Broken', 'Switch Broken'), ('Returned for Investigation', 'Returned for Investigation'), ('Stick', 'Stick')], default='In Service', max_length=30),
        ),
        migrations.AlterField(
            model_name='denman_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Hamilton', 'Hamilton Park'), ('Pontefract', 'Pontefract'), ('Chester', 'Chester'), ('Wetherby', 'Wetherby'), ('Newbury', 'Newbury'), ('Kempton Park', 'Kempton Park'), ('Market Rasen', 'Market Rasen'), ('Kelso', 'Kelso'), ('Aintree', 'Aintree'), ('Newmarket', 'Newmarket'), ('Redcar', 'Redcar'), ('Goodwood', 'Goodwood'), ('Beverly', 'Beverly'), ('Epsom Downs', 'Epsom Downs'), ('Cartmel', 'Cartmel'), ('York', 'York'), ('Exeter', 'Exeter'), ('Taunton', 'Taunton'), ('Musselburgh', 'Musselburgh'), ('Huntingdon', 'Huntingdon'), ('Salisbury', 'Salisbury'), ('Haydock', 'Haydock Park'), ('Catterick Bridge', 'Catterick Bridge'), ('Leicester', 'Leicester'), ('Thirsk', 'Thirsk'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Wincanton', 'Wincanton'), ('Cheltenham', 'Cheltenham'), ('Warwick', 'Warwick'), ('Ludlow', 'Ludlow'), ('Ayr', 'Ayr'), ('Sandown Park', 'Sandown Park'), ('Perth', 'Perth'), ('Nottingham', 'Nottingham'), ('Carlisle', 'Carlisle')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='enable',
            name='status',
            field=models.CharField(choices=[('IN SERVICE', 'In Service'), ('NOT IN SERVICE', 'Not In Service'), ('IN REPAIR', 'In Repair')], default='IN SERVICE', max_length=15),
        ),
        migrations.AlterField(
            model_name='enable_entry',
            name='status',
            field=models.CharField(choices=[('In Repair', 'In Repair'), ('Never Worked', 'Refurb'), ('Connector Broken', 'Connector Broken'), ('Missing', 'Missing'), ('Failed', 'Failed'), ('No Solid White', 'No Solid White'), ('Damaged Case', 'Damaged Case'), ('No Solid Orange', 'No Solid Orange'), ('Refurb', 'Refurb'), ('Good Performance', 'Good Performance'), ('Failed Battery', 'Failed Battery'), ('Switch Broken', 'Switch Broken'), ('Returned for Investigation', 'Returned for Investigation'), ('Stick', 'Stick')], default='In Service', max_length=30),
        ),
        migrations.AlterField(
            model_name='enable_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Hamilton', 'Hamilton Park'), ('Pontefract', 'Pontefract'), ('Chester', 'Chester'), ('Wetherby', 'Wetherby'), ('Newbury', 'Newbury'), ('Kempton Park', 'Kempton Park'), ('Market Rasen', 'Market Rasen'), ('Kelso', 'Kelso'), ('Aintree', 'Aintree'), ('Newmarket', 'Newmarket'), ('Redcar', 'Redcar'), ('Goodwood', 'Goodwood'), ('Beverly', 'Beverly'), ('Epsom Downs', 'Epsom Downs'), ('Cartmel', 'Cartmel'), ('York', 'York'), ('Exeter', 'Exeter'), ('Taunton', 'Taunton'), ('Musselburgh', 'Musselburgh'), ('Huntingdon', 'Huntingdon'), ('Salisbury', 'Salisbury'), ('Haydock', 'Haydock Park'), ('Catterick Bridge', 'Catterick Bridge'), ('Leicester', 'Leicester'), ('Thirsk', 'Thirsk'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Wincanton', 'Wincanton'), ('Cheltenham', 'Cheltenham'), ('Warwick', 'Warwick'), ('Ludlow', 'Ludlow'), ('Ayr', 'Ayr'), ('Sandown Park', 'Sandown Park'), ('Perth', 'Perth'), ('Nottingham', 'Nottingham'), ('Carlisle', 'Carlisle')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.CharField(blank=True, choices=[('On course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('In Refurb: Fixed and returning to course', 'In Refurb: Fixed and returning to course'), ('On course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb: Broken beyond repair', 'In Refurb: Broken beyond repair'), ('In Refurb: Send for mechanical repair', 'In Refurb: Send for mechanical repair'), ('On course - Test: No Red', 'On course - Test: No Red'), ('On course - Test: No Solid White', 'On course - Test: No Solid White'), ('On course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('In Refurb: No reply from modem', 'In Refurb: No reply from modem'), ('Out of Service and returned for Refurb', 'Out of Service and returned for Refurb'), ('On course - Test: No Orange', 'On course - Test: No Orange'), ('On course - Racing: Good Performance', 'On course - racing: Good Performance')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Hamilton', 'Hamilton Park'), ('Pontefract', 'Pontefract'), ('Chester', 'Chester'), ('Wetherby', 'Wetherby'), ('Newbury', 'Newbury'), ('Kempton Park', 'Kempton Park'), ('Market Rasen', 'Market Rasen'), ('Kelso', 'Kelso'), ('Aintree', 'Aintree'), ('Newmarket', 'Newmarket'), ('Redcar', 'Redcar'), ('Goodwood', 'Goodwood'), ('Beverly', 'Beverly'), ('Epsom Downs', 'Epsom Downs'), ('Cartmel', 'Cartmel'), ('York', 'York'), ('Exeter', 'Exeter'), ('Taunton', 'Taunton'), ('Musselburgh', 'Musselburgh'), ('Huntingdon', 'Huntingdon'), ('Salisbury', 'Salisbury'), ('Haydock', 'Haydock Park'), ('Catterick Bridge', 'Catterick Bridge'), ('Leicester', 'Leicester'), ('Thirsk', 'Thirsk'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Wincanton', 'Wincanton'), ('Cheltenham', 'Cheltenham'), ('Warwick', 'Warwick'), ('Ludlow', 'Ludlow'), ('Ayr', 'Ayr'), ('Sandown Park', 'Sandown Park'), ('Perth', 'Perth'), ('Nottingham', 'Nottingham'), ('Carlisle', 'Carlisle')], max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='frankel',
            name='status',
            field=models.CharField(choices=[('IN SERVICE', 'In Service'), ('NOT IN SERVICE', 'Not In Service'), ('IN REPAIR', 'In Repair')], default='IN SERVICE', max_length=15),
        ),
        migrations.AlterField(
            model_name='frankel_entry',
            name='status',
            field=models.CharField(choices=[('In Repair', 'In Repair'), ('Never Worked', 'Refurb'), ('Connector Broken', 'Connector Broken'), ('Missing', 'Missing'), ('Failed', 'Failed'), ('No Solid White', 'No Solid White'), ('Damaged Case', 'Damaged Case'), ('No Solid Orange', 'No Solid Orange'), ('Refurb', 'Refurb'), ('Good Performance', 'Good Performance'), ('Failed Battery', 'Failed Battery'), ('Switch Broken', 'Switch Broken'), ('Returned for Investigation', 'Returned for Investigation'), ('Stick', 'Stick')], default='In Service', max_length=30),
        ),
        migrations.AlterField(
            model_name='frankel_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Hamilton', 'Hamilton Park'), ('Pontefract', 'Pontefract'), ('Chester', 'Chester'), ('Wetherby', 'Wetherby'), ('Newbury', 'Newbury'), ('Kempton Park', 'Kempton Park'), ('Market Rasen', 'Market Rasen'), ('Kelso', 'Kelso'), ('Aintree', 'Aintree'), ('Newmarket', 'Newmarket'), ('Redcar', 'Redcar'), ('Goodwood', 'Goodwood'), ('Beverly', 'Beverly'), ('Epsom Downs', 'Epsom Downs'), ('Cartmel', 'Cartmel'), ('York', 'York'), ('Exeter', 'Exeter'), ('Taunton', 'Taunton'), ('Musselburgh', 'Musselburgh'), ('Huntingdon', 'Huntingdon'), ('Salisbury', 'Salisbury'), ('Haydock', 'Haydock Park'), ('Catterick Bridge', 'Catterick Bridge'), ('Leicester', 'Leicester'), ('Thirsk', 'Thirsk'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Wincanton', 'Wincanton'), ('Cheltenham', 'Cheltenham'), ('Warwick', 'Warwick'), ('Ludlow', 'Ludlow'), ('Ayr', 'Ayr'), ('Sandown Park', 'Sandown Park'), ('Perth', 'Perth'), ('Nottingham', 'Nottingham'), ('Carlisle', 'Carlisle')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='kauto',
            name='status',
            field=models.CharField(choices=[('IN SERVICE', 'In Service'), ('NOT IN SERVICE', 'Not In Service'), ('IN REPAIR', 'In Repair')], default='IN SERVICE', max_length=15),
        ),
        migrations.AlterField(
            model_name='kauto_entry',
            name='status',
            field=models.CharField(choices=[('In Repair', 'In Repair'), ('Never Worked', 'Refurb'), ('Connector Broken', 'Connector Broken'), ('Missing', 'Missing'), ('Failed', 'Failed'), ('No Solid White', 'No Solid White'), ('Damaged Case', 'Damaged Case'), ('No Solid Orange', 'No Solid Orange'), ('Refurb', 'Refurb'), ('Good Performance', 'Good Performance'), ('Failed Battery', 'Failed Battery'), ('Switch Broken', 'Switch Broken'), ('Returned for Investigation', 'Returned for Investigation'), ('Stick', 'Stick')], default='In Service', max_length=30),
        ),
        migrations.AlterField(
            model_name='kauto_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Hamilton', 'Hamilton Park'), ('Pontefract', 'Pontefract'), ('Chester', 'Chester'), ('Wetherby', 'Wetherby'), ('Newbury', 'Newbury'), ('Kempton Park', 'Kempton Park'), ('Market Rasen', 'Market Rasen'), ('Kelso', 'Kelso'), ('Aintree', 'Aintree'), ('Newmarket', 'Newmarket'), ('Redcar', 'Redcar'), ('Goodwood', 'Goodwood'), ('Beverly', 'Beverly'), ('Epsom Downs', 'Epsom Downs'), ('Cartmel', 'Cartmel'), ('York', 'York'), ('Exeter', 'Exeter'), ('Taunton', 'Taunton'), ('Musselburgh', 'Musselburgh'), ('Huntingdon', 'Huntingdon'), ('Salisbury', 'Salisbury'), ('Haydock', 'Haydock Park'), ('Catterick Bridge', 'Catterick Bridge'), ('Leicester', 'Leicester'), ('Thirsk', 'Thirsk'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Wincanton', 'Wincanton'), ('Cheltenham', 'Cheltenham'), ('Warwick', 'Warwick'), ('Ludlow', 'Ludlow'), ('Ayr', 'Ayr'), ('Sandown Park', 'Sandown Park'), ('Perth', 'Perth'), ('Nottingham', 'Nottingham'), ('Carlisle', 'Carlisle')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='winx',
            name='status',
            field=models.CharField(choices=[('IN SERVICE', 'In Service'), ('NOT IN SERVICE', 'Not In Service'), ('IN REPAIR', 'In Repair')], default='IN SERVICE', max_length=15),
        ),
    ]