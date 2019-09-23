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

        return result