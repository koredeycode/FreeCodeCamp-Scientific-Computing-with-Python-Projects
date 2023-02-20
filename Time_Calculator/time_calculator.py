#add_time("11:30 AM", "2:32", "Monday")
def add_time(start, duration, day=None):
  if day is not None:
    day = day.capitalize()
  li = start.split(" ")
  ltime = li[0].split(":")
  start_hour = int(ltime[0])
  start_minute = int(ltime[1])
  start_time = li[1]
  if start_time == "PM":
    start_hour += 12

  lid = duration.split(":")
  duration_hour = int(lid[0])
  duration_minute = int(lid[1])

  day_count = 0
  while duration_hour > 24:
    day_count += 1
    duration_hour -= 24

  total_hour = duration_hour + start_hour
  total_minute = duration_minute + start_minute

  while total_minute > 60:
    total_hour += 1
    total_minute -= 60

  while total_hour >= 24:
    day_count += 1
    total_hour -= 24
  total_time = "AM"
  if total_hour >= 12:
    total_time = "PM"
    total_hour -= 12
  if total_hour == 0:
    total_hour = 12

  new_time = "{}:{:02} {}{}".format(total_hour, total_minute, total_time,
                                    end_day(day, day_count))
  return new_time


def end_day(start_day, difference):
  days = [
    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
    "Saturday"
  ]
  if not start_day:
    day_text = ""
  else:
    start_day_index = days.index(start_day)
    day_text = ", " + days[(start_day_index + difference) % 7]
  if difference == 0:
    return day_text
  if difference == 1:
    return day_text + " (next day)"
  return day_text + " ({} days later)".format(difference)
