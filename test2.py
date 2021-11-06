import xml.etree.ElementTree as ET

def timestamps_by_description(xml, description):
    root = ET.fromstring(xml) 
    _timestamps = []
    for child in root: 
        _description = child.find('description').text
        if(description == _description):
            _timestamps.append(int(child.get('timestamp')))

    return _timestamps

xml = """<?xml version="1.0" encoding="UTF-8"?>
<log>
    <event timestamp="1614285589">
        <description>Intrusion detected</description>
    </event>
    <event timestamp="1614286432">
        <description>Intrusion ended</description>
    </event>
</log>"""

print(timestamps_by_description(xml, 'Intrusion ended'))
