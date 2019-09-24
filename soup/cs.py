import requests
import shutil
from datetime import datetime
class CS:
    def __init__(self, soup):
        self.soup = soup
        self.arrayToPrint = []

    #init the process
    def init(self):
        return self.run(self.soup)

    #the method that actually make every parameter from Portal section
    def run(self, soup):
        result = []
        #GET title
        result.append(f"GET title: {soup.title.string}")
        result.append("---------------------------------------")

        #get all href
        result.append(f"GET and display the href: Output exceeds 30 lines, sending output to: logs/3cs_display_the_href.txt")

        f = open("../logs/3cs_display_the_href.txt","w+")
        f.writelines("Date of generation: " + str(datetime.now())+"\r\n")
        f.writelines("================================================"+"\r\n")
        if(len(soup.find_all(attrs={"href":True})) > 30):
            for i in soup.find_all(attrs={"href":True}):
                if i.text != "":
                    f.writelines("-"+i.name.strip()+": "+i['href']+"\r\n")
        else:
            result.append("-"+i.name.strip()+": "+i.text.strip())

        result.append("---------------------------------------")

        #Download the "FACULTAD de CIENCIAS ECONOMICAS" logo. (you need to obtain the link dynamically)
        result.append(f"Download FCE logo")
        imgUrl = soup.find_all(class_="fl-photo-img wp-image-500 size-full")[0]['src']
        response = requests.get(imgUrl, stream=True)
        with open("../fce.png", 'wb') as f:
            f.write(response.content)
        result.append("---------------------------------------")
        #GET following <meta>: "title", "description" ("og")
        result.append(f"GET following <meta>: \"title\", \"description\" (\"og\"):")
        metaT = soup.find("meta",  property="og:title")
        metaD = soup.find("meta",  property="og:description")
        result.append(f"- title: {metaT['content']}")
        result.append(f"- description: {metaD['content']}")
        result.append("---------------------------------------")
        #count all <a> (just display the count)
        result.append(f"count all <a> (just display the count): {len(soup.find_all('a'))}")
        result.append("---------------------------------------")    

        #count all <div> (just display the count)
        result.append(f"count all <div> (just display the count): {len(soup.find_all('div'))}")
        result.append("---------------------------------------")

        return result