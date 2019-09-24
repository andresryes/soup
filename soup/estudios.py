from datetime import datetime

class Estudios:
    def __init__(self, soup):
        self.soup = soup
        self.arrayToPrint = []

    #init the process
    def init(self):
        return self.run(self.soup)

    #the method that actually make every parameter from Estudios section
    def run(self, soup):
        result = []
        #display all items from "topmenu"
        result.append(f"display all items from \"topmenu\" (8 in total):")
        for i in soup.find(id="topmenu").ul.find_all(class_="external text"):
            result.append("-"+i.text)
        result.append("---------------------------------------")

        # display ALL "Estudios" (Doctorados/Maestrias/Posgrados/Licenciaturas/Baccalaureus)
        result.append(f"display ALL \"Estudios\" (Doctorados/Maestrias/Posgrados/Licenciaturas/Baccalaureus):  Output exceeds 30 lines, sending output to: logs/2estudios_display_all_estudios.txt")            

        f = open("../logs/2estudios_display_all_estudios.txt","w+")
        f.writelines("Date of generation: " + str(datetime.now())+"\r\n")
        f.writelines("================================================"+"\r\n")
        if(len(soup.find_all(class_="estudios")[0].parent.parent.parent.parent.find_all('div')[0].find_all('a')) > 30):
            for i in soup.find_all(class_="estudios")[0].parent.parent.parent.parent.find_all('div')[0].find_all('a'):
                if i.text != "":
                    f.writelines("-"+i.text+"\r\n")
        else:
            result.append("-"+i.text)
        result.append("---------------------------------------")

        #display from "leftbar" all <li> items (4 in total)
        result.append(f"display from \"leftbar\" all <li> items (4 in total)")            
        for i in soup.find_all(class_="leftbar")[0].find_all('li'):
            result.append("-"+i.find('a').text)
        result.append("---------------------------------------")
        # get and display all available social media with its links (href) "class=social pull-right"
        result.append(f"get and display all available social media with its links (href) \"class=social pull-right\"")
        
        for i in soup.find_all(class_="social pull-right")[0].find_all('a'):
            result.append("-"+i['href'])

        result.append("---------------------------------------")

        # count all <a> (just display the count)
        result.append(f"count all <a> (just display the count): {len(soup.find_all('a'))}")
        result.append("---------------------------------------")

        return result