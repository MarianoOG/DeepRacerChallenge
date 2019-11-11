def reward_function(params):
    # libraries
    import math
    
    # Read input parameters
    all_wheels_on_track = params["all_wheels_on_track"]
    x = params["x"]
    y = params["y"]
    distance_from_center = params["distance_from_center"]
    is_left_of_center = params["is_left_of_center"]
    heading = params["heading"]
    progress = params["progress"]
    steps = params["steps"]
    speed = params["speed"]
    steering_angle = params["steering_angle"]
    track_width = params["track_width"]
    waypoints = params["waypoints"]
    closest_waypoints = params["closest_waypoints"]
    
    # User defined params
    MAX_STEPS = 300 # Assuming is the max number of steps
    MAX_DIFF_ANGLE = 15.0
    BUFFER_FROM_CENTER = 0.8
    
    # Next and prev waypoint
    prev_point = waypoints[closest_waypoints[0]]
    next_point = waypoints[closest_waypoints[1]]
    
    # Initialize reward
    reward = 1.0
    
    # All wheels on track
    if(all_wheels_on_track):
    	reward *= 1.1
    else:
    	reward *= 0.5
    
    # If going in the middle
    if(distance_from_center<BUFFER_FROM_CENTER*track_width/2):
    	reward *= 1.2
    
    # Calculate the direction of track
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]) # in radians
    track_direction = math.degrees(track_direction) # in degrees
    
    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff
    
    # Penalize the reward if the difference is too large
    if direction_diff > MAX_DIFF_ANGLE:
        reward *= 0.5
    
    # Give reward per steps and 
    reward *= (1 + progress/100 - steps/MAX_STEPS)
        
    return float(reward)
