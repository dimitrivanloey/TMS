# Generated by Django 3.0.5 on 2021-01-07 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_logs', '0008_auto_20210107_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='on_course_racing',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='on_course_test',
        ),
        migrations.AlterField(
            model_name='arkle_entry',
            name='status',
            field=models.CharField(choices=[('No Solid Orange', 'No Solid Orange'), ('Stick', 'Stick'), ('In Repair', 'In Repair'), ('No Solid White', 'No Solid White'), ('Failed', 'Failed'), ('Never Worked', 'Refurb'), ('Damaged Case', 'Damaged Case'), ('Missing', 'Missing'), ('Failed Battery', 'Failed Battery'), ('Returned for Investigation', 'Returned for Investigation'), ('Connector Broken', 'Connector Broken'), ('Switch Broken', 'Switch Broken'), ('Refurb', 'Refurb'), ('Good Performance', 'Good Performance')], default='In Service', max_length=30),
        ),
        migrations.AlterField(
            model_name='arkle_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Catterick Bridge', 'Catterick Bridge'), ('Ludlow', 'Ludlow'), ('Beverly', 'Beverly'), ('Aintree', 'Aintree'), ('Kempton Park', 'Kempton Park'), ('Perth', 'Perth'), ('Salisbury', 'Salisbury'), ('Sandown Park', 'Sandown Park'), ('Redcar', 'Redcar'), ('Wincanton', 'Wincanton'), ('Goodwood', 'Goodwood'), ('Pontefract', 'Pontefract'), ('Thirsk', 'Thirsk'), ('Warwick', 'Warwick'), ('Haydock', 'Haydock Park'), ('Taunton', 'Taunton'), ('Epsom Downs', 'Epsom Downs'), ('Ayr', 'Ayr'), ('Nottingham', 'Nottingham'), ('York', 'York'), ('Newbury', 'Newbury'), ('Newmarket', 'Newmarket'), ('Chester', 'Chester'), ('Exeter', 'Exeter'), ('Wetherby', 'Wetherby'), ('Musselburgh', 'Musselburgh'), ('Cheltenham', 'Cheltenham'), ('Hamilton', 'Hamilton Park'), ('Cartmel', 'Cartmel'), ('Kelso', 'Kelso'), ('Huntingdon', 'Huntingdon'), ('Market Rasen', 'Market Rasen'), ('Carlisle', 'Carlisle'), ('Leicester', 'Leicester'), ('Stratford-On-Avon', 'Stratford-On-Avon')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='denman_entry',
            name='status',
            field=models.CharField(choices=[('No Solid Orange', 'No Solid Orange'), ('Stick', 'Stick'), ('In Repair', 'In Repair'), ('No Solid White', 'No Solid White'), ('Failed', 'Failed'), ('Never Worked', 'Refurb'), ('Damaged Case', 'Damaged Case'), ('Missing', 'Missing'), ('Failed Battery', 'Failed Battery'), ('Returned for Investigation', 'Returned for Investigation'), ('Connector Broken', 'Connector Broken'), ('Switch Broken', 'Switch Broken'), ('Refurb', 'Refurb'), ('Good Performance', 'Good Performance')], default='In Service', max_length=30),
        ),
        migrations.AlterField(
            model_name='denman_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Catterick Bridge', 'Catterick Bridge'), ('Ludlow', 'Ludlow'), ('Beverly', 'Beverly'), ('Aintree', 'Aintree'), ('Kempton Park', 'Kempton Park'), ('Perth', 'Perth'), ('Salisbury', 'Salisbury'), ('Sandown Park', 'Sandown Park'), ('Redcar', 'Redcar'), ('Wincanton', 'Wincanton'), ('Goodwood', 'Goodwood'), ('Pontefract', 'Pontefract'), ('Thirsk', 'Thirsk'), ('Warwick', 'Warwick'), ('Haydock', 'Haydock Park'), ('Taunton', 'Taunton'), ('Epsom Downs', 'Epsom Downs'), ('Ayr', 'Ayr'), ('Nottingham', 'Nottingham'), ('York', 'York'), ('Newbury', 'Newbury'), ('Newmarket', 'Newmarket'), ('Chester', 'Chester'), ('Exeter', 'Exeter'), ('Wetherby', 'Wetherby'), ('Musselburgh', 'Musselburgh'), ('Cheltenham', 'Cheltenham'), ('Hamilton', 'Hamilton Park'), ('Cartmel', 'Cartmel'), ('Kelso', 'Kelso'), ('Huntingdon', 'Huntingdon'), ('Market Rasen', 'Market Rasen'), ('Carlisle', 'Carlisle'), ('Leicester', 'Leicester'), ('Stratford-On-Avon', 'Stratford-On-Avon')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='enable_entry',
            name='status',
            field=models.CharField(choices=[('No Solid Orange', 'No Solid Orange'), ('Stick', 'Stick'), ('In Repair', 'In Repair'), ('No Solid White', 'No Solid White'), ('Failed', 'Failed'), ('Never Worked', 'Refurb'), ('Damaged Case', 'Damaged Case'), ('Missing', 'Missing'), ('Failed Battery', 'Failed Battery'), ('Returned for Investigation', 'Returned for Investigation'), ('Connector Broken', 'Connector Broken'), ('Switch Broken', 'Switch Broken'), ('Refurb', 'Refurb'), ('Good Performance', 'Good Performance')], default='In Service', max_length=30),
        ),
        migrations.AlterField(
            model_name='enable_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Catterick Bridge', 'Catterick Bridge'), ('Ludlow', 'Ludlow'), ('Beverly', 'Beverly'), ('Aintree', 'Aintree'), ('Kempton Park', 'Kempton Park'), ('Perth', 'Perth'), ('Salisbury', 'Salisbury'), ('Sandown Park', 'Sandown Park'), ('Redcar', 'Redcar'), ('Wincanton', 'Wincanton'), ('Goodwood', 'Goodwood'), ('Pontefract', 'Pontefract'), ('Thirsk', 'Thirsk'), ('Warwick', 'Warwick'), ('Haydock', 'Haydock Park'), ('Taunton', 'Taunton'), ('Epsom Downs', 'Epsom Downs'), ('Ayr', 'Ayr'), ('Nottingham', 'Nottingham'), ('York', 'York'), ('Newbury', 'Newbury'), ('Newmarket', 'Newmarket'), ('Chester', 'Chester'), ('Exeter', 'Exeter'), ('Wetherby', 'Wetherby'), ('Musselburgh', 'Musselburgh'), ('Cheltenham', 'Cheltenham'), ('Hamilton', 'Hamilton Park'), ('Cartmel', 'Cartmel'), ('Kelso', 'Kelso'), ('Huntingdon', 'Huntingdon'), ('Market Rasen', 'Market Rasen'), ('Carlisle', 'Carlisle'), ('Leicester', 'Leicester'), ('Stratford-On-Avon', 'Stratford-On-Avon')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.CharField(blank=True, choices=[('On course - Test: Broken Switch', 'On course - Test: Broken Switch'), ('On course - Test: No Solid White', 'On course - Test: No Solid White'), ('In Refurb: Fixed and returning to course', 'In Refurb: Fixed and returning to course'), ('In Refurb: Broken beyond repair', 'In Refurb: Broken beyond repair'), ('On course - Racing: Good Performance', 'On course - racing: Good Performance'), ('Out of Service and returned for Refurb', 'Out of Service and returned for Refurb'), ('In Refurb: No reply from modem', 'In Refurb: No reply from modem'), ('On course - Racing: Not to course', 'On course - racing: Not to course'), ('In Refurb: Send for mechanical repair', 'In Refurb: Send for mechanical repair'), ('On course - Test: Broken Connector', 'On course - Test: Broken Connector'), ('On course - Test: No Orange', 'On course - Test: No Orange'), ('On course - Racing: Stuck on track', 'On course - racing: Stuck on track'), ('On course - Test: No Red', 'On course - Test: No Red')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Catterick Bridge', 'Catterick Bridge'), ('Ludlow', 'Ludlow'), ('Beverly', 'Beverly'), ('Aintree', 'Aintree'), ('Kempton Park', 'Kempton Park'), ('Perth', 'Perth'), ('Salisbury', 'Salisbury'), ('Sandown Park', 'Sandown Park'), ('Redcar', 'Redcar'), ('Wincanton', 'Wincanton'), ('Goodwood', 'Goodwood'), ('Pontefract', 'Pontefract'), ('Thirsk', 'Thirsk'), ('Warwick', 'Warwick'), ('Haydock', 'Haydock Park'), ('Taunton', 'Taunton'), ('Epsom Downs', 'Epsom Downs'), ('Ayr', 'Ayr'), ('Nottingham', 'Nottingham'), ('York', 'York'), ('Newbury', 'Newbury'), ('Newmarket', 'Newmarket'), ('Chester', 'Chester'), ('Exeter', 'Exeter'), ('Wetherby', 'Wetherby'), ('Musselburgh', 'Musselburgh'), ('Cheltenham', 'Cheltenham'), ('Hamilton', 'Hamilton Park'), ('Cartmel', 'Cartmel'), ('Kelso', 'Kelso'), ('Huntingdon', 'Huntingdon'), ('Market Rasen', 'Market Rasen'), ('Carlisle', 'Carlisle'), ('Leicester', 'Leicester'), ('Stratford-On-Avon', 'Stratford-On-Avon')], max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='frankel_entry',
            name='status',
            field=models.CharField(choices=[('No Solid Orange', 'No Solid Orange'), ('Stick', 'Stick'), ('In Repair', 'In Repair'), ('No Solid White', 'No Solid White'), ('Failed', 'Failed'), ('Never Worked', 'Refurb'), ('Damaged Case', 'Damaged Case'), ('Missing', 'Missing'), ('Failed Battery', 'Failed Battery'), ('Returned for Investigation', 'Returned for Investigation'), ('Connector Broken', 'Connector Broken'), ('Switch Broken', 'Switch Broken'), ('Refurb', 'Refurb'), ('Good Performance', 'Good Performance')], default='In Service', max_length=30),
        ),
        migrations.AlterField(
            model_name='frankel_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Catterick Bridge', 'Catterick Bridge'), ('Ludlow', 'Ludlow'), ('Beverly', 'Beverly'), ('Aintree', 'Aintree'), ('Kempton Park', 'Kempton Park'), ('Perth', 'Perth'), ('Salisbury', 'Salisbury'), ('Sandown Park', 'Sandown Park'), ('Redcar', 'Redcar'), ('Wincanton', 'Wincanton'), ('Goodwood', 'Goodwood'), ('Pontefract', 'Pontefract'), ('Thirsk', 'Thirsk'), ('Warwick', 'Warwick'), ('Haydock', 'Haydock Park'), ('Taunton', 'Taunton'), ('Epsom Downs', 'Epsom Downs'), ('Ayr', 'Ayr'), ('Nottingham', 'Nottingham'), ('York', 'York'), ('Newbury', 'Newbury'), ('Newmarket', 'Newmarket'), ('Chester', 'Chester'), ('Exeter', 'Exeter'), ('Wetherby', 'Wetherby'), ('Musselburgh', 'Musselburgh'), ('Cheltenham', 'Cheltenham'), ('Hamilton', 'Hamilton Park'), ('Cartmel', 'Cartmel'), ('Kelso', 'Kelso'), ('Huntingdon', 'Huntingdon'), ('Market Rasen', 'Market Rasen'), ('Carlisle', 'Carlisle'), ('Leicester', 'Leicester'), ('Stratford-On-Avon', 'Stratford-On-Avon')], default='Kempton Park', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='kauto_entry',
            name='status',
            field=models.CharField(choices=[('No Solid Orange', 'No Solid Orange'), ('Stick', 'Stick'), ('In Repair', 'In Repair'), ('No Solid White', 'No Solid White'), ('Failed', 'Failed'), ('Never Worked', 'Refurb'), ('Damaged Case', 'Damaged Case'), ('Missing', 'Missing'), ('Failed Battery', 'Failed Battery'), ('Returned for Investigation', 'Returned for Investigation'), ('Connector Broken', 'Connector Broken'), ('Switch Broken', 'Switch Broken'), ('Refurb', 'Refurb'), ('Good Performance', 'Good Performance')], default='In Service', max_length=30),
        ),
        migrations.AlterField(
            model_name='kauto_entry',
            name='venue',
            field=models.CharField(blank=True, choices=[('Catterick Bridge', 'Catterick Bridge'), ('Ludlow', 'Ludlow'), ('Beverly', 'Beverly'), ('Aintree', 'Aintree'), ('Kempton Park', 'Kempton Park'), ('Perth', 'Perth'), ('Salisbury', 'Salisbury'), ('Sandown Park', 'Sandown Park'), ('Redcar', 'Redcar'), ('Wincanton', 'Wincanton'), ('Goodwood', 'Goodwood'), ('Pontefract', 'Pontefract'), ('Thirsk', 'Thirsk'), ('Warwick', 'Warwick'), ('Haydock', 'Haydock Park'), ('Taunton', 'Taunton'), ('Epsom Downs', 'Epsom Downs'), ('Ayr', 'Ayr'), ('Nottingham', 'Nottingham'), ('York', 'York'), ('Newbury', 'Newbury'), ('Newmarket', 'Newmarket'), ('Chester', 'Chester'), ('Exeter', 'Exeter'), ('Wetherby', 'Wetherby'), ('Musselburgh', 'Musselburgh'), ('Cheltenham', 'Cheltenham'), ('Hamilton', 'Hamilton Park'), ('Cartmel', 'Cartmel'), ('Kelso', 'Kelso'), ('Huntingdon', 'Huntingdon'), ('Market Rasen', 'Market Rasen'), ('Carlisle', 'Carlisle'), ('Leicester', 'Leicester'), ('Stratford-On-Avon', 'Stratford-On-Avon')], default='Kempton Park', max_length=18, null=True),
        ),
    ]
