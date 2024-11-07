# main.py
bays_schedules = {}

import dockingBays as db

# Function to print docking bays information
def print_docking_bays():
    print("Docking Bays:")
    for bay in db.docking_bays:
        print(f"Bay {bay['bay_id']} - Size: {bay['size']}, Schedule: {bay['schedule']}")

# Function to print incoming ships information
def print_incoming_ships():
    print("\nIncoming Ships:")
    for ship in db.incoming_ships:
        print(f"Ship {ship['ship_name']} - Size: {ship['size']}, Arrival: {ship['arrival_time']}, Departure: {ship['departure_time']}")

def print_new_schedule():
    for bay in db.docking_bays:
        schedule = []
        bay_id = bay['bay_id']
        for i, time in enumerate(bay['schedule']):
            arrive_int = bays_schedules[str(bay_id)][i][0]
            depart_int = bays_schedules[str(bay_id)][i][1]
            arrive_meridium = ""
            depart_meridium = ""
            if arrive_int < 12:
                arrive_meridium = "PM"
            else:
                if arrive_int != 12:
                    arrive_meridium = "AM"
                    arrive_int -= 12
                else:
                    arrive_meridium = "AM"


            if depart_int < 12:
                depart_meridium = "PM"
            else:

                if depart_int != 12:
                    depart_meridium = "AM"
                    depart_int -= 12
                else:
                    depart_meridium = "AM"

            schedule.append(f"{time[2]} - {arrive_int} {arrive_meridium} to {depart_int} {depart_meridium}")
        print(f"Bay {bay_id}: {' | '.join(schedule)} ")
        
# Function to match ship size requirements (Decaprecated)
# def match_ship_size(ship):
#     for docking_bay in db.docking_bays:
#         if docking_bay.get("size") == ship.get("size"):
#             return docking_bay


def convert_ship_time(ship):
    ship_arrive_hour = 0
    ship_departure_hour = 0
        # Get ship arrival ints to use in calculations

    if ship['arrival_time'][2] == ":":
        ship_arrive_hour = int(ship['arrival_time'][:2])
    else:
        ship_arrive_hour = int(ship['arrival_time'][0])

    # Get ship depart ints to use in calculations
    if ship['departure_time'][2] == ":":
        ship_departure_hour = int(ship['departure_time'][:2])
    else:
        ship_departure_hour = int(ship['departure_time'][0])
    return ship_arrive_hour, ship_departure_hour

# Get docking schedule ints for calculations
def convert_docking_time(docking_bay):
    bays_schedules[str(docking_bay['bay_id'])] = []
    bay = bays_schedules[str(docking_bay['bay_id'])]

    for i, time in enumerate(docking_bay['schedule']):
        bay.append([])

        if time[0][2] == ":":
            bay[i].append(int(time[0][:2]))
        else:
            bay[i].append(int(time[0][1]))
        if time[1][2] == ":":
            bay[i].append(int(time[1][:2]))
        else:
            bay[i].append(int(time[1][1]))


def match_ships(ship):
    # This will be used to assign priority
    possible_bays = []
    ship_arrive_hour, ship_departure_hour = convert_ship_time(ship)


    for i, v in enumerate(bays_schedules):
        bay_time = bays_schedules[str(v)] 
        bay = db.docking_bays[i]

        #if ship is not right size go to next bay
        if ship['size'] != bay['size']: continue

        #if schedule is empty, add to possible bays
        if not bay_time:
            possible_bays.append(bay)
            continue

        #if there is space, add to possible bays
        for times in bay_time:
            if ship_arrive_hour > times[1] or ship_departure_hour < times[0]:
                possible_bays.append(bay)
                break
    # Assign bay to bay that has the least times in its schedule
    if possible_bays:
        min_bay = possible_bays[0] 
        for bay in possible_bays:
            if len(bay['schedule']) < len(min_bay['schedule']):
                min_bay = len(bay['schedule'])
        bays_schedules[str(bay['bay_id'])].append([ship_arrive_hour, ship_departure_hour])
        bay['schedule'].append((ship['arrival_time'], ship['departure_time'], ship['ship_name']))


    # for docking_bay in db.docking_bays:
    #     if docking_bay.get("size") == ship.get("size"):
    #         return docking_bay

# Main function
def main():

    # print_docking_bays()
    # print_incoming_ships()
    
    for bay in db.docking_bays:
        convert_docking_time(bay)

    for ship in db.incoming_ships:
        match_ships(ship)
    print_new_schedule()


if __name__ == "__main__":
    main()

