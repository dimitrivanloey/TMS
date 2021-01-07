from django.db import models

class Winx(models.Model):

    STATUS_CHOICES = {
        ('IN SERVICE', 'In Service'),
        ('IN REPAIR', 'In Repair'),
        ('NOT IN SERVICE', 'Not In Service'),
    }

    number = models.PositiveSmallIntegerField(unique=True)
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='IN SERVICE')

    def __str__(self):
        """Returning a sring representation of the model"""
        name = f"W{self.number}"
        return name


class Enable(models.Model):

    STATUS_CHOICES = {
        ('IN SERVICE', 'In Service'),
        ('IN REPAIR', 'In Repair'),
        ('NOT IN SERVICE', 'Not In Service'),
    }

    number = models.PositiveSmallIntegerField(unique=True)
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='IN SERVICE')

    def __str__(self):
        """Returning a sring representation of the model"""
        name = f"E{self.number}"
        return name


class Arkle(models.Model):

    STATUS_CHOICES = {
        ('IN SERVICE', 'In Service'),
        ('IN REPAIR', 'In Repair'),
        ('NOT IN SERVICE', 'Not In Service'),
    }

    number = models.PositiveSmallIntegerField(unique=True)
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='IN SERVICE')

    def __str__(self):
        """Returning a sring representation of the model"""
        name = f"A{self.number}"
        return name


class Denman(models.Model):

    STATUS_CHOICES = {
        ('IN SERVICE', 'In Service'),
        ('IN REPAIR', 'In Repair'),
        ('NOT IN SERVICE', 'Not In Service'),
    }

    number = models.PositiveSmallIntegerField(unique=True)
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='IN SERVICE')

    def __str__(self):
        """Returning a sring representation of the model"""
        name = f"D{self.number}"
        return name



class Kauto(models.Model):

    STATUS_CHOICES = {
        ('IN SERVICE', 'In Service'),
        ('IN REPAIR', 'In Repair'),
        ('NOT IN SERVICE', 'Not In Service'),
    }

    number = models.PositiveSmallIntegerField(unique=True)
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='IN SERVICE')

    def __str__(self):
        """Returning a sring representation of the model"""
        name = f"K{self.number}"
        return name


class Frankel(models.Model):

    STATUS_CHOICES = {
        ('IN SERVICE', 'In Service'),
        ('IN REPAIR', 'In Repair'),
        ('NOT IN SERVICE', 'Not In Service'),
    }

    number = models.PositiveSmallIntegerField(unique=True)
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='IN SERVICE')

    def __str__(self):
        """Returning a sring representation of the model"""
        name = f"F{self.number}"
        return name


class Entry(models.Model):


    STATUS = {
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
    }

    VENUES = {
        ('Aintree', 'Aintree'),
        ('Ayr', 'Ayr'),
        ('Beverly', 'Beverly'),
        ('Carlisle', 'Carlisle'),
        ('Cartmel', 'Cartmel'),
        ('Catterick Bridge', 'Catterick Bridge'),
        ('Cheltenham', 'Cheltenham'),
        ('Chester', 'Chester'),
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
    }

    winx = models.ForeignKey(Winx, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=41, choices=STATUS, blank=True, null=True)
    venue = models.CharField(max_length=18, choices=VENUES, blank=True, null=True)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        return f"Entry: {self.date_added}"


class Enable_Entry(models.Model):

    STATUS_CHOICES = {
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
    }

    VENUES = {
        ('Aintree', 'Aintree'),
        ('Ayr', 'Ayr'),
        ('Beverly', 'Beverly'),
        ('Carlisle', 'Carlisle'),
        ('Cartmel', 'Cartmel'),
        ('Catterick Bridge', 'Catterick Bridge'),
        ('Cheltenham', 'Cheltenham'),
        ('Chester', 'Chester'),
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
    }

    enable = models.ForeignKey(Enable, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=41, choices=STATUS_CHOICES, default='In Service')
    venue = models.CharField(max_length=18, choices=VENUES, default='Kempton Park', blank=True, null=True)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'enable entries'

    def __str__(self):
        return f"Entry: {self.date_added}"


class Arkle_Entry(models.Model):

    STATUS_CHOICES = {
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
    }

    VENUES = {
        ('Aintree', 'Aintree'),
        ('Ayr', 'Ayr'),
        ('Beverly', 'Beverly'),
        ('Carlisle', 'Carlisle'),
        ('Cartmel', 'Cartmel'),
        ('Catterick Bridge', 'Catterick Bridge'),
        ('Cheltenham', 'Cheltenham'),
        ('Chester', 'Chester'),
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
    }

    arkle = models.ForeignKey(Arkle, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=41, choices=STATUS_CHOICES, default='In Service')
    venue = models.CharField(max_length=18, choices=VENUES, default='Kempton Park', blank=True, null=True)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'arkle entries'

    def __str__(self):
        return f"Entry: {self.date_added}"

class Denman_Entry(models.Model):

    STATUS_CHOICES = {
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
    }

    VENUES = {
        ('Aintree', 'Aintree'),
        ('Ayr', 'Ayr'),
        ('Beverly', 'Beverly'),
        ('Carlisle', 'Carlisle'),
        ('Cartmel', 'Cartmel'),
        ('Catterick Bridge', 'Catterick Bridge'),
        ('Cheltenham', 'Cheltenham'),
        ('Chester', 'Chester'),
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
    }

    denman = models.ForeignKey(Denman, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=41, choices=STATUS_CHOICES, default='In Service')
    venue = models.CharField(max_length=18, choices=VENUES, default='Kempton Park', blank=True, null=True)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'denman entries'

    def __str__(self):
        return f"Entry: {self.date_added}"

class Kauto_Entry(models.Model):

    STATUS_CHOICES = {
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
    }

    VENUES = {
        ('Aintree', 'Aintree'),
        ('Ayr', 'Ayr'),
        ('Beverly', 'Beverly'),
        ('Carlisle', 'Carlisle'),
        ('Cartmel', 'Cartmel'),
        ('Catterick Bridge', 'Catterick Bridge'),
        ('Cheltenham', 'Cheltenham'),
        ('Chester', 'Chester'),
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
    }

    kauto = models.ForeignKey(Kauto, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=41, choices=STATUS_CHOICES, default='In Service')
    venue = models.CharField(max_length=18, choices=VENUES, default='Kempton Park', blank=True, null=True)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'kauto entries'

    def __str__(self):
        return f"Entry: {self.date_added}"

class Frankel_Entry(models.Model):

    STATUS_CHOICES = {
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
    }

    VENUES = {
        ('Aintree', 'Aintree'),
        ('Ayr', 'Ayr'),
        ('Beverly', 'Beverly'),
        ('Carlisle', 'Carlisle'),
        ('Cartmel', 'Cartmel'),
        ('Catterick Bridge', 'Catterick Bridge'),
        ('Cheltenham', 'Cheltenham'),
        ('Chester', 'Chester'),
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
    }

    frankel = models.ForeignKey(Frankel, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=41, choices=STATUS_CHOICES, default='In Service')
    venue = models.CharField(max_length=18, choices=VENUES, default='Kempton Park', blank=True, null=True)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'frankel entries'

    def __str__(self):
        return f"Entry: {self.date_added}"
