import requests, re, subprocess
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import database

class Webscraper:

    def __init__(self):

        #checking the internet connection first
        self.checkInternetConnection()

        self.db = database.Scraperdatabase()
        self.url = "https://news.sky.com"
        self.websiteName = ['bbc','cnn','sky','euronews']

        #launch the operation
        # self.extractAllContent(self.url)

    def geturls(self,page):
        """returns a list of urls"""
        urls = []

        soup = BeautifulSoup(page, 'html.parser')

        for link in soup.find_all('a'):
            urls.append((link.get('href'),link.text))
        print(urls)

        return urls

    def fetchpage(self,url):
        """returns an html document"""
        # #selenium
        # extension_path = "/usr/local/share/chromedriver"
        # display = Display(visible=0)
        # display.start()
        # driver = webdriver.Chrome(extension_path)
        # driver.implicitly_wait(30)
        #
        # try:
        #     driver.maximize_window()
        # except:
        #     pass
        #
        # driver.get(url)
        #
        # sourcePage = driver.page_source
        # driver.close()

        #requests
        userAgent = {'User-Agent':'Mozilla/5.0'}
        req = requests.session()
        page_raw = req.get(url, headers=userAgent)
        sourcePage = page_raw.text


        return sourcePage

    def extractAllContent(self, url):
        final = []
        urllist = None
        wsn = self.websitename(url)
        if wsn in self.websiteName and wsn == 'bbc':
           urllist = self.extractnavlinksbbc(url)
        else:
            urllist = self.extractnavlinks(url)
        websitename = self.websitename(url)

        for url in urllist:
            page = self.fetchpage(url)
            content = self.extractContent(page)

            for clist in content:
                tmp = list(clist)
                index = content.index(clist)
                tmp.append(websitename)
                content[index] = (tuple(tmp))

            isnone = False
            #make sure there will be no duplicate items in the final list
            for plist in final:
                for clist in content:
                    if clist in plist:
                        content.remove(clist)


            #check for none value
            for a in content:
                for b in a:
                    if b == None:
                        isnone = True
                        break
                if isnone:
                    break

            if len(content) > 0 and not isnone:
                final.append(content)
                # print(content)
                # print(len(content))

        self.savetodatabase(final)

        return final

    def savetodatabase(self,objectlist):

        for obj in objectlist:
            self.db.insertdata(obj)

    def constructlink(self,base,extent):
        result = ''
        if base[-1] == '/':
            if extent[0] == '/':
                result = base + extent[1:]
            else:
                result = base + extent
        else:
            if extent[0] == '/':
                result = base + extent
            else:
                result = base + '/' + extent

        return result

    def websitename(self,url):
        r = url.split('.')
        if str(r[0]).startswith('http'):
            return r[1]
        else:
            return r[0]

    def extractnavlinks(self,url):

        links = []
        page = self.fetchpage(url)

        soup = BeautifulSoup(page, 'html.parser')
        headerlink = soup.find('header')
        headerlink = headerlink.find('ul').children

        for i in headerlink:
            l = self.constructlink(url,i.find('a').get('href'))
            links.append(l)

        return links

    def extractnavlinkseuronews(self,url):

        links = []
        page = self.fetchpage(url)

        soup = BeautifulSoup(page, 'html.parser')
        headerlink = soup.find('header')
        headerlink = headerlink.find('ul')
        # print(headerlink)

        for i in headerlink.children:
            if str(i.find('a')).startswith('<a'):
                l = self.constructlink(url, i.find('a').get('href'))
                if not l in links:
                    links.append(l)
        print(links)
        return links

    def extractnavlinksbbc(self,url):

        links = []
        page = self.fetchpage(url)

        soup = BeautifulSoup(page, 'html.parser')
        headerlink = soup.find('ul', {'class':'gs-o-list-ui--top-no-border nw-c-nav__wide-sections'})
        # print(headerlink)

        url = url.split('/')
        url = url[0] + '//' + url[2]

        for i in headerlink.children:
            if str(i.find('a')).startswith('<a'):
                l = self.constructlink(url, i.find('a').get('href'))
                if not l in links:
                    links.append(l)
        print(links)
        return links

    def extractEuronewsContent(self):
        pass

    def extractContent(self,page):
        """returns a list of tuples of title:paragraph or title only"""

        soup = BeautifulSoup(page,'html.parser')
        info = []

        for item in soup.find_all(re.compile(r'h[1-3]')):
            temp = []

            if str(item).startswith('<') and str(item).endswith('>'):
                # dealing with title's children
                for child in item.children:
                    if str(child).startswith('<a') and str(child).endswith('</a>'):
                        if child.string:
                            temp.append(child.string)


                #retreiving paragraph if it exists
                inter = []
                for up in item.parent:
                    if str(up) != str(item):
                        inter.append(up)
                while inter:
                    up = inter.pop()
                    if str(up).startswith('<') and str(up).endswith('>'):
                        if str(up).startswith('<p') and str(up).endswith('</p>'):
                            temp.append(up.string)
                            break
                        else:
                            if up.find('p'):
                                temp.append(up.find('p').string)
                                break

            #construct the final tuple and add to the list
            if len(temp) > 1:
                info.append(tuple(temp))

        return info
    def extractAllAfriquemediaContent(self, url):
        final = []
        urllist = [url]
        websitename = self.websitename(url)


        # extract subcontent
        i =0
        page = self.fetchpage(url)
        soup = BeautifulSoup(page, 'html.parser')
        ul = soup.find('ul', {'class': 'pagination'})
        for link in ul.find_all('a'):
            if str(link).startswith('<a'):
                l = "http://www.afriquemedia.tv" + str(link.get('href'))
                urllist.append(l)
        if len(urllist) > 1:
            for i in range(2):
                if urllist:
                    urllist.pop()


        # retreive useful info
        for url in urllist:
            page = self.fetchpage(url)
            content = self.extractContentAfriquemedia(page)

            for clist in content:
                tmp = list(clist)
                index = content.index(clist)
                tmp.append(websitename)
                content[index] = (tuple(tmp))

            #make sure there will be no duplicate items in the final list
            for plist in final:
                for clist in content:
                    if clist in plist:
                        content.remove(clist)

            if len(content) > 0:
                final.append(content)
                # print(content)
                # print(len(content))

        self.savetodatabase(final)

        return final

    def extractContentAfriquemedia(self, page):
        """returns a list of tuples of title:paragraph or title only"""

        soup = BeautifulSoup(page, 'html.parser')
        info = []

        for item in soup.find_all(re.compile(r'h[1-3]')):
            temp = []

            if str(item).startswith('<') and str(item).endswith('>'):
                # dealing with title's children
                for child in item.children:
                    if str(child).startswith('<a') and str(child).endswith('</a>'):
                        if child.string:
                            temp.append(child.string)
                        # print(child)

                # retreiving paragraph if it exists
                inter = []
                inter = item.parent.find('div',{'class':'catItemIntroText'})
                if inter:
                    temp.append(inter.string)


            # construct the final tuple and add to the list
            if len(temp) > 1:
                info.append(tuple(temp))
                # for i in temp:
                #     print(i)


        return info


    def retreivefromdb(self):
        return self.db.retreivedata()

    def display(self):

        info = self.db.retreivedata()
        stripped = []
        for row in info:
            for item in row:
                self.formater(item)
                # print(str(item).strip('\n').replace('\t',""))
            print("\n\n")

    def formater(self,string):
        string = str(string).strip('\n').replace('\t',"")
        res = []
        i = 0
        k = 0
        for c in str(string):

            if i == 27:
                if c != ' ':
                    j = k - 1
                    while j > 0:
                        if res[j] == ' ':
                            res[j] = '\n'
                            break
                        j -= 1
                    res.append(c)
                else:
                    res.append('\n')
                i = 0
            else:
                res.append(c)
                i += 1
            k += 1
        f = ''
        for c in res:
            f += c
        print(f)

    def run(self):

        #websites to scrape
        sky = "https://news.sky.com"
        afriquemedia = "http://www.afriquemedia.tv/infos/actualite/afrique"
        linuxtoday = "https://www.linuxtoday.com"
        linuxinsider = "https://www.linuxinsider.com"

        # retreive content from afriquemedia
        self.extractAllAfriquemediaContent(afriquemedia)

        #retreive content from sky
        self.extractAllContent(sky)

    def checkInternetConnection(self):

        host = '8.8.8.8'

        response = subprocess.run(['ping','-c 1','8.8.8.8'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if response.returncode == 0:
            print('\n[+] Internet connection is active\n')
        else:
            print('\n[+] There is no active Internet connection\n')
            print('[+] Please make sure you have an active connection then try again')
            print('[+] Exiting the programme')
            exit(1)

def main():
    wp = Webscraper()
    url = "https://news.sky.com"
    # url = "http://www.bbc.com/news"
    # url = "http://www.euronews.com/"
    # wp.extractnavlinksbbc("http://www.bbc.com/news")

    # wp.extractAllAfriquemediaContent("http://www.afriquemedia.tv/infos/actualite/afrique")

    wp.run()
    # wp.display()

if __name__ == '__main__':
    main()