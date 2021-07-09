from django.db import models
import emoji
from django.db import connection

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
    tracker_group = models.CharField(max_length=15, choices=TRACKER_TYPES, null=False)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='In Service')

    class Meta:
      unique_together = ('number', 'tracker_group')

    def __str__(self):
        """Returning a sring representation of the model"""
        name = f"{self.tracker_group[0]}{self.number}"
        return name

    def number_per_category_before_date(given_datetime):
      all_categories = [entry.status.category for entry in [t.entry_set.filter(timestamp__lte=given_datetime).order_by('timestamp').last() for t in Tracker.objects.all()] if entry is not None]
      return [all_categories.count(particular_category) for particular_category in Status.all_categories()]

    def latest_entry_in_category(category):
      return [entry for entry in [t.entry_set.order_by('timestamp').last() for t in Tracker.objects.all()] if entry is not None and entry.status.category == category]


class Status(models.Model):
  CATEGORIES = (
    ('Working', 'Working'),
    ('Warning', 'Warning'),
    ('Failure', 'Failure'),
    ('Repair', 'Repair'),
    ('OOA', 'Out of Action'),
    ('OOS', 'Out of Service')
  )

  category = models.CharField(max_length=15, choices=CATEGORIES, null=False)
  description = models.CharField(max_length=50, null=False)

  def category_to_emoji(self):
    return {
      'Warning': emoji.emojize(':red_exclamation_mark:'),
      'Failure': emoji.emojize(':cross_mark:'),
      'Repair': emoji.emojize(':hammer_and_wrench:'),
      'OOA': emoji.emojize(':skull_and_crossbones:'),
      'OOS': emoji.emojize(':red_question_mark:'),
      'Working': emoji.emojize(':check_mark_button:'),
    }.get(self.category, emoji.emojize(':red_question_mark:'))    # 9 is default if x not found

  def all_categories():
    return [category['category'] for category in Status.objects.values('category').distinct()]


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
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    venue = models.CharField(max_length=18, choices=VENUES, blank=True, null=True)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        return f"Entry: {self.timestamp}"
