import random
from .classes import Event, Weather


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


def get_request_events(request):
    events = []
    client_events = request.data.get("events", [])

    for ev in client_events:
        event = Event(
            ev["index"],
            ev["x"]
        )
        events.append(event)

    return events