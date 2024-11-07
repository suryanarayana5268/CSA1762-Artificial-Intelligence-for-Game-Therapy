def vacuum_cleaner(room_status, start_position):
    position = start_position
    while 'dirty' in room_status.values():
        if room_status[position] == 'dirty':
            print(f"Cleaning room {position}...")
            room_status[position] = 'clean'
        else:
            print(f"Room {position} is already clean.")
        position = 'B' if position == 'A' else 'A'
        print(f"Moving to room {position}...")
    print("All rooms are clean!")
room_status = {'A': 'clean', 'B': 'dirty'}
start_position = 'A'
vacuum_cleaner(room_status, start_position)
