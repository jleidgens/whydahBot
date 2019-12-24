import os
from pytz import timezone
from datetime import datetime
from dateutil.relativedelta import relativedelta

from marinetrafficapi import MarineTrafficApi

SECONDS_IN_DAY = 24 * 60 * 60
LAST_HOUR = 60


def get_last_port_call(ship_id):
    api = MarineTrafficApi(api_key=os.getenv('MARINE_TRAFFIC_API_KEY'))
    result = api.port_calls(imo=ship_id, time_span=LAST_HOUR, movetype=0)
    if result.models:
        return result.models[0]
    return None


def get_ship_name(port_call):
    return port_call.ship_name.value


def get_port_name(port_call):
    return port_call.port_name.value


def get_local_time(port_call):
    return port_call.local_timestamp.value


def get_time_difference_of_port(port_call):
    utc = timezone('utc').localize(port_call.utc_timestamp.value)
    german_time = utc.astimezone(timezone('Europe/Berlin')).replace(tzinfo=None)
    ship_local_time = get_local_time(port_call)

    return relativedelta(german_time, ship_local_time).hours
