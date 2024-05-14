from database.DAO import DAO

conn = DAO.get_all_connection(1900)
sel = DAO.get_sel_countries(2000)
print(sel)
print(len(conn))
