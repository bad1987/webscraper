import sqlite3
from datetime import datetime

class Scraperdatabase:

    def __init__(self):
        self.conn = sqlite3.connect('scraper.db')
        self.cur = self.conn.cursor()
        self.createtable()
        self.date = self.buildTime()
        self.deleteOldData()


    def createtable(self):

        self.cur.executescript("""
                create table if not exists news (
                id integer primary key,
                title text not null,
                body text not null,
                website text not null,
                date text not null,
                link text
                );
        """)

    def insertdata(self, datalist):

        for data in datalist:

            #check if the item already exists before inserting
            tmp = list(data)
            tmp.pop()
            tmp = tuple(tmp)
            self.cur.execute("select title, body from news where title=? and body=?",tmp)
            if not self.cur.fetchone():

                #add the date
                t = list(data)
                t.append(self.date)
                data = tuple(t)
                try:
                    self.cur.execute("insert into news(title,body,website,date) values (?,?,?,?)",data)
                    print('item inserted')
                except:
                    print('something went wrong while trying to insert {}'.format(data))
        try:
            self.conn.commit()
        except:
            self.conn.rollback()

    def closeconnection(self):
        self.conn.close()

    def retreivedata(self):

        result = self.cur.execute("select title, body, website, date from news")
        rows = result.fetchall()

        return rows

    def retreivePerWebsiteData(self,web):

        result = self.cur.execute("select title, body, website from news where website=?", (web,))
        rows = result.fetchall()

        return rows

    def buildTime(self):

        date = datetime.now().date()

        y = date.year
        m = date.month
        d = date.day

        fdate = str(y) + '/' + str(m) + '/' + str(d)

        return fdate

    def deleteOldData(self):
        todayDate = self.date

        res = self.cur.execute("select date from news")
        d = res.fetchone()

        print('[+] trying to delete old data\n')
        if len(d) > 0:

            if todayDate != d[0]:
                res = self.cur.execute("delete from news where date=?",d)

                try:
                    self.conn.commit()
                    print('[+]old news deleted\n')
                except:
                    print('[+]something went wrong, data not deleted\n')
                    self.conn.rollback()
            else:
                print('[+] there are no old data to delete\n')
        else:
            print('[+] database is empty\n')