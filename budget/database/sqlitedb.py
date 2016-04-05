import sqlite3


class Datastore():
    """This class represents data-storage object.

    The Datastore will store all the account information for
    food and miscellaneous accounts.

    Attributes:
        _conn (sqlite3.Connection): A sqlite3.Connection object that represents the database
        _cursor (sqlite3.Cursor): A sqlite3.Cursor object that enables traversal over the records in the database
        _databaseFileName (str): The database filename on the disc
    """

    def __init__(self, dbFileName = None):
        if not dbFileName:
            self._databaseFileName = "example.db"
        else:
            self._databaseFileName = dbFileName

        self._conn = None
        self._cursor = None

    def connect(self):
        """Opens a database connection to the database file and creates tables."""

        try:
            self._conn = sqlite3.connect(self._databaseFileName)
            self._cursor = self._conn.cursor()

            # Create FoodAccount and MiscAccount database tables
            self._cursor.execute('''CREATE TABLE IF NOT EXISTS FoodAccount (month text, year text, amount real, total real)''')
            self._cursor.execute('''CREATE TABLE IF NOT EXISTS MiscAccount (month text, year text, amount real, total real)''')

            # Commit the change
            self._conn.commit()
        except Exception as e:
            self._conn.rollback()
            print "Error: while creating tables FoodAccount and MiscAccount:", e

    def disconnect(self):
        """Closes the database connection."""

        # Save (commit) the changes
        self._conn.commit()

        # Close the connection
        self._conn.close()

    def insertFoodAccount(self, month, year, amount):
        """Insert food account details into FoodAccount."""

        try:
            # We can use the sqlite3.Connection object as context manager to automatically commit or rollback transactions
            with self._conn:
                # Insert info to FoodAccount
                self._cursor.execute("INSERT INTO FoodAccount VALUES ('April', '2016', 45, 45)")

        except sqlite3.IntegrityError:
            print "Error: couldn't add to FoodAccount", e

    def insertMiscAccount(self, month, year):
        """Insert misc. account details into MiscAccount."""

        """
        try:
            with con:
            with self._conn:
                con.execute("insert into person(firstname) values (?)", ("Joe",))
        except sqlite3.IntegrityError:
            print "couldn't add Joe twice"
        """
        print "XXX"

    def fetchFoodAccount(self):
        """Fetch all the details from FoodAccount."""

        try:
            # We can use the sqlite3.Connection object as context manager to automatically commit or rollback transactions
            with self._conn:
                self._cursor.execute("select * from FoodAccount")
                print self._cursor.fetchall()
        except sqlite3.IntegrityError:
            print "Error: couldn't add to FoodAccount", e

    def fetchMiscAccount(self):
        """Fetch all the details from MiscAccount."""



db = Datastore()
db.connect()
db.insertFoodAccount("April", "2016", 5.45)
db.fetchFoodAccount()

"""
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS FoodAccount (month text, year text, amount real, total real)''')
#c.execute('''CREATE TABLE IF NOT EXISTS MiscAccount (month text, year text, amount real, total real)''')

#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
c.execute("INSERT INTO FoodAccount VALUES ('March','2016', 50, 50)")

conn.commit()

#t = ('RHAT',)
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
#print c.fetchone()
c.execute('SELECT * FROM FoodAccount')
print c.fetchall()
table = pd.read_sql_query("SELECT * from table_name", db)
table.to_csv(table_name + '.csv', index_label='index')


"""
#TODO Add comments in whole file


"""
Table
- FoodAccount
    - Columns: month, year, amount, total
- MiscAccount
    - Columns: month, year, amount, total
"""
