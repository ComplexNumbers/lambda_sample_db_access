import pymysql.cursors

class DbAccessByPymySQL: 

    __connection = None

    def __init__(self, endpoint, db_user, db_passwd, db_schema,db_charset='utf8'):

        if self.__connection == None:
            self.__connection =  pymysql.connect(
                            host=endpoint,
                            user=db_user,
                            password=db_passwd,
                            db=db_schema,
                            charset=db_charset,
                            cursorclass=pymysql.cursors.DictCursor)

    def close_db(self):
        if self.__connection != None:
            self.__connection.close()

    def insert(self,sql):
        self.__execute_sql(self,sql)

    def select_one(self,sql):
        result = []
        with self.__connection.cursor() as cursor:
            cursor.execute(sql)
            result.append(cursor.fetchone())
        return result

    def select_all(self,sql):
        result = []
        with self.__connection.cursor() as cursor:
            cursor.execute(sql)
            result.append(cursor.fetchall())
        return result

    def update(self,sql):
        self.__execute_sql(self,sql)

    def delete(self,sql):
        self.__execute_sql(self,sql)

    def __execute_sql(self,sql):
        with self.__connection.cursor() as cursor:
            cursor.execute(sql)
        

            






