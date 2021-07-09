# Generated by Django 3.0.5 on 2021-07-06 15:18

from django.db import migrations
from django.db import connection, IntegrityError
from psycopg2 import errors


def assign_birthday(date, first_tracker_number, last_tracker_number, tracker_group):
  for x in range(first_tracker_number, last_tracker_number+1, 1):
    found_id = None

    try:
      cursor = connection.cursor()
      cursor.execute(f"select id from unit_logs_tracker where number = {x} and tracker_group = '{tracker_group}'")
      found_id = cursor.fetchone()[0]
    except:
      continue

    exp = f"insert into unit_logs_entry (timestamp, tracker_id, status_id, comments) select TO_TIMESTAMP('{date} 01:00:00+00', 'YYYY-MM-DD HH:MI:SS'), {found_id}, 1, ''"
    cursor.execute(exp)


class Migration(migrations.Migration):

    dependencies = [
      ('unit_logs', '0009_auto_20210706_1602'),
    ]

    def forwards(apps, schema_editor):
      assign_birthday('2019-09-01', 1,89, 'Arkle')
      assign_birthday('2020-06-01', 101,116, 'Arkle')
      assign_birthday('2020-08-11', 117,122, 'Arkle')
      assign_birthday('2020-12-02', 123,134, 'Arkle')
      assign_birthday('2020-12-29', 135,140, 'Arkle')
      assign_birthday('2021-01-13', 141,142, 'Arkle')
      assign_birthday('2021-05-02', 143,187, 'Arkle')
      assign_birthday('2021-06-01', 188,195, 'Arkle')
      assign_birthday('2019-09-18', 1,65, 'Denman')
      assign_birthday('2019-09-21', 66,99, 'Denman')
      assign_birthday('2020-06-02', 100,111, 'Denman')
      assign_birthday('2020-12-22', 112,135, 'Denman')
      assign_birthday('2020-03-26', 136,138, 'Denman')
      assign_birthday('2021-05-07', 139,166, 'Denman')
      assign_birthday('2021-06-01', 167,195, 'Denman')
      assign_birthday('2019-07-27', 1,55, 'Enable')
      assign_birthday('2019-08-21', 57,80, 'Enable')
      assign_birthday('2019-09-12', 82,96, 'Enable')
      assign_birthday('2020-06-03', 101,121, 'Enable')
      assign_birthday('2020-09-15', 123,125, 'Enable')
      assign_birthday('2020-11-18', 126,127, 'Enable')
      assign_birthday('2020-06-20', 128, 128, 'Enable')
      assign_birthday('2020-09-04', 129,130, 'Enable')
      assign_birthday('2020-12-02', 131,145, 'Enable')
      assign_birthday('2020-12-26', 146,160, 'Enable')
      assign_birthday('2021-05-05', 161,165, 'Enable')
      assign_birthday('2021-06-01', 166, 195, 'Enable')
      assign_birthday('2019-10-02', 1,43, 'Winx')
      assign_birthday('2019-11-01', 44,74, 'Winx')
      assign_birthday('2019-12-07', 76,80, 'Winx')
      assign_birthday('2020-06-01', 81,97, 'Winx')
      assign_birthday('2020-12-04', 100,112, 'Winx')
      assign_birthday('2021-02-22', 113,134, 'Winx')
      assign_birthday('2021-05-07', 135,165, 'Winx')
      assign_birthday('2021-06-01', 166,195, 'Winx')



    operations = [
      migrations.RunPython(forwards)
    ]
