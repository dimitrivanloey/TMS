from django.db import models
import emoji
from django.db import connection
from django.utils import timezone
import datetime

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

    def number_per_category_before_date(given_datetime, ordered_entry_sets, all_status_categories):
      # all_categories = [entry.status.category for entry in [t.entry_set.filter(timestamp__lte=given_datetime).order_by('timestamp').last() for t in Tracker.objects.all()] if entry is not None]
      # breakpoint()

      #########################

      # all_cs = []
      # for t in Tracker.objects.all():
      #   last_entry = t.entry_set.filter(timestamp__lte=given_datetime).order_by('timestamp').last()
      #   if last_entry is not None:
      #     all_cs.append(last_entry.status.category)

      ###########################

      all_categories = [e.status.category for e in [entryset.prefetch_related('status').filter(timestamp__lte=given_datetime).last() for entryset in ordered_entry_sets] if e is not None]
      # breakpoint()

      res = [all_categories.count(particular_category) for particular_category in all_status_categories]
      return res

    def latest_entry_in_category(category):
      return [entry for entry in [t.entry_set.order_by('timestamp').last() for t in Tracker.objects.all()] if entry is not None and entry.status.category == category]

    @property
    def current_status(self):
      return self.entry_set.order_by('timestamp').last().status


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


  @property
  def category_style(self):
    return {
      'Warning': 'warning',
      'Failure': 'danger',
      'Repair': 'secondary',
      'OOA': 'dark',
      'OOS': 'light',
      'Working': 'success'
    }.get(self.category, 'primary')

class Entry(models.Model):

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
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    venue = models.CharField(max_length=18, choices=VENUES, blank=True, null=True)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        return f"Entry: {self.timestamp}"
