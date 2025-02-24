import mysql.connector

class dbConnector:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="10.10.0.3",
            user="root",
            password="E543^%lLKo16",
            database="wikidb"
        )

        self.cursor = self.db.cursor()


    def get_links_from(self, from_id):
        self.cursor.execute("""
            SELECT p.page_id 
            FROM pagelinks AS pl 
            JOIN linktarget AS lt ON pl.pl_target_id = lt.lt_id 
            JOIN page AS p ON lt.lt_title = p.page_title 
            WHERE pl.pl_from = %s
        """, (from_id,))  # Using tuple for parameterized input

        # Fetch and return the results
        results = {row[0] for row in self.cursor.fetchall()}
        return results
    

    def get_links_to(self, target_id):
        self.cursor.execute("""
            SELECT pl.pl_from
            FROM pagelinks AS pl 
            JOIN linktarget AS lt ON pl.pl_target_id = lt.lt_id 
            JOIN page AS p ON lt.lt_title = p.page_title 
            WHERE p.page_id = %s
        """, (target_id,))  # Using tuple for parameterized input

        # Fetch and return the results
        results = {row[0] for row in self.cursor.fetchall()}
        return results
    

    def get_id_from_title(self, title):
        self.cursor.execute("""
            SELECT page_id 
            FROM page  
            WHERE CONVERT(page_title USING utf8mb4) = %s
        """, (title,))  # Using tuple for parameterized input

        result = self.cursor.fetchone()[0]
        return result
    
    def get_title_from_id(self, page_id):
        self.cursor.execute("""
            SELECT CONVERT(page_title USING utf8mb4) 
            FROM page  
            WHERE page_id = %s
        """, (page_id,))  # Using tuple for parameterized input

        result = self.cursor.fetchone()[0]
        return result
    

    # Context management: enter and exit methods
    def __enter__(self):
        # Return self to be used in the "with" block
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close cursor and connection when exiting the "with" block
        if self.cursor:
            self.cursor.close()
        if self.db:
            self.db.close()
        print("Connection and cursor closed.")


    
if __name__ == "__main__":
    with dbConnector() as db: 
        print("Links FROM Har Schania:")
        print(db.get_links_from(58021))
        print("Links TO Har Schania:")
        print(db.get_links_to(58021))
