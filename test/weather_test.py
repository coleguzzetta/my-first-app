# this is the "test/weather_test.py" file...

from app.weather import forecast_demo


def test_forecast_demo():
    assert forecast_demo == 202
