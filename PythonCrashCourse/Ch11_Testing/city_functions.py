import typing

def format_location(city: str, country: str) -> str:
    res = city.title() + ', ' + country.title()
    return res