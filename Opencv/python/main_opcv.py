from sqlite_tex import Controle as SQL
from filtros import Controle as fil
from qt import App
import os,sys
from PyQt5.QtWidgets import  QApplication

nome = '\033[0;34;40mNome:Allan Ferreira de Souza RA:225619511919\nNome:Matheus Herbert RA:226264611919 \033[m'
#-------------------------------------------------------------------------------------------------------------------------------

nex = 1
sql = SQL()

def OpenCV():
  os.system('clear' if os.name == 'unix' else 'cls' )
  print("Connectando OpenCV...")
  filtros_galeria()


def filtros_galeria():
  global nex
  filt = fil(sql.select_db(nex))
  #''' Meta Dados'''
  list = {1:filt.blur_Mediano,2:filt.blur_Bilateral,3:filt.blur_GaussianBlur,4:filt.Linarizar_canal,5:filt.corte,6:filt.canalAlpha,
         7:filt.RGB_color,8:filt.RGB_degrade_efetos,9:filt.grabcut,10:filt.colar,11:filt.blur,12:filt.guadros_GaussianBlur,13:filt.RGB_Corte_pente,
         14:filt.Circulo_listrado_raio,15:filt.linear,16:filt.Retangulo,17:filt.Texto_escr,18:filt.saturacao_mt,19:filt.resize,
         20:filt.resize_Slicing,21:filt.trasformacao_affinis}
  while True:
   os.system('clear' if os.name == 'unix' else 'cls' )
   opcao =  menu_filtro()
   if opcao in list:
       list[opcao]()
   elif opcao is 23:
       pass
   elif opcao is 24:
       break
   elif opcao is 25:
      nex+=1
      break
   else:
     print("OPS Invalida...")
     os.system

def algoritmo_OpenCV():

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())


def menu_filtro():
 ops = '''\033[0;33;40mGaleria de Filtros:
               1-Blur Mediano       11-Blur            21-Rotacao
               2-Blur Bilateral     12-Blur Caixa      23-Retorno
               3-Blur Gaussiano     13-Corte e Pintar  24-Sair
               4-Limiarizacao       14-Raio RGB
               5-Corte              15-Linha           25- Next
               6-Alpha              16-Quadrado
               7-RGB                17-Texto
               8-Degrade            18-Saturacao
               9-GrabCut            19-Resize
\033[0;31;40m               10-Colar\033[m             20-Resize Slicing
                                                                         \033[m '''
 inp =  int(input(ops+"\nops:"))
 return inp


def menu():

 ops = nome+"\n\n"+ 59*'/'+"**"+59*'/' + '/\033[0;33;40mSofware  de Computação Grafica e Processamento de Imagen (OpenCV)\033[m \n' + 4*"/\n" + 59*'/'+"**"+59*'/' + '''

             \033[0;33;40m
             1 - Start
             2 - Help
             3 - Exit
             4 - Algoritmo-OCR\n\n\033[m'''+ 60*'/'*2 + 6*"/\n"*2 + 60*'/'*2

 inpu = int(input(ops))
 return  inpu

def main():
 while True:
  os.system('clear' if os.name == 'unix' else 'cls' )
  ops = menu()
  print(ops)

  if ops is 1:
    try:
     print("Start OpenCV")
     OpenCV()
    except:
     print("Erro Critico")
     break

  elif ops is 2:
     help = """ --------------------------------------"""

  elif ops is 3:
    break

  elif ops is 4:
    try:
     algoritmo_OpenCV()
    except:
     print("Erro Critico")
     break

  else:
    break


#main
main()
