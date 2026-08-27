
from rest_framework.test import APITestCase

class TestView(APITestCase):

    def test_weather_json_api(self):
        data={
            "doy": 1,
            "temperature": 38.0,
            "wetting": 1,
            "humidity": 32.0,
            "rain": 14.0,
            "events": [
                {"index": 0, "x": 0.4},
                {"index": 1, "x": 0.0}
            ]
        }

        actual= self.client.post("", data, format="json")
        resp_data= actual.json()

        events= resp_data["events"]

        self.assertEqual(actual.status_code, 200)
        self.assertEqual(resp_data["doy"], 1)

        self.assertEqual(len(events), 3)
        self.assertEqual(events[2]["index"], 2)
        self.assertEqual(events[2]["x"], 0.0)