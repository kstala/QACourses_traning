import pymysql
from model.group import Group
from model.customer import Customer


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database = name, user = user, password = password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_customer_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address from addressbook WHERE deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address) = row
                list.append(Customer(id=str(id), firstname=firstname, lastname=lastname, address=address))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()

