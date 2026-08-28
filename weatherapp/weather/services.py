import random

from django.db.models import Model

from .classes import Event, Weather
from .models import WeatherResponse


def event_create(weather, index):
    first_condition = (
            weather.wetting == 1 and
            weather.rain > 0.0
    )
    second_condition = (
            weather.wetting == 1 and
            weather.humidity > 80.0 and
            weather.temperature > 15.0
    )

    if first_condition or second_condition:
        return Event(index, 0)
    else:
        return None


def x_growth_1(x):
    return round(x + 0.1, 1)


def x_growth_2(x):
    return round(x + 0.2, 1)


def x_growth_3(x):
    return round(x + 0.4, 1)


def event_x_update(events):
    growth_rules = [x_growth_1, x_growth_2, x_growth_3]
    for event in events:
        random_rule = random.choice(growth_rules)
        updated_x = random_rule(event.x)
        event.x = updated_x
        if event.x > 1:
            event.x = 1

    return events


def weather_data_build(data):
    return Weather(
        data["doy"],
        data["temperature"],
        data["wetting"],
        data["humidity"],
        data["rain"]
    )


def get_multi_doy(client_doys):
    doys = []

    for data in client_doys:
        weather = weather_data_build(data)
        doys.append(weather)

    return doys


def get_request_events(client_doys):
    events = []
    client_events = []

    for ev in client_doys:
        if "events" in ev:
            client_events = ev["events"]
            break

    for ev in client_events:
        event = Event(
            ev["index"],
            ev["x"]
        )
        events.append(event)

    return events


def get_response_info(response_form, weather_list, events):
    for list_index, weather_data in enumerate(weather_list):

        if list_index > 0:
            event_x_update(events)

            new_index = len(events)
            new_event = event_create(weather_data, new_index)

            if new_event:
                events.append(new_event)

        response_events = []

        for event in events:
            response_events.append(
                Event(event.index, event.x)
            )

        response_form.append(
            {
                "doy": weather_data.doy,
                "events": response_events
            }
        )

def save_response(response_serializer):
    for response_data in response_serializer.data:
        WeatherResponse.objects.create(
            doy = response_data["doy"],
            events = response_data["events"]
        )

