from turtle import Screen
from timmy import Timmy
from level_counter import Levels
from cars_generator import Cars
import time


def main() -> None:
    screen = Screen()


    screen.setup(width = 600, height = 600)
    screen.tracer(0)
    screen.title("Crossy Road - Python Version")
    screen.listen()
    screen.colormode(255)

    timmy = Timmy()
    levels = Levels()
    cars = Cars()

    screen.onkey(fun = timmy.move, key = "space")

    levels.update()
    screen.update()
    game_is_on = True
    while game_is_on:
        time.sleep(0.05)
        cars.new_car_line()
        cars.move_cars()
        
        
        # Detect collisions with car
        for each in cars.repository:
            if timmy.distance(each) < 20:
                levels.game_over()
                game_is_on = False
        
        # Detect finishing a level
        if timmy.ycor() > 280:
            timmy.reset_position()
            levels.level_count += 1
            levels.update()
            
            cars.increase_speed()
        
        # Remove excessive cars to save performance
        cars.remove_excessive()
        screen.update()
        
    screen.exitonclick()

if __name__ == "__main__":
    main()