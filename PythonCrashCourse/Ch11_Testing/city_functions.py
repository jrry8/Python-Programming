import typing

def format_location(city: str, country: str, population: int = None) -> str:
    res = city.title() + ', ' + country.title()
    if population:
        res += ' - population ' + str(population) 
    return res