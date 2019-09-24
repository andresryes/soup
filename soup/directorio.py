from direction import Direction
from entity import Entity
import json
import csv

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
            faculty = tablaRaw[i-4].text.split(",")[0].replace("\n","")
            phone = tablaRaw[i-2].text.split(",")[0].replace("\n","")
            if name != "":
                if(name[0]==" "):
                    li = list(name)
                    li[0] = ""
                    name = "".join(li)
            if faculty != "":
                if(faculty[0]==" "):
                    li = list(faculty)
                    li[0] = ""
                    faculty = "".join(li)
            #creating my direction object, setting attributes Faculty and Building for each one
            direction = Direction(faculty, name, phone)

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
        result.append("Try to correlate in a JSON Faculty Dean and Directors, and dump it to logs/4directorio_deans.json")
        tablaRaw = []
        entities = []
        tab = soup.find_all(class_="tabla ancho100 col3")
        for i in range(1,len(tab),1):
            tablaRaw+=tab[i].find_all('td')

        for i in range(2, len(tablaRaw), 3):
            fac = tablaRaw[i-2].text
            name = tablaRaw[i-1].text
            mail = tablaRaw[i].text
            if name != "":
                if(name[0]==" "):
                    li = list(name)
                    li[0] = ""
                    name = "".join(li)
            if fac != "":
                if(fac[0]==" "):
                    li = list(fac)
                    li[0] = ""
                    fac = "".join(li)    
            mail = mail.replace(" ","").strip()  
            #print(mail+".")   
            entity = Entity(fac, name, mail)
            entities.append(entity)
            #print(tablaRaw[i].text)
        data = {}
        for e in entities:
            for d in directions:
                if e.faculty.replace("Facultad de ","").replace("Instituto de ","") == d.faculty:
                    e.phone = d.phone
            data[f'{e.faculty}'] = {
                "Dean/Director" : e.name,
                "email" : e.mail,
                "Phone number" : e.phone
                }
        
        with open('../logs/4directorio_deans.json', 'w+', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        result.append("---------------------------------------")

        #GET the directory of all 3 column table and generate a CSV with these columns (Entity,FullName, Email), and dump it to logs/4directorio_3column_tables.csv
        result.append("GET the directory of all 3 column table and generate a CSV with these columns (Entity,FullName, Email), and dump it to logs/4directorio_3column_tables.csv")
        
        #get the table in which the entities are
        tab = soup.find_all(class_="tabla ancho100 col3")[0]

        #defined the list
        
        for i in range(2, len(tablaRaw), 3):
            fac = tablaRaw[i-2].text
            name = tablaRaw[i-1].text
            mail = tablaRaw[i].text
            if name != "":
                if(name[0]==" "):
                    li = list(name)
                    li[0] = ""
                    name = "".join(li)
            if fac != "":
                if(fac[0]==" "):
                    li = list(fac)
                    li[0] = ""
                    fac = "".join(li)    
            mail = mail.replace(" ","").strip()  
            #print(mail+".")   
            entity = Entity(fac, name, mail)
            entities.append(entity)
            #print(tablaRaw[i].text)

        with open('../logs/4directorio_3column_tables.csv', 'w+') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['Text','href'])
            for i in soup.find_all('a'):
                filewriter.writerow([i.text.strip(), i["href"].strip()])        
        
        result.append("---------------------------------------")
        
        return result