import turtle

def create_turtle_image(filename):
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    t.color("black")

    for i in range(36):
        t.forward(200)
        t.right(170)

    screen.getcanvas().postscript(file=filename + ".eps")
    # Convert EPS to PNG
    try:
        from PIL import Image
        img = Image.open(filename + ".eps")
        img.save(filename + ".png")
        img.close()
    except ImportError:
        print("PIL module not found. Please install Pillow to convert EPS to PNG.")

    turtle.bye()

if __name__ == "__main__":
    create_turtle_image("turtle_image")