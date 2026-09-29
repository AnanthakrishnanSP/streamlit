import mysql.connector


class booklistcreateretriveupdatedelete:
    def __init__(self):
        self.con= mysql.connector.connect(user='root',password='root',host='localhost',database='library_db')
        print(self.con)
        self.cursor=self.con.cursor()
        print("connected")
    def list(self):
        query="select * from book"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            # for row in records:
            #     print(row)
            return(records)
        else:
            print("no records")

    def create(self,title,author,price, pages, language):
        query = "insert into book(title, author, price, pages, language)values (%s, %s, %s, %s, %s)"
        data = (title, author, price, pages, language)
        self.cursor.execute(query, data)
        self.con.commit()
        print("Inserted Data Successfully")

    def retrive(self,id):
        query="select * from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            return(record)
        else:
            print("no records")

    def update(self,id, title, author, price, pages, language):
        query = "update book set title=%s, author=%s, price=%s, pages=%s, language=%s where id=%s"
        data = (title, author, price, pages, language, id)
        self.cursor.execute(query, data)
        self.con.commit()
        if self.cursor.rowcount > 0:
            return True
        else:
            return False

    def delete(self,id):
        query="delete from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.con.commit()
        if self.cursor.rowcount>0:
            # print("deleted")
            return True
        else:
            # print('not record')
            return False


b=booklistcreateretriveupdatedelete()
b.list()
b.create('abc',"john",360,500,'english')
b.retrive(2)
b.delete(6)
b.update(2, 'Python', 'John', 500, 600, 'English')