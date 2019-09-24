import sys
from portal import Portal
from estudios import Estudios
from cs import CS
from directorio import Directorio
from request import Request

def test_addition():
  assert 1 + 1 == 2

request = Request()

def test_portal():
    res = []
    res.append("=============================")
    res.append("1. Portal")
    portalSoup = request.makeGet("http://ufm.edu/Portal")
    por = Portal(portalSoup)
    return res

#estudios method that instances the Estudios class and run it
def test_estudios():
    res = []
    res.append("=============================")
    res.append("2. Estudios")
    soup = request.makeGet("http://ufm.edu/Portal")
    soup = request.makeGet("http://ufm.edu"+soup.find(id="menu-table").find_all(class_="menu-key")[0].a['href'])
    #soup = request.makeGet("http://ufm.edu/Estudios")
    estudios = Estudios(soup)
    return res

#cs method 
def test_cs():
    res = []
    res.append("=============================")
    res.append("3. CS")
    soup = request.makeGet("https://fce.ufm.edu/carrera/cs/")
    cs = CS(soup)
    return res

#directorio method 
def test_directorio():
    res = []
    res.append("=============================")
    res.append("4. Directorio")
    soup = request.makeGet("https://www.ufm.edu/Directorio")
    directorio = Directorio(soup)
    return res