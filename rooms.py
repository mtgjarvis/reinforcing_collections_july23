room = {
    'data': {'rooms': [{'id': 1, 'room_number': "201", 'capacity': 50},
                       {'id': 2, 'room_number': "301", 'capacity': 200},
                       {'id': 3, 'room_number': "1B", 'capacity': 100}
                       ],
             'events': [{'id': 1, 'room_id': 2, 'start_time': 18, 'end_time': 20, 'attendees': 75},
                        {'id': 2, 'room_id': 1, 'start_time': 10, 'end_time': 18, 'attendees': 25},
                        {'id': 3, 'room_id': 2, 'start_time': 10, 'end_time': 18, 'attendees': 20},
                        {'id': 4, 'room_id': 3, 'start_time': 18, 'end_time': 21, 'attendees': 56},
                       ]
             }
        }

room201 = room['data']['rooms'][0]['room_number']
print(room201)


def get_capacity():
    room_201_capacity = room['data']['rooms'][0]['capacity']
    return room_201_capacity


print(get_capacity())

data_set = room['data']['events']
for item in data_set:
    if item['room_id'] == 1:
        if item['attendees'] <= get_capacity():
            print("you're booked")
        else:
            print("You're booked")