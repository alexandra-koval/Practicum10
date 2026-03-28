import turtle
import random

turtle.setup(1000, 700)
turtle.bgcolor("darkblue")
turtle.title("Городской силуэт")
turtle.tracer(0)
turtle.speed(0)
turtle.hideturtle()


def draw_star(x_coordinate, y_coordinate, star_size):
    """Draws a single star"""
    turtle.up()
    turtle.goto(x_coordinate, y_coordinate)
    turtle.down()
    turtle.color("gold")
    turtle.dot(star_size)


def draw_stars():
    """Draws a starry sky"""
    for _ in range(120):
        x_coordinate = random.randint(-480, 480)
        y_coordinate = random.randint(0, 320)
        star_size = random.choice([2, 3, 4])
        draw_star(x_coordinate, y_coordinate, star_size)


def draw_moon():
    """Draws the moon"""
    turtle.up()
    turtle.goto(350, 280)
    turtle.down()
    turtle.color("gold")
    turtle.begin_fill()
    turtle.circle(35)
    turtle.end_fill()


def draw_rectangular_building(
    x_coordinate, y_coordinate, building_width, building_height
):
    """Draws a rectangular building (black)"""
    turtle.up()
    turtle.goto(x_coordinate, y_coordinate)
    turtle.down()
    turtle.color("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(building_width)
        turtle.left(90)
        turtle.forward(building_height)
        turtle.left(90)
    turtle.end_fill()


def draw_triangle_roof(
    x_coordinate, y_coordinate, building_width, building_height
):
    """Draws a triangular roof (black)"""
    turtle.up()
    turtle.goto(x_coordinate, y_coordinate + building_height)
    turtle.down()
    turtle.color("black")
    turtle.begin_fill()
    roof_peak_y = y_coordinate + building_height + building_width / 3
    turtle.goto(x_coordinate + building_width / 2, roof_peak_y)
    turtle.goto(x_coordinate + building_width, y_coordinate + building_height)
    turtle.goto(x_coordinate, y_coordinate + building_height)
    turtle.end_fill()


def draw_window(x_coordinate, y_coordinate, window_size, is_lit):
    """Draws a square window"""
    turtle.up()
    turtle.goto(x_coordinate, y_coordinate)
    turtle.down()
    if is_lit:
        turtle.color("yellow")
    else:
        turtle.color("darkgray")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(window_size)
        turtle.left(90)
    turtle.end_fill()


def draw_windows(x_coordinate, y_coordinate, building_width, building_height):
    """Draws windows on a building"""
    window_size = random.randint(5, 7)

    number_of_floors = building_height // 35
    windows_per_floor = building_width // (window_size + 12)

    if number_of_floors < 1:
        number_of_floors = 1
    if windows_per_floor < 1:
        windows_per_floor = 1

    margin_x = (
        (building_width - window_size * windows_per_floor)
        // (windows_per_floor + 1)
    )
    margin_y = (
        (building_height - window_size * number_of_floors)
        // (number_of_floors + 1)
    )

    for floor in range(number_of_floors):
        for window_number in range(windows_per_floor):
            window_x = (
                x_coordinate + margin_x
                + window_number * (window_size + margin_x)
            )
            window_y = (
                y_coordinate + margin_y
                + floor * (window_size + margin_y)
            )
            is_lit = random.random() < 0.4
            draw_window(window_x, window_y, window_size, is_lit)


def draw_city():
    """Draws the city skyline (all buildings are black)"""

    ground_y = -340

    buildings = [
        (-500, 55, 150, 1),
        (-445, 60, 170, 2),
        (-385, 65, 190, 1),
        (-320, 70, 210, 2),
        (-250, 55, 140, 1),
        (-195, 75, 230, 2),
        (-120, 65, 200, 1),
        (-55, 70, 220, 2),
        (15, 80, 260, 1),
        (95, 65, 190, 2),
        (160, 85, 290, 1),
        (245, 55, 130, 1),
        (300, 70, 180, 2),
        (370, 60, 160, 1),
        (430, 55, 145, 2),
        (485, 50, 120, 1),
    ]

    current_x = -500
    for building_info in buildings:
        building_width = building_info[1]
        building_height = building_info[2]
        roof_type = building_info[3]

        draw_rectangular_building(
            current_x, ground_y, building_width, building_height
        )
        draw_windows(
            current_x, ground_y, building_width, building_height
        )

        if roof_type == 2:
            draw_triangle_roof(
                current_x, ground_y, building_width, building_height
            )

        current_x = current_x + building_width


def draw_ground():
    """Draws the ground line"""
    turtle.up()
    turtle.goto(-500, -340)
    turtle.down()
    turtle.color("gray")
    turtle.pensize(2)
    turtle.goto(500, -340)


def draw_city_silhouette():
    """Draws the complete city silhouette"""
    draw_city()
    draw_ground()
    draw_moon()
    draw_stars()
    turtle.update()


draw_city_silhouette()
turtle.mainloop()
