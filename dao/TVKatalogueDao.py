import pyodbc


class TVKatalogueDAO:
    # fix this url crap tonightUID
   ## def __init__(self):
   ##     connection_url = MySQLdb.connect(host='24.54.205.36', tvkatalogue='RemoteMatcha', passwd='RemoteMatcha', db='BeyondHorizonsDB',port = 6606)
   ##     # connection_url = (host="localhost", tvkatalogue='Argent', passwd='ArgentSable776', db='MatchaWareDB')
   ##     self.conn = connection_url

    def __init__(self):
        connection_url = pyodbc.connect(Driver="SQL Server Native Client 11.0",
        SERVER="localhost", DATABASE="BingeWatcherFlaskTest", Trusted_Connection="yes")
        ##connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    #server = 'tcp:myserver.database.windows.net' 
    #database = 'mydb' 
    #tvkataloguename = 'mytvkataloguename' 
    #password = 'mypassword' 
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    #cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+tvkataloguename+';PWD='+ password)
    #cursor = cnxn.cursor()


    def getAllTVKatalogues(self):
        cursor = self.conn.cursor()
        query = "select * from [TVKatalogue];"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTVKatalogueById(self, tvkid):
        cursor = self.conn.cursor()
        query = "select * from [TVKatalogue] Where tvkid = ?;"
        cursor.execute(query, (tvkid))
        result = cursor.fetchone()
        return result

    def getTVKatalogueByUID(self, UID):
        cursor = self.conn.cursor()
        query = "select * from [TVKatalogue] Where uid = ?;"
        cursor.execute(query, (UID,))
        result = cursor.fetchone()
        return result

    def insert(self, uid, tvid, tvkustatus):
        cursor = self.conn.cursor()
        query = "insert into [TVKatalogue](uid, tvid, tvkustatus) values (?, ?, ?) ;"
        cursor.execute(query, (uid, tvid, tvkustatus))
        query = "SELECT @@IDENTITY AS [TVKID];"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.commit()
        return result

    def delete(self, tvkid):
        cursor = self.conn.cursor()
        query = "delete from [TVKatalogue] where tvkid = ?;"
        cursor.execute(query, (tvkid,))
        self.conn.commit()
        return tvkid

    def update(self, tvkid, uid, tvid, tvkustatus):
        cursor = self.conn.cursor()
        query = "update [TVKatalogue] set uid = ?, tvid = ?, tvkustatus = ? where tvkid = ?;"
        cursor.execute(query, (uid, tvid, tvkid, tvkustatus))
        self.conn.commit()
        return tvkid