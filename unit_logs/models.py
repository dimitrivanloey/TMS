from django.db import models

class Tracker(models.Model):
    STATUS_CHOICES = (
      ('In Service', 'In Service'),
      ('In Repair', 'In Repair'),
      ('Not In Service', 'Not In Service'),
      ('Lost', 'Lost')
    )

    TRACKER_TYPES = (
      ('Arkle', 'Arkle'),
      ('Enable', 'Enable'),
      ('Denman', 'Denman'),
      ('Frankel', 'Frankel'),
      ('Kauto', 'Kauto'),
      ('Winx', 'Winx'),
      ('Other', 'Other')
    )

    number = models.PositiveSmallIntegerField()
    group = models.CharField(max_length=15, choices=TRACKER_TYPES, null=False)
    date_added = models.DateField(auto_now=True)

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='In Service')

    start_date = models.DateField(blank=True, null=True)
    class Meta:
      unique_together = ('number', 'group')

    def __str__(self):
        """Returning a sring representation of the model"""
        name = f"{self.group[0]}{self.number}"
        return name

class Entry(models.Model):

    STATUS = (
      ('On Course - Test: No Solid White', 'On course - Test: No Solid White'),
      ('On Course - Test: No Orange', 'On course - Test: No Orange'),
      ('On Course - Test: Broken Switch', 'On course - Test: Broken Switch'),
      ('On Course - Test: Broken Connector', 'On course - Test: Broken Connector'),
      ('On Course - Racing: Not to course', 'On course - racing: Not to course'),
      ('On Course - Racing: Stuck on track', 'On course - racing: Stuck on track'),
      ('On Course - Racing: Good Performance', 'On course - racing: Good Performance'),
      ('On Course - Test: No Red', 'On Course - Test: No Red'),
      ('In Refurb - Send for mechanical repair', 'In Refurb - Send for mechanical repair'),
      ('In Refurb - No reply from modem', 'In Refurb - No reply from modem'),
      ('In Refurb - Broken beyond repair', 'In Refurb - Broken beyond repair'),
      ('In Refurb - Fixed and returning to course', 'In Refurb - Fixed and returning to course'),
      ('Out of Service and Returned for Refurb', 'Out of Service and returned for Refurb'),
    )

    VENUES = (
        ('Aintree', 'Aintree'),
        ('Ayr', 'Ayr'),
        ('Beverly', 'Beverly'),
        ('Carlisle', 'Carlisle'),
        ('Cartmel', 'Cartmel'),
        ('Catterick Bridge', 'Catterick Bridge'),
        ('Cheltenham', 'Cheltenham'),
        ('Chester', 'Chester'),
        ('Dundalk', 'Dundalk'),
        ('Epsom Downs', 'Epsom Downs'),
        ('Exeter', 'Exeter'),
        ('Goodwood', 'Goodwood'),
        ('Hamilton', 'Hamilton Park'),
        ('Haydock', 'Haydock Park'),
        ('Huntingdon', 'Huntingdon'),
        ('Kelso', 'Kelso'),
        ('Kempton Park', 'Kempton Park'),
        ('Leicester', 'Leicester'),
        ('Ludlow', 'Ludlow'),
        ('Market Rasen', 'Market Rasen'),
        ('Musselburgh', 'Musselburgh'),
        ('Newbury', 'Newbury'),
        ('Newmarket', 'Newmarket'),
        ('Nottingham', 'Nottingham'),
        ('Perth', 'Perth'),
        ('Pontefract', 'Pontefract'),
        ('Salisbury', 'Salisbury'),
        ('Redcar', 'Redcar'),
        ('Sandown Park', 'Sandown Park'),
        ('Stratford-On-Avon', 'Stratford-On-Avon'),
        ('Taunton', 'Taunton'),
        ('Thirsk', 'Thirsk'),
        ('Warwick', 'Warwick'),
        ('Wetherby', 'Wetherby'),
        ('Wincanton', 'Wincanton'),
        ('York', 'York'),
    )

    tracker = models.ForeignKey(Tracker, on_delete=models.CASCADE, default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=41, choices=STATUS, blank=True, null=True)
    venue = models.CharField(max_length=18, choices=VENUES, blank=True, null=True)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        return f"Entry: {self.date_added}"


class Failure(models.Model):
    """Specifies a list of failures"""

    FAILURE_CODES = (
        ('Battery Failure', 'Battery Failure'),
        ('USB Connector Broken', 'USB Connector Broken'),
        ('Switch Broken', 'Switch Broken'),
        ('Case Damaged', 'Case Damaged'),
        ('Lights in Grey State', 'Lights in Grey State'),
        ('Clear Water Ingress Damage', 'Clear Water Ingress Damage'),
        ('Antenna Broken', 'Antenna Broken'),
        ('Unknown', 'Unknown')
    )

    tracker = models.ForeignKey(Tracker, on_delete=models.CASCADE)
    code = models.CharField(max_length=41, choices=FAILURE_CODES, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'failures'

    def __str__(self):
        return f"Failure Code: {self.code}"
