import sqlite3


class Database():
    def __init__(self, database='quotes.db'):
        self.connection(database, status='connect')

    def connection(self, database='quotes.db', status='connect'):
        if status == 'connect':
            self.conn = sqlite3.connect(database)
            self.curr = self.conn.cursor()
        elif status == 'commit':
            self.conn.commit()
        else:
            self.conn.commit()
            self.conn.close()

    def create_table(self, table, field_dict, exist_ok=True):
        field = []
        for i, j in field_dict.items():
            field.append('{} {}'.format(i, j))
        field = ','.join(field)
        response = self.execute('create table {}({})'.format(table, field))
        if response and (exist_ok == False):
            self.execute('drop table {}'.format(table))
            self.execute('create table {}({})'.format(table, field))
            print("New table is created")

    def execute(self, string):
        try:
            self.curr.execute('''{}'''.format(string))
        except Exception as err:
            print(err)
            return 1


'''
a = Database()
a.create_table('quote_data', {'quote': 'text',
                              'author': 'text', 'tag': 'text'}, exist_ok=False)
a.execute('insert into quote_data values ("Hello1","Me1","Prince1")')
a.connection(status=False)
'''
