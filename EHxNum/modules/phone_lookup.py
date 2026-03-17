import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def lookup(number):

    parsed = phonenumbers.parse(number)

    data = {}

    data["country"] = geocoder.description_for_number(parsed, "en")
    data["carrier"] = carrier.name_for_number(parsed, "en")
    data["timezone"] = timezone.time_zones_for_number(parsed)
    data["valid"] = phonenumbers.is_valid_number(parsed)

    return data
