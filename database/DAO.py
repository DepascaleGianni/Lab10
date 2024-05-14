from database.DB_connect import DBConnect
from model.connection import Connection
from model.country import Country


class DAO():
    @staticmethod
    def get_all_countries():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM country"

        cursor.execute(query, ())

        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_connection(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * 
                    from contiguity c
                    where c.conttype = 1 and c.`year` <= %s
                    """
        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Connection(**row))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_sel_countries(year):
        conn = DBConnect.get_connection()

        #result = set()

        cursor = conn.cursor(dictionary=True)
        # query = """select state1no,state2no
        #             from contiguity c
        #             where c.`year` <= %s
        #             """
        # cursor.execute(query, (year,))
        #
        # for row in cursor:
        #     result.add(row['state1no'])
        #     result.add(row['state2no'])

        result = []

        query = """select distinct state1no 
                    from contiguity c
                    where c.`year` <= %s"""

        cursor.execute(query, (year,))

        for row in cursor:
            result.append(row['state1no'])

        cursor.close()
        conn.close()
        return result


