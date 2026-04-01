from Scripts.Database import CreateDataBase,InsertData
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
   
#Exortando para

    