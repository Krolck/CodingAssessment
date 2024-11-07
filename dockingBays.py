# dockingBays.py

# List of docking bays at the space station
# Each bay is represented as a dictionary with an ID, size, and current schedule

# Sizes can be 'small', 'medium', 'large'

docking_bays = [
    {
        'bay_id': 1,
        'size': 'small',
        'schedule': []  # list of (arrival_time, departure_time, ship_name) tuples
    },
    {
        'bay_id': 2,
        'size': 'small',
        'schedule': []
    },
    {
        'bay_id': 3,
        'size': 'medium',
        'schedule': []
    },
    {
        'bay_id': 4,
        'size': 'medium',
        'schedule': []
    },
    {
        'bay_id': 5,
        'size': 'large',
        'schedule': []
    },
    {
        'bay_id': 6,
        'size': 'large',
        'schedule': []
    }
]

# Example ships with size requirements and docking times
# Each ship is a dictionary with a name, size requirement, and desired docking time

incoming_ships = [
    {
        'ship_name': 'Shuttle Alpha',
        'size': 'small',
        'arrival_time': '12:00',
        'departure_time': '14:00'
        
    },
    {
        'ship_name': 'Freighter Beta',
        'size': 'medium',
        'arrival_time': '13:00',
        'departure_time': '15:00'
    },
    {
        'ship_name': 'Cruiser Gamma',
        'size': 'large',
        'arrival_time': '14:00',
        'departure_time': '18:00'
    },
    {
        'ship_name': 'Shuttle Delta',
        'size': 'small',
        'arrival_time': '15:00',
        'departure_time': '17:00'
    },
    {
        'ship_name': 'Freighter Epsilon',
        'size': 'medium',
        'arrival_time': '16:00',
        'departure_time': '18:00'
    },
    {
        'ship_name': 'Cruiser Zeta',
        'size': 'large',
        'arrival_time': '10:00',
        'departure_time': '12:00'
    }
]

# Existing bookings in the docking bays
docking_bays[0]['schedule'] = [
    ('10:00', '12:00', 'Maintenance A'),
    ('16:00', '18:00', 'Maintenance B')
]  # Bay 1

docking_bays[2]['schedule'] = [
    ('11:00', '13:00', 'Supply Drop')
]  # Bay 3

docking_bays[4]['schedule'] = [
    ('14:00', '16:00', 'Repair C')
]  # Bay 5
