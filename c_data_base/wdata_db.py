import sqlite3

# Terminology:
# - raw_data (rd) stands for data coming from a_data_processing or b_data_processing
# - db is the usual db for DataBase that we are creating



def db_manager():
    pass



# ---------------------------------------------------------------------------------------------------------------------
# db methods db methods db methods db methods db methods db methods db methods db methods db methods db methods db methods
# ---------------------------------------------------------------------------------------------------------------------


def create_db_file(name):
    sqlite3.connect(name)


def create_table(db, table):
    with sqlite3.connect(db) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute(f"""CREATE TABLE {table} (
                            Query_ID int,
                            Query_ID_Name text,
                            Query_Date text,
                            Query_Time text,
                            Position int,
                            Video_ID int,
                            Video_Title text,
                            Video_Description text,
                            Video_Category_ID int,
                            Video_Category_Name text,
                            Tags text,
                            Number_of_Tags int,
                            Publication_Date text,
                            Publication_Time text,
                            Video_duration_s int,
                            Thumbnail_Url text,
                            Visualizations int,
                            Likes int,
                            Dislikes int,
                            Favorites int,
                            Comments int,
                            Channel_ID text,
                            Channel_Title text,
                            Channel_Country text,
                            Channel_Description text,
                            Channel_Creation_Date text,
                            Channel_Views int,
                            Channel_Subscribers int,
                            Channel_Videos_Published int,
                            Video_Etag text,
                            Channel_Etag text)
                            """)

        
def insert_row(raw_data):
    pass



# the raw_data comes already ordered
def fill_db(raw_data, db, table):
    with sqlite3.connect(db) as connection:
        with connection:
            
            execution_string = f"INSERT INTO {table} VALUES ("
            for _ in range(len(raw_data["Data"][0]) - 1):
                execution_string += "?, "
            execution_string += "?)"
            
            for i in range(len(raw_data["Data"])):
                row = rd_get_single_row(data, i)
                print(row)
                connection.execute(execution_string, row)
                
                

def search_db(db, table, collum, atribute, generator=False):
    with sqlite3.connect(db) as connection:
        with connection:
            cursor.execute("SELECT * FROM ? WHERE ?=?",  
                           (table, collum, atribute))
            if generator == False:
                return cursor.fetchall()
            else:
                for i in cursor.fetchall():
                    yield (i,)


def update_data(data):
    pass


def delete_data(data):
    pass



# ---------------------------------------------------------------------------------------------------------------------
# raw_data methods raw_data methods raw_data methods raw_data methods raw_data methods raw_data methods raw_data methods
# ---------------------------------------------------------------------------------------------------------------------

# this function may yield tuples where keys are followed by values
# ex: {"age":42} -> ("age", 42)
# or return only values
def rd_get_single_row(data, numb):
    row = ()
    for j, k in data["Data"][numb].items():
        row += (k,)
    return row

        
def rd_get_all_rows(data):
    for i in data["Data"]:
        for j, k in i.items():
            yield (j, k)
            

            


# create_db_file("testando.db")
# create_table("testando.db", "testando")

fill_db(data, "testando.db", "testando")