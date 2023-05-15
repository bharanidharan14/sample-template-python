import jaydebeapi


class DremioInterface:
    def __init__(self):
        print("inside Dremio interface class")

    def get_connection(self):
        """create dremio connection and returns connection object"""
        conn = jaydebeapi.connect(
            "com.dremio.jdbc.Driver",
            "jdbc:dremio:direct=localhost:31010",
            ["test", "test1234"],
            "/Users/admin/Downloads/dremio-jdbc-driver-3.0.1-201811132128360291-804fe82.jar",
        )
        return conn

    def execute_fetch_one_result(self, query: str):
        try:
            with self.get_connection() as conn:
                with conn.cursor() as fetch_one_cur:
                    fetch_one_cur.execute(query)
                    result = fetch_one_cur.fetchone()
                    return result
        except Exception as e:
            raise e

    def execute_fetch_all_result(self, query):
        try:
            with self.get_connection() as conn:
                with conn.cursor() as fetch_all_cur:
                    fetch_all_cur.execute(query)
                    result = fetch_all_cur.fetchall()
                    return result
        except Exception as e:
            raise e
