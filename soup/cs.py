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
        return result