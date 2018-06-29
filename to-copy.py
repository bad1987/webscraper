
import time, threading, database


QtCore.QObject.connect(self.sky, QtCore.SIGNAL('clicked()'), self.skyNews)
QtCore.QObject.connect(self.afriquemedia, QtCore.SIGNAL('clicked()'), self.afrmediaNews)

self.stopThread = False
self.lock = threading.Lock()
self.numThread = 0

def display(self, website='sky'):
    db = database.Scraperdatabase()

    stop = False
    while True:

        res = db.retreivePerWebsiteData(website)
        if res:
            for content in res:
                self.title.setText(_fromUtf8(str(content[0]).rstrip('\n').replace('\n', "")))
                self.body.setText(_fromUtf8(content[1]))
                # self.website.setText(_fromUtf8(content[2]))
                # self.textBrowser.setText(_fromUtf8(content[0]))
                time.sleep(10)

                with self.lock:
                    if self.stopThread:
                        self.stopThread = False
                        self.numThread -= 1
                        if self.numThread < 0:
                            self.numThread = 0

                        stop = True

                if stop:
                    break
            if stop:
                break

        else:
            # print("the database is empty")
            self.title.setText(_fromUtf8('there are no news available for now'))
            self.body.setText(_fromUtf8('No content available, be patient'))


def skyNews(self):
    # self.display('sky')

    with self.lock:
        if self.numThread != 0:
            self.stopThread = True
        self.numThread += 1

    thread = threading.Thread(target=self.display, args=('sky',), daemon=True)
    thread.start()


def afrmediaNews(self):
    # self.display('afriquemedia')

    with self.lock:
        if self.numThread != 0:
            self.stopThread = True
        self.numThread += 1

    thread = threading.Thread(target=self.display, args=('afriquemedia',), daemon=True)
    thread.start()
