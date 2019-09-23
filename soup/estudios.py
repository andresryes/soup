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
        result.append(f"display ALL \"Estudios\" (Doctorados/Maestrias/Posgrados/Licenciaturas/Baccalaureus):")
        resEst = []
        for i in soup.find_all(class_="estudios")[0].parent.find_all('p'):
            resEst.append(i.text)
            
        for i in soup.find_all(class_="estudios")[0].parent.parent.parent.parent.find_all('div')[2]:
            print(i)
        print(resEst)
        result.append("---------------------------------------")


        return result