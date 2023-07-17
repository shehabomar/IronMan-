import turtle 


# Coordinates of the face
face_one = [
  [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),(-40, -20), (0, -20)],

  [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),(40, 120), (0, 120)]
]

face_two = [
  [(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),(-80, -230), (-64, -210), (0, -210)],
  
  [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),(100, -46), (50, -40), (40, -30), (0, -30)]
]

face_three = [
  [(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),(0, -250)],
  
  [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220),(0,-220)]
]

# Hide the Cursor
turtle.hideturtle()

# Setting up the background
turtle.bgcolor("red")
turtle.setup(500,600)

# Assigning the values of the start points
face_one_start = (0,120)
face_two_start = (0,-30)
face_three_start = (0,-220)

# Adjusting the speed of the drawing
turtle.speed(2)

# A function to draw each face based on its coordinates and its starting point
def draw_face(face_details_list,start_point):
    
    turtle.penup()
    
    turtle.goto(start_point)

    turtle.pendown()

    turtle.color("yellow")

    turtle.begin_fill()

    for i in range(len(face_details_list[0])):
        x, y = face_details_list[0][i]
        turtle.goto(x, y)
    
    for i in range(len(face_details_list[1])):
        x, y = face_details_list[1][i]
        turtle.goto(x, y)
    
    turtle.end_fill()

# Calling the function to draw the faces
draw_face(face_one, face_one_start)

draw_face(face_two, face_two_start)

draw_face(face_three, face_three_start)
