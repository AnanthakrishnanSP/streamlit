import mysql.connector


class DonorCreateRetrieveUpdateDelete:

    def __init__(self):
        self.con = mysql.connector.connect(
            user="root",
            password="root",
            host="localhost",
            database="blood_db"
        )

        self.cursor = self.con.cursor()

    # CREATE
    def create(self, name, blood_group, phone, city, last_donation):

        query = """
        insert into donor(name, blood_group, phone, city, last_donation)
        values(%s, %s, %s, %s, %s)
        """

        data = (name, blood_group, phone, city, last_donation)

        self.cursor.execute(query, data)
        self.con.commit()

        return self.cursor.rowcount > 0

    # RETRIEVE ALL
    def retrieve(self):

        query = "select * from donor"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        return records

    # RETRIEVE USING ID
    def retrieve_by_id(self, id):

        query = "select * from donor where id = %s"

        self.cursor.execute(query, (id,))

        records = self.cursor.fetchall()

        return records

    # UPDATE
    def update(self, id, name, blood_group, phone, city, last_donation):

        query = """
        update donor
        set name = %s,
            blood_group = %s,
            phone = %s,
            city = %s,
            last_donation = %s
        where id = %s
        """

        data = (
            name,
            blood_group,
            phone,
            city,
            last_donation,
            id
        )

        self.cursor.execute(query, data)

        self.con.commit()

        return self.cursor.rowcount > 0

    # DELETE
    def delete(self, id):

        query = "delete from donor where id = %s"

        self.cursor.execute(query, (id,))

        self.con.commit()

        return self.cursor.rowcount > 0