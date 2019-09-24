import sys
from portal import Portal
from estudios import Estudios
from cs import CS
from directorio import Directorio
from request import Request
#print ('Argument List:', str(sys.argv))

#Instance of request class, in order to DRY
request = Request()

#main class to verify args from running process
def main(args):
    #print(args)
    #print(args.__contains__("1"))

    #array to set the print result
    result = [""]

    #call the correct methods according to the args
    if len(args) == 0:
        result = runAll(result)
    elif args.__contains__("1"):
        result = portal(result)
    elif args.__contains__("2"):
        result = estudios(result)   
    elif args.__contains__("3"):
        result = cs(result)  
    elif args.__contains__("4"):
        result = directorio(result)  
    printResult(result)

#portal method that instances the Portal class and run it
def portal(result):
    res = []
    res.append("=============================")
    res.append("1. Portal")
    portalSoup = request.makeGet("http://ufm.edu/Portal")
    por = Portal(portalSoup)
    portalArray = por.init()
    #print(portalArray)
    res = res + portalArray
    return res

#estudios method that instances the Estudios class and run it
def estudios(result):
    res = []
    res.append("=============================")
    res.append("2. Estudios")
    soup = request.makeGet("http://ufm.edu/Portal")
    soup = request.makeGet("http://ufm.edu"+soup.find(id="menu-table").find_all(class_="menu-key")[0].a['href'])
    #soup = request.makeGet("http://ufm.edu/Estudios")
    estudios = Estudios(soup)
    estudiosArray = estudios.init()
    res += estudiosArray
    return res

#cs method 
def cs(result):
    res = []
    res.append("=============================")
    res.append("3. CS")
    soup = request.makeGet("https://fce.ufm.edu/carrera/cs/")
    cs = CS(soup)
    csArray = cs.init()
    res += csArray
    return res

#directorio method 
def directorio(result):
    res = []
    res.append("=============================")
    res.append("4. Directorio")
    soup = request.makeGet("https://www.ufm.edu/Directorio")
    directorio = Directorio(soup)
    dirArray = directorio.init()
    res += dirArray
    return res

#method defined if no args set
def runAll(result):
    result += portal(result)
    result += estudios(result)
    result += cs(result)
    result += directorio(result)
    return result

#method to print results 
def printResult(result):
    result.insert(0, "Enrique Andres Bolanos Reyes")
    for i in result:
        print(i)

#main method in which I get the args from the running process
if __name__ == "__main__":
   main(sys.argv[1:])
