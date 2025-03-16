import turtle
import time
import math

# Screen setup
turtle.setup(600, 600)
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0, 0)

def prime_branching(n):
    """ Returns a deterministic phase-locking ratio based on prime number logic """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # Add more if needed
    return primes[n % len(primes)] / primes[(n+1) % len(primes)]

def draw_structured_lightning(x, y, length, angle, depth=0):
    """ Recursively generates structured lightning based on prime harmonic ratios """
    if depth > 7:  # Limit recursion depth
        return
    
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("yellow")
    turtle.width(max(1, 3 - depth * 0.3))  # Decrease width over depth
    
    # Compute structured offsets using prime ratios
    x_offset = length * prime_branching(depth) * math.cos(math.radians(angle))
    y_offset = length * prime_branching(depth) * math.sin(math.radians(angle))
    
    new_x, new_y = x + x_offset, y - y_offset
    turtle.goto(new_x, new_y)
    
    # Recursive structured bifurcation
    draw_structured_lightning(new_x, new_y, length * 0.7, angle - 20, depth + 1)
    draw_structured_lightning(new_x, new_y, length * 0.7, angle + 20, depth + 1)

def lightning_effect():
    """ Clears the screen and redraws structured lightning at intervals """
    while True:
        turtle.clear()
        draw_structured_lightning(0, 200, 30, -90)
        turtle.update()
        time.sleep(1)

def main():
    lightning_effect()
    turtle.done()

turtle.Screen().title("Structured Lightning - Prime Resonance")
main()