import sqlite3
import os.path
import cv2


class Controle():
 def __init__(self):
     #print("Class Banco de dados...")
     pass

 def sqlite_create_db_tb(self,path):
   exis = not os.path.exists(path)
   if exit:
     conect = sqlite3.connect(path)
     table = ''' CREATE TABLE if not exists PICTURE(
     ID INTEGER PRIMARY KEY AUTOINCREMENT,
     Nome VARCHAR(11) NOT NULL,
     Data DATE NOT NULL,
     Picture BLOB,
     Formato VARCHAR(4)

     )'''
     conect.execute(table)

   else:
     print("tabela não Existe\n")

   return conect


 def Tamanho_path(self,path):
    arquivo = os.path.join(os.getcwd(),"Fotos")
    dir = os.listdir(arquivo)
    return len(dir)


 def insert_db(self,conne,file_foto):
  #Iseri fotos de 0 a tam (Tamanho da Pasta)
  tam = Tamanho_path(file_foto)
  path = os.path.basename(file_foto)
  nome ,form = os.path.splitext(file_foto)
  for i in range(tam-1):
   #path_novo =   nome.replace("1",str(i)) + form
   filePasta = file_foto.replace("1",str(i))
   #--------------------------------------------------------------------------------------------------------------
   with open(filePasta, 'rb') as input_file:
    ablob = input_file.read()
    arquivo = os.path.basename(filePasta)
    insert = (''' INSERT INTO PICTURE (Nome, Data,Picture,Formato)
    VALUES(?,?,?,?);''')
    nome, format = os.path.splitext(arquivo)
    conne.execute(insert,[nome,'2019-04-13',sqlite3.Binary(ablob),format])
    conne.commit()

 def select_pintura(self,cursor, id_foto):
    sql = "SELECT Nome,Data,Picture,Formato FROM PICTURE WHERE id = :id"
    param = {'id': id_foto}
    cursor.execute(sql, param)
    nome, data, ablob,format = cursor.fetchone()
    filename = nome + format
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename

 def criar_db(self):
  #Desativa apenas Quando criar o banco de dados
  '''
  #Criar banco  de dados
  self.sqlite_create_db_tb("OpenCV1_db.sqlite3")
  print("Banco Criado com Sucesso")
 '''

 def Abilit_Insert(self):
   conect = self.sqlite_create_db_tb("OpenCV1_db.sqlite3")
   path = "C:/Users/allan/Documents/Drive sof/Opencv/Fotos/foto1.jpg"
   self.insert_db(conect,path)
   #print("Dados Inseridos  com Sucesso")

 def select_db(self,id):
   #Selecionar dados do DB
   conect = self.sqlite_create_db_tb("OpenCV1_db.sqlite3")#Ativar Essa opção apenas quando criar o banco de dados
   cursor = conect.cursor()
   BMP =self.select_pintura(cursor,id)
  # print("Selecao feita com Sucesso")
   return BMP

 def close_db(self):
   cursor.close()
   conect.close()

 def cv(self):
     img = cv2.imread(self.select_db())
     cv2.imshow("CV",img)
     cv2.waitKey(0)

#dados = Controle()
#dados.select_db()
#dados.cv()

#----------------------------------------------------------------------------------------------------------
'''
file = open("C:/Users/allan/Documents/Drive sof/Opencv/Fotos/foto1.jpg",'rb')
x = file.read()
print(x)
file.close()
'''
