import unittest

from weatherapp.weather.classes import Weather, Event
from weatherapp.weather.services import event_create, event_x_update


class TestService(unittest.TestCase):

  def test_event_create(self):
      weather = Weather(
          doy=1,
          temperature=38.0,
          wetting=1,
          humidity=32.0,
          rain=14.0
      )

      event = event_create(weather, 0)

      self.assertIsNotNone(event)
      self.assertEqual(event.index, 0)
      self.assertEqual(event.x, 0)


  def test_event_not_create(self):
      weather = Weather(
          doy=2,
          temperature=38.0,
          wetting=0,
          humidity=32.0,
          rain=0.0
      )

      event= event_create(weather, 0)

      self.assertIsNone(event)


  def test_x_not_decrease(self):
      event= Event(0, 0.1)
      events= [event]
      event_x_update(events)

      self.assertGreater(event.x,0)


  def test_x_not_exceeds_1(self):
      event = Event(0, 0.9)
      events = [event]
      event_x_update(events)

      self.assertLessEqual(event.x, 1)