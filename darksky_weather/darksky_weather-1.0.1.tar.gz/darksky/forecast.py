from typing import List
from datetime import datetime

from . import base
from .utils import get_datetime_from_unix
from .types import languages, units, weather


class CurrentlyForecast(base.AutoInit):
    time: datetime
    summary: str
    icon: str
    nearest_storm_distance: int
    precip_intensity: float
    precip_intensity_error: float
    precip_probability: float
    precip_type: str
    temperature: float
    apparent_temperature: float
    dew_point: float
    humidity: float
    pressure: float
    wind_speed: float
    wind_gust: float
    wind_bearing: int
    cloud_cover: float
    uv_index: int
    visibility: float
    ozone: float


class MinutelyForecastItem(base.AutoInit):
    time: datetime
    precip_intensity: float
    precip_intensity_error: float
    precip_intensity_probability: float
    precip_probability: float
    precip_type: str


class MinutelyForecast(base.BaseWeather):
    data: List[MinutelyForecastItem]
    data_class = MinutelyForecastItem


class HourlyForecastItem(base.AutoInit):
    time: datetime
    summary: str
    icon: str
    precip_intensity: float
    precip_probability: float
    precip_type: str
    temperature: float
    apparent_temperature: float
    dew_point: float
    humidity: float
    pressure: float
    wind_speed: float
    wind_gust: float
    wind_bearing: int
    cloud_cover: float
    uv_index: int
    visibility: float
    ozone: float


class HourlyForecast(base.BaseWeather):
    data: List[HourlyForecastItem]
    data_class = HourlyForecastItem


class DailyForecastItem(base.AutoInit):
    time: datetime
    summary: str
    icon: str
    sunrise_time: int
    sunset_time: int
    moon_phase: float
    precip_intensity: float
    precip_intensity_max: float
    precip_intensity_max_time: int
    precip_probability: float
    precip_type: str
    temperature_high: float
    temperature_high_time: int
    temperature_low: float
    temperature_low_time: int
    apparent_temperature_high: float
    apparent_temperature_high_time: int
    apparent_temperature_low: float
    apparent_temperature_low_time: int
    dew_point: float
    humidity: float
    pressure: float
    wind_speed: float
    wind_gust: float
    wind_gust_time: int
    wind_bearing: int
    cloud_cover: float
    uv_index: int
    uv_index_time: int
    visibility: int
    ozone: float
    temperature_min: float
    temperature_min_time: int
    temperature_max: float
    temperature_max_time: int
    apparent_temperature_min: float
    apparent_temperature_min_time: int
    apparent_temperature_max: float
    apparent_temperature_max_time: int


class DailyForecast(base.BaseWeather):
    data: List[DailyForecastItem]
    data_class = DailyForecastItem


class Alert(base.AutoInit):
    title: str
    time: datetime
    expires: datetime
    description: str
    uri: str


class Forecast(object):
    latitude: float
    longitude: float
    timezone: str
    currently: CurrentlyForecast
    minutely: MinutelyForecast
    hourly: HourlyForecast
    daily: DailyForecast
    alerts: List[Alert]

    def __init__(self, latitude: float, longitude: float, timezone: str,
        currently: dict={}, minutely: dict={}, hourly: dict={},
        daily: dict={}, alerts: [dict]=None, flags: [str]=None):
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone

        self.currently = CurrentlyForecast(**currently)
        self.minutely = MinutelyForecast(**minutely)
        self.hourly = HourlyForecast(**hourly)
        self.daily = DailyForecast(**daily)

        alerts = alerts or []
        self.alerts = [Alert(**item) for item in alerts]