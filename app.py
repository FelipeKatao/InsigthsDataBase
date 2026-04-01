from Scripts.Database import CreateDataBase,InsertData
from Scripts.ClearData import ClearDataColumn
#Configuracao Base
Configs = {
    "Column":"mes",
    "TableName":"Estoque_2025",
    "Csv":"./DataBase/Estoque_Snapshot_ano2025.csv",
    "Db":"EstoqueVendas"
}
# Criação da DataBase
con,pd = CreateDataBase("./DataBase/Estoque_Snapshot_ano2025.csv","EstoqueVendas","Estoque_2025")
if pd[Configs["Column"]].count() <=1:
    InsertData(pd,con)
   
#limpeza de dados 
#Precos
ClearDataColumn("preco_medio IS NULL","./DataBase/"+Configs["Db"]+".db","preco_medio",0,f"{Configs["TableName"]}")
ClearDataColumn("preco_medio = 'erro'","./DataBase/"+Configs["Db"]+".db","preco_medio",0,f"{Configs["TableName"]}")
ClearDataColumn("desconto_percentual = 'dez'","./DataBase/"+Configs["Db"]+".db","desconto_percentual",0,f"{Configs["TableName"]}")
ClearDataColumn("produto = 'Mouze'","./DataBase/"+Configs["Db"]+".db","produto","'Mouse'",f"{Configs["TableName"]}")

