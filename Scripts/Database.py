import pandas as pf
import sqlite3

def CreateDataBase(CsvEntrada,dbname,table):
    pd_data =  pf.read_csv(CsvEntrada)
    con = sqlite3.connect("./DataBase/"+dbname+".db")
    cursor = con.cursor()
    query = CreateTable(pd_data,table)
    cursor.execute(query)
    con.commit()
    return con,pd_data


def GetTypeColumn(dataSet):
    try:
        pf.to_numeric(dataSet.dropna(),downcast="integer")
        if(dataSet.dropna() %1 == 0).all():
            return "INTEGER"
    except:
        pass
    try:
        pf.to_numeric(dataSet.dropna(),downcast="float")
        return "REAL"
    except:
        pass
    try:
        pf.to_datetime(dataSet.dropna(), errors="coerce",
            infer_datetime_format=True)
        return "DATE"
    except:
        pass
    return "TEXT"


def CreateTable(dataset,table):
    col_sql = []
    for col in dataset.columns:
        tipo = GetTypeColumn(dataset[col])
        col_sql.append(f'"{col}" {tipo}')
    ColumnSql = ",\n".join(col_sql)
    return f"""
    CREATE TABLE IF NOT EXISTS {table}(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    {ColumnSql} )
    """
    
def InsertData(df,con,table):
    print(df.columns)
    df.to_sql(table,con,if_exists="append",index=False)
    con.commit()
    return True

def UpdateData(WhereColumn,columnUpdate,data,id,table,con):
    conn  =sqlite3.connect(con)
    cursor =  conn.cursor()
    query =  f"""
    UPDATE {table}
    SET {columnUpdate} = {data}
    WHERE {WhereColumn}
    """
    cursor.execute(query)
    conn.commit()
    conn.close()