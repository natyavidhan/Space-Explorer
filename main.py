from flask import Flask, render_template, request, redirect, url_for
import json
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/planets')
def planets():
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    details = json.load(open('planets.json'))
    return render_template('planets.html', planets = planets, details=details)

@app.route('/solar-system')
def ss():
    return render_template('solar system.html')

@app.route('/celestial-objects')
def co():
    objects = {
        "Asteroids": "https://img.icons8.com/cotton/64/000000/asteroid.png",
        "Meteorite": "https://img.icons8.com/external-vitaliy-gorbachev-lineal-color-vitaly-gorbachev/60/000000/external-meteorite-museum-vitaliy-gorbachev-lineal-color-vitaly-gorbachev.png",
        "Comet": "https://img.icons8.com/external-vitaliy-gorbachev-lineal-color-vitaly-gorbachev/60/000000/external-comet-space-vitaliy-gorbachev-lineal-color-vitaly-gorbachev.png",
        "Stars": "https://img.icons8.com/external-vitaliy-gorbachev-lineal-vitaly-gorbachev/60/000000/external-stars-location-vitaliy-gorbachev-lineal-vitaly-gorbachev.png",
        "Satellite":"https://img.icons8.com/dusk/64/000000/full-moon--v1.png" ,
        "Galaxies": "https://img.icons8.com/ultraviolet/40/000000/galaxy.png",
        "Planets": "https://img.icons8.com/external-wanicon-lineal-color-wanicon/64/000000/external-planets-space-wanicon-lineal-color-wanicon.png"
    }
    return render_template('celestial objects.html', objects=objects)

@app.route('/celestial-objects/<objectName>')
def co_objects(objectName):
    details = json.load(open('objects.json', encoding="utf8"))
    objectName = objectName.lower()
    for i in details:
        if objectName in i['name'].lower():
            return render_template('objects.html', object=i)
    return redirect('/')

@app.route('/fact/api')
def factAPI():
    doc = requests.get("https://fungenerators.com/random/facts/space/").text
    soup = BeautifulSoup(doc, 'html.parser')
    fact = soup.find('h2', attrs = {'class':'wow'}).text
    return fact

@app.route('/fact')
def fact():
    return render_template('fact.html')
        

if __name__ == '__main__':
    app.run(debug=True)
    

"""
refrences:
#https://www.space.com/16080-solar-system-planets.html
"""