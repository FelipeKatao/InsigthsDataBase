from Scripts.Database import UpdateData

def ClearDataColumn(column,con,columnUpdate,valueUpdate,table):
    UpdateData(f"{column}",columnUpdate,valueUpdate,table,con)