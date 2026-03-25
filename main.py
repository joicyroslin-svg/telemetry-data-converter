def convertFromFormat1(location_str):
    """
    Splits the given location string using '/' and maps it to country,
    city, area, factory, and section.
    
    Parameters:
    location_str (str): The location string formatted as 'country/city/area/factory/section'.
    
    Returns:
    dict: A dictionary containing the mapped location components.
    """
    components = location_str.split('/')
    location_mapping = {
        'country': components[0] if len(components) > 0 else None,
        'city': components[1] if len(components) > 1 else None,
        'area': components[2] if len(components) > 2 else None,
        'factory': components[3] if len(components) > 3 else None,
        'section': components[4] if len(components) > 4 else None,
    }
    return location_mapping

def convertFromFormat2(iso_timestamp):
    """
    Parses the given ISO 8601 timestamp and converts it to milliseconds.
    
    Parameters:
    iso_timestamp (str): The ISO 8601 timestamp.
    
    Returns:
    int: The timestamp in milliseconds since epoch.
    """
    from datetime import datetime
    dt = datetime.fromisoformat(iso_timestamp)
    return int(dt.timestamp() * 1000)

# Unit Tests
import unittest

class TestConversionFunctions(unittest.TestCase):
    def test_convertFromFormat1(self):
        self.assertEqual(convertFromFormat1('USA/New York/NY/FactoryA/Section1'), \
            {'country': 'USA', 'city': 'New York', 'area': 'NY', 'factory': 'FactoryA', 'section': 'Section1'})
        self.assertEqual(convertFromFormat1('Canada/Vancouver'), \
            {'country': 'Canada', 'city': 'Vancouver', 'area': None, 'factory': None, 'section': None})

    def test_convertFromFormat2(self):
        self.assertEqual(convertFromFormat2('2026-03-25T13:25:17'), 1679750717000)
        self.assertEqual(convertFromFormat2('2021-01-01T00:00:00'), 1609459200000)

if __name__ == '__main__':
    unittest.main()