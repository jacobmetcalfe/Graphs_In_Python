# FILE SCRAPING
import json

# PLOT MAP
import turtle

# GRAB URL DATA
import urllib.request

# TIME OF PASSOVER
import time

# URL CONSTANT
URL = 'http://api.open-notify.org/astros.json'
URL_ISS = 'http://api.open-notify.org/iss-now.json'
URL_PASSOVER = 'http://api.open-notify.org/iss-pass.json'

# OPEN URL
response = urllib.request.urlopen(URL)
response_ISS = urllib.request.urlopen(URL_ISS)

# LOAD IN JSON FILE FROM URL
result = json.loads(response.read())
result_ISS = json.loads(response_ISS.read())

# PRINTS VALUE ASSOCIATED WITH KEY
# print('People in Space: ', result['number'])
# print('Latitude:', result_ISS['iss_position']) 

people = result['people']
location = result_ISS['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])

def time_of_passover(city, passover_time):
  print(city + ': ' + time.ctime(passover_time))

# PRINT SAT COORDINATES
print('ISS COORDINATES')
print('---------------')
print('Longitude:', lon)
print('Latitude:' , lat)

print('\n')

# PRINTS ALL PEOPLE ABOARD
print('People in Space')
print('---------------')
for person in people:
  print(person['name'] + ': ' + person['craft'])
print('\n')

# SCREEN SETUP
map = turtle.Screen()
map.setup(720, 360)
map.setworldcoordinates(-180, -90, 180, 90)
map.bgpic('map.gif')

# MARK THE SATELLITE WITH SHAPE
map.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

print("Program using API's that tells you the next passover time of the ISS")
print('--------------------------------------------------------------------')

# SPACE CENTER: USER
place = input('What is your city name: ')
user_lat = input('Please enter the latitude: ')
user_lon = input('Please enter the longitude: ')

user_Loc = turtle.Turtle()
user_Loc.penup()
user_Loc.color('yellow')
user_Loc.goto(user_lon, user_lat)
user_Loc.dot(5)
user_Loc.hideturtle()

# PASSOVER TIME: USER
URL_USER = URL_PASSOVER + '?lat=' + str(float(user_lat)) + '&lon=' + str(float(user_lon))
response_user = urllib.request.urlopen(URL_USER)
result_user = json.loads(response_user.read())

overtime = result_user['response'][1]['risetime']

style = ('Arial', 4, 'bold')
user_Loc.color('yellow')
user_Loc.write(time.ctime(overtime), font=style)
time_of_passover(place, overtime)

# SPACE CENTER: NASA
nasa_lat = 29.5502
nasa_lon = -95.097

nasa_Loc = turtle.Turtle()
nasa_Loc.penup()
nasa_Loc.color('red')
nasa_Loc.goto(nasa_lon, nasa_lat)
nasa_Loc.dot(5)
nasa_Loc.hideturtle()

# PASSOVER TIME: NASA
place = 'NASA'
URL_NASA = URL_PASSOVER + '?lat=' + str(float(nasa_lat)) + '&lon=' + str(float(nasa_lon))
response_nasa = urllib.request.urlopen(URL_NASA)
result_nasa = json.loads(response_nasa.read())

overtime = result_nasa['response'][1]['risetime']

style = ('Arial', 4, 'bold')
nasa_Loc.color('red')
nasa_Loc.write(time.ctime(overtime), font=style)
time_of_passover(place, overtime)

# SPACE CENTER: COLORADO SPRINGS
cos_lat = 38.833881
cos_lon = -104.821365

cos_Loc = turtle.Turtle()
cos_Loc.penup()
cos_Loc.color('yellow')
cos_Loc.goto(cos_lon, cos_lat)
cos_Loc.dot(5)
cos_Loc.hideturtle()

# PASSOVER TIME: COLORADO SPRINGS
place = 'Colorado Springs'
URL_COS = URL_PASSOVER + '?lat=' + str(float(cos_lat)) + '&lon=' + str(float(cos_lon))
response_cos = urllib.request.urlopen(URL_COS)
result_cos = json.loads(response_cos.read())

overtime = result_cos['response'][1]['risetime']

style = ('Arial', 4, 'bold')
cos_Loc.color('yellow')
cos_Loc.write(time.ctime(overtime), font=style)
time_of_passover(place, overtime)
