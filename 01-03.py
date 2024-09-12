# Ball pit program

# -------------------------
# Subprograms
# -------------------------
# Function to return the volume of the ball pit
def ball_pit_volume(ball_pit_radius, ball_pit_height):
    pi = 3.14
    return pi * (ball_pit_radius * ball_pit_radius) * ball_pit_height


# Function to return the volume of a ball
def ball_volume(ball_radius):
    pi = 3.14
    return (4 / 3) * pi * (ball_radius * ball_radius * ball_radius)


# -------------------------
# Main program
# -------------------------
ball_pit_radius = float(input("Enter the radius of the ball pit in meters: "))  # Meters
ball_pit_height = float(input("Enter the height of the ball pit in meters: "))  # Meters
ball_radius = float(input("Enter the radius of one ball in meters: "))  # Meters
packing_density = 0.75  # Volume taken up by the balls
balls = (ball_pit_volume(ball_pit_radius, ball_pit_height) / ball_volume(ball_radius)) * packing_density
balls = int(balls) + 1
print("You need", balls, "balls to fill the ball pit.")
