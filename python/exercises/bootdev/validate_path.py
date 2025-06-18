def validate_path(expected_path, character_path):
    character_name = character_path.pop(0)
    total_waypoints = len(expected_path)
    correct_waypoints = 0

    for i in range (len(expected_path)):
        if character_path[i] == expected_path[i]:
            correct_waypoints += 1

    return character_name, (correct_waypoints/total_waypoints) * 100
            
            
