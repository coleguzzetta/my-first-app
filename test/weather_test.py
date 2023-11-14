# this is the "test/weather_test.py" file...

from app.weather import weather_data


def test_weather_data():
    weather = weather_data()

    assert isinstance(weather, list)
    assert len(weather) == 7
    assert isinstance(weather[0], dict)
    assert list(weather[0].keys()) == ['number', 'name', 'startTime', 'endTime', 'isDaytime', 'temperature', 'temperatureUnit', 'temperatureTrend', 'probabilityOfPrecipitation', 'dewpoint', 'relativeHumidity', 'windSpeed', 'windDirection', 'icon', 'shortForecast', 'detailedForecast']