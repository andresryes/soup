from direction import Direction
import json
class Directorio:
    def __init__(self, soup):
        self.soup = soup
        self.arrayToPrint = []

    #init the process
    def init(self):
        return self.run(self.soup)

    #the method that actually make every parameter from Portal section
    def run(self, soup):
        result = []

        #Sort all emails alphabetically (href="mailto:arquitectura@ufm.edu") in a list, dump it to logs/4directorio_emails.txt
        result.append("Sort all emails alphabetically (href=\"mailto:arquitectura@ufm.edu\") in a list, dump it to logs/4directorio_emails.txt")
        emails = []
        for i in soup.find_all(attrs={"href":True}):
            if str(i['href']).__contains__("mailto"):
                emails.append(str(i['href'].replace("mailto:","")))
        emails.sort()
        #print(emails)
        f = open("../logs/4directorio_emails.txt","w+")
        for i in emails:
            f.write(i+"\r\n")
        result.append("---------------------------------------")

        #Count all emails that start with a vowel. (just display the count)
        count = 0
        for i in emails:
            if i[0] in ['a','e','i','o','u','A','E','I','O','U']:
                count = count+1
        result.append(f"Count all emails that start with a vowel. (just display the count): {count}")
        result.append("---------------------------------------")
        

        # Group in a JSON all rows that have Same Address (dont use Room number) as address, dump it to logs/4directorio_address.json
        result.append("Group in a JSON all rows that have Same Address (dont use Room number) as address, dump it to logs/4directorio_address.json")
        edificios = []
        tablaRaw = []
        #get all data from the tables 
        for i in soup.find_all(class_="tabla ancho100"):
            tablaRaw+=i.find_all('td')

        directions = []
        #looking for the parameters that I need, Building and Faculty
        for i in range(4,len(tablaRaw),5):
            #print(i.find_all('td'))
            #if (tablaRaw[i].text.split(",")[0]!="\n" and tablaRaw[i].text.split(",")[0].replace("\n","").replace(" ","") not in edificios):
             #   edificios.append(tablaRaw[i].text.split(",")[0])
                #print("--")
            #print(len(i.find_all('td')))
            #print(tablaRaw[i].text.split(",")[0].replace("\n","").replace(" ","")+".")
            

            #getting rid of the space in the first char of the string for the buildings
            name = tablaRaw[i].text.split(",")[0].replace("\n","")
            if name != "":
                if(name[0]==" "):
                    li = list(name)
                    li[0] = ""
                    name = "".join(li)

            #creating my direction object, setting attributes Faculty and Building for each one
            direction = Direction(tablaRaw[i-4].text.split(",")[0].replace("\n",""), name)

            #appends to directions list
            directions.append(direction)

            #append to edificios list if is not there
            if(name != "" and name not in edificios):
                edificios.append(name)
        #print(tablaRaw[9].text)
        #print(edificios)
        #print(directions[0].faculty)

        #creating the json data
        data = {}
        #loop in edificios
        for edificio in edificios:
            directionJson = []
            #for each edificio, iterate in all directions to find coincidences in the building
            for direc in directions:
                #if building in direction equals current edificio, append the jsonDirectionList
                if direc.building==edificio:
                    directionJson.append(direc.faculty)
            #setting the parameter in the json
            data[f'{edificio}'] = directionJson
        #print(json.dumps(data))

        #writing the file
        with open('../logs/4directorio_address.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        #print(len(soup.find_all(class_="tabla ancho100")))
        result.append("---------------------------------------")

        #Try to correlate in a JSON Faculty Dean and Directors, and dump it to logs/4directorio_deans.json

        return result