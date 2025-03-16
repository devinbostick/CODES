import turtle
import random
import time
import math

# Screen setup
turtle.setup(600, 600)
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0, 0)

def draw_lightning(x, y, length, angle):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("yellow")
    turtle.width(3)
    
    for _ in range(random.randint(5, 10)):
        x += length * random.uniform(0.6, 1.0) * random.choice([-1, 1])
        y -= length * random.uniform(0.6, 1.0)
        angle += random.uniform(-30, 30)
        turtle.goto(x, y)

def draw_ripples(x, y, max_radius):
    """Draws expanding ripples from the (x, y) point."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white", "blue")  # Ripple color with fill for intensity
    turtle.width(2)
    
    for radius in range(10, max_radius, 5):
        turtle.setheading(0)
        turtle.circle(radius)
        turtle.fillcolor((random.random(), random.random(), random.random()))  # Random fill color for effect

def lightning_effect():
    while True:
        turtle.clear()
        
        # Draw lightning with ripple effects
        draw_lightning(0, 200, 20, -90)
        
        # Simulate a **thunderstorm** vibe
        draw_ripples(0, 200, 150)
        
        turtle.update()
        time.sleep(random.uniform(0.3, 1.0))  # Faster and more dramatic bursts

def main():
    lightning_effect()
    turtle.done()  # This keeps the Turtle window open after the animation ends

main()