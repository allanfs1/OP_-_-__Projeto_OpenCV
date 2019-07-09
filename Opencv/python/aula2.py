''' Sofware para Computação Gráfica'''

'''
    User:OpenCV e OpenGL
    Data:07/04/2019
    Autor:@Allan F de Souza
    Curso:Ciências da Computação
    Materia:Computação Gráfica e Processamento de Imagen
    '''
import cv2
from  PIL import Image
import numpy as np
from matplotlib import pyplot as plt
'''Chamar as Imagen do Banco de dados'''
#img= Image.open("foto03.jpg")
#img.rotate(45).show()
i=0
n=5
valor = 100
#-------------------------------------------------------------------------------------------------------------------
class Controle:

  def __init__(self):
   '''Ler imagen da Memoria Hard Disk'''
   self.imagenOtton = cv2.imread("BZ.jpg")
   print("Class Iniciada")

  def tamanho_RGB(self):
    print("Processamento...")
    self.tam = self.imagenOtton.shape
    print("Tamanho:\nY={0} e X={1}\n\n".format(self.tam[0],self.tam[1]))
    if valor <= self.tam[0] and valor <= self.tam[1]:
     print("Cores RGB:")
     print("Blu=",self.imagenOtton.item(self.tam[0]-valor,self.tam[1]-100,2))
     print("Green=",self.imagenOtton.item(self.tam[0]-valor,self.tam[1]-100,1))
     print("Red=",self.imagenOtton.item(self.tam[0]-valor,self.tam[1]-100,0))
     (b,g,r) = self.imagenOtton[200,140]
     print("Red",r,"Verde",g,"Azul",b)

  def Linarizar_canal(self):
    global imagenOtton
    self.imagenOtton = cv2.cvtColor(self.imagenOtton,cv2.COLOR_BGR2GRAY)
    suave = cv2.GaussianBlur(self.imagenOtton,(5,5),cv2.BORDER_DEFAULT)
    (T,bin) = cv2.threshold(suave,160,255,cv2.THRESH_BINARY)
    (T,bin1) = cv2.threshold(suave,160,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Gaussian Blur",np.hstack((imagenOtton,bin)))
    #a = np.hstack([cv2.bitwise_and(imagenOtton,imagenOtton,mask=bin1),bin])
    cv2.imshow("Gaussian Blur",np.vstack([np.hstack([suave,bin]),np.hstack([bin1,suave])]))
    cv2.waitKey(0)



  def corte(self):
     self.tam = self.imagenOtton.shape
     self.bola = self.imagenOtton[int(self.tam[0]/2)+(valor):self.tam[0],int(self.tam[1]/2)+(valor):self.tam[1]]#centro da imagen
     #corte1 = imagenOtton[100:550,100:550 ] # Selecionar da linha 100 linha 550 e da coluna 100 ate a coluna 550
     cv2.imwrite("BZ_corte.jpg",self.bola)#Salvar imagen no disco
     cv2.imshow("RBG matriz 3x3",self.bola)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     return self.bola


  def canalAlpha(self):
   self.cotx = self.corte()
   self.tam = self.imagenOtton.shape

   mask = np.zeros(self.imagenOtton.shape[:2], np.uint8)
   bgdModel = np.zeros((1,65), np.float64)
   fgdModel = np.zeros((1,65), np.float64)
   rect = (250, 250, 450, 290)# Grabcut
   cv2.grabCut(self.imagenOtton, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

   r_channel, g_channel, b_channel = cv2.split(self.imagenOtton)
   a_channel = np.where((mask==2)|(mask==0),128,200).astype('uint8')
   img_RGBA = cv2.merge((r_channel, g_channel, b_channel, a_channel))
   cv2.imwrite("BZ_Alpha.jpg.png", img_RGBA)
   plt.imshow(img_RGBA)
   plt.show()



  def RGB_color(self):
     cotx = self.corte()
     for i in range(self.imagenOtton.shape[0]):
      for j in range(self.imagenOtton.shape[1]):
        #cotx.itemset((i,j,2),255)#azul#cotx.itemset((i,j,1),0)#Verde#cotx.itemset((i,j,0),0)#Vermelho
        self.imagenOtton.itemset((i,j,2),255)#azul
        self.imagenOtton.itemset((i,j,1),0)#Verde
        self.imagenOtton.itemset((i,j,0),0)#Vermelho
     cv2.imwrite("BZ_RGB.jpg",self.imagenOtton)#480 e 370
     cv2.imshow("RBG matriz 3x3",self.imagenOtton)
     cv2.waitKey(0)
     cv2.destroyAllWindows()


  def RGB_degrade_efetos(self):
     cotx = self.corte()
     for i in range(self.imagenOtton.shape[0]):
      for j in range(self.imagenOtton.shape[1]):
        #cotx.itemset((i,j,2),255)#azul#cotx.itemset((i,j,1),0)#Verde#cotx.itemset((i,j,0),0)#Vermelho
        self.imagenOtton[i,j] = (i%255,i%256,i%255)
     cv2.imwrite("BZ_RGB.jpg",self.imagenOtton)#480 e 370
     cv2.imshow("RBG matriz 3x3",self.imagenOtton)
     cv2.waitKey(0)


  def gacurte(self):
    # global imagenOtton
     mask = np.zeros(self.imagenOtton.shape[:2], np.uint8)
     bgdModel = np.zeros((1,65),np.float64)
     fgdModel = np.zeros((1,65),np.float64)
     rect = (100,100,550,490)

     cv2.grabCut(self.imagenOtton,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
     mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
     self.imagenOtton = self.imagenOtton * mask2 [:,:,np.newaxis]
     plt.imshow(self.imagenOtton)
     plt.colorbar()
     plt.show()



  def colar(self):
    cotx = self.corte()
    tam = self.imagenOtton.shape
    watch_face = self.imagenOtton[int(tam[0]/2):tam[0],int(tam[1]/2):tam[1]] #centro da Imagen
    self.imagenOtton[0:380,0:270] = watch_face
    cv2.imwrite("BZ_Colagem.jpg",self.imagenOtton)#380 e 270"
    plt.imshow(self.imagenOtton)
    plt.colorbar()
    plt.show()

# kernel_3x3 = np.ones((3,3),np.float32)/9
 #kernel_7x7 = np.ones((7,7),np.float32)/49

  def blur_Mediano(self):
    img = self.imagenOtton[::2,::2]#Diminuir a Imagen 1/4
    suave = np.vstack([
      np.hstack([img ,cv2.medianBlur(img,3)]),
      np.hstack([cv2.medianBlur(img,5),cv2.medianBlur(img,7)]),
      np.hstack([cv2.medianBlur(img,9),cv2.medianBlur(img,11)]),
      ])
    cv2.imshow("Imagen do Banco com Aplicação do Filtro Bilateral Blur",suave)
    cv2.waitKey(0)


  def blur_Bilateral(self):
   img = self.imagenOtton[::2,::2]#Diminuir a Imagen 1/4
   suave = np.vstack([
    np.hstack([img ,cv2.bilateralFilter(img,3, 21,21)]),
    np.hstack([cv2.bilateralFilter(img,5, 35, 35),cv2.bilateralFilter(img,7, 49 ,49)]),
    np.hstack([cv2.bilateralFilter(img,9,63,63),cv2.bilateralFilter(img,19,77,77)]),
   ])
   cv2.imshow("Imagen do Banco com Aplicação do Filtro Bilateral Blur",suave)
   cv2.waitKey(0)
   plt.title("Filtro Bilateral Blur")
   plt.subplot(121)
   plt.imshow(img)

   plt.title("Blur ")
   plt.subplot(122)
   plt.imshow(suave)
   plt.colorbar()
   plt.show()


  def blur(self):
   img = self.imagenOtton[::2,::2]#Diminuir a Imagen 1/4
   suave = np.vstack([
    np.hstack([img ,cv2.blur(img,(3,3))]),
    np.hstack([cv2.blur(img,(5,5)),cv2.blur(img,(7,7))]),
    np.hstack([cv2.blur(img,(9,9)),cv2.blur(img,(11,11))]),
   ])
   cv2.imshow("Imagen do Banco com Aplicação do Filtro blu",suave)
   cv2.waitKey(0)
   cv2.destroyAllWindows()



  def blur_GaussianBlur(self):
   #plt.subplot(121),plt.title("Original"),plt.imshow(imagenOtton)
    img = self.imagenOtton[::2,::2]#Diminuir a Imagen
    dts = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
    cv2.imshow("Gaussian Blur",np.hstack((img,dts)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

  def guadros_GaussianBlur(self):
     img = self.imagenOtton[::2,::2]#Diminuir a Imagen
     suave = np.vstack([
     np.hstack([img ,cv2.GaussianBlur(img,(3,3), 0)]),
     np.hstack([cv2.GaussianBlur(img,(5,5),0),cv2.GaussianBlur(img,(7,7),0)]),
     np.hstack([cv2.GaussianBlur(img,(9,9),0),cv2.GaussianBlur(img,(11,11),0)]),
     ])
     cv2.imshow("Imagen do Banco com Aplicação do Filtro Gaussiano",suave)
     cv2.waitKey(0)
     #plt.subplot(122)
     #plt.imshow(imagenOtton)
     #plt.title("GaussianBlur")
     #plt.show()



  def RGB_Corte_pente(self):
     cotx = self.corte()
     for i in range(cotx.shape[0]):
      for j in range(cotx.shape[1]):
        #cotx.itemset((i,j,2),255)#azul#cotx.itemset((i,j,1),0)#Verde#cotx.itemset((i,j,0),0)#Vermelho
        cotx.itemset((i,j,2),255)#azul
        cotx.itemset((i,j,1),0)#Verde
        cotx.itemset((i,j,0),0)#Vermelho
     cv2.imwrite("BZ_RGB.jpg",cotx )#480 e 370
     cv2.imshow("Corte_cor",cotx)
     cv2.waitKey(0)
     cv2.destroyAllWindows()



  def Circulo_listrado_raio(self):
     vermelho = (0,0,255)
     verde = (0,255,0)
     azul = (255,0,0)

     '''Circulo'''
     (X,Y) = (self.imagenOtton.shape[1] // 2,self.imagenOtton.shape[0] //2)
     print("Shape:=",self.imagenOtton.shape[1])

     for raio in range(200,300,5):
         cv2.circle(self.imagenOtton,(X,Y),raio,(0,0,255),1)
     cv2.imshow("Circulo",self.imagenOtton)
     cv2.waitKey(0)


  def linear(self):
    '''Linha'''
    cv2.line(self.imagenOtton,(0,0),(200,350),(0,255,0),10)
    cv2.line(self.imagenOtton,(250,250),(250,600),(0,0,255),10)
    cv2.imshow("Linha",self.imagenOtton)
    cv2.waitKey(0)

  def Retangulo(self,ops):
   if ops is 0:
    self.imagenOtton[0:100,0:100] = (255,0,0)
    #imagenOtton[:,0:100] = (128,128,255)
    cv2.imshow("Quadrado",self.imagenOtton)
    cv2.waitKey(0)
   else:
    cv2.rectangle(self.imagenOtton,(0,450),(250,600),(0,0,255),10)
    cv2.imshow("Quadrado",self.imagenOtton)
    cv2.waitKey(0)

  def Texto_escr(self,texto,RGB):
    #Texto
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(self.imagenOtton,texto,(0,150),fonte,2,RGB,4,cv2.LINE_AA)
    cv2.imshow("Escrita",self.imagenOtton)
    cv2.waitKey(0)



  def saturacao_mt(self):
    (canalAzul,canalVerde,canalVermelho) = cv2.split(self.imagenOtton)
    zeros = np.zeros(self.imagenOtton.shape[:2],dtype="uint8")

    cv2.imshow("vermelho",cv2.merge([zeros,zeros,canalVermelho]))
    cv2.imshow("verde",cv2.merge([zeros,canalVerde,zeros]))
    cv2.imshow("Azul",cv2.merge([canalAzul,zeros,zeros]))
    cv2.waitKey(0)

  def resize(self):
    cv2.imshow("Resizeoriginal",self.imagenOtton)
    cv2.waitKey(0)
    print("Resize... em 20% da Imagen = X=110")
    proporcao = 110.0/ self.imagenOtton.shape[1]#(Achar a propoção da altura em relação a Altura da imagen) #(P)= (AL / L)
    tamanho_novo = (110,int(self.imagenOtton.shape[0] * proporcao)) #PX = (AL * P)
    img_redimencionada = cv2.resize(self.imagenOtton,tamanho_novo,interpolation=cv2.INTER_AREA)#Calculo Matematico para interpolação (INTER_AREA)
    cv2.imshow("Resize_REdimencionada",img_redimencionada)
    print("Resize Suceful***")
    cv2.waitKey(0)
    def dados_resize():
        print("Propocao=",proporcao)
        print("Altura=",self.imagenOtton.shape[0] , "Largura",self.imagenOtton.shape[1])
        print("Tamanho Novo=",tamanho_novo)
        print("Imagen Final Redimencionada",img_redimencionada )
    dados_resize()

  def resize_Slicing(self):
    cv2.imshow("Resize_Original",self.imagenOtton)
    img_redimencionada = self.imagenOtton[::2,::2]#Regra = (Interpolação pega primeira linha ignora a segunda, depois pega a quarta e ignora)
    cv2.waitKey(0)
    print("1/4 da Imagen")
    cv2.imshow("Resize_Novo(Slicing)",img_redimencionada)
    cv2.waitKey(0)
    def dados_resize():
        print("Altura=",imagenOtton.shape[0] , "Largura",self.imagenOtton.shape[1])
        print("Tamanho Novo=",img_redimencionada)
        print("Altura=",img_redimencionada.shape[0] , "Largura",img_redimencionada.shape[1])
    dados_resize()

  def trasformacao_affinis(self):
    (alt , lar) = self.imagenOtton.shape[:2]#Captura alura e largura
    centro = (lar // 2,alt //2)#Acha o centro
    M= cv2.getRotationMatrix2D(centro,30,1.0)#30 Graus
    img_rotation = cv2.warpAffine(self.imagenOtton,M,(lar,alt))
    print("Conjunto Matriz 2D=",self.imagenOtton.shape[:2])
    print("Matriz",self.imagenOtton[:2,:2])
    print("Altura",alt,"Largura",lar)
    print("M Rotation",M)
    cv2.imshow("Resize_Novo(Slicing)",img_rotation)
    cv2.waitKey(0)




fil = Controle()
fil.tamanho_RGB()
#fil.Linarizar_canal()
#fil.corte()
#fil.canalAlpha()
#fil.RGB_color()
#fil.RGB_degrade_efetos()
#fil.gacurte()
#fil.colar()
#fil.blur_Mediano()
#fil.blur_Bilateral()
#fil.blur()
#fil.blur_GaussianBlur()
#fil.guadros_GaussianBlur()
#fil.RGB_Corte_pente()
#fil.Circulo_listrado_raio()
#fil.saturacao_mt()
#fil.resize()
#fil.resize_Slicing()
#fil.trasformacao_affinis()
'''Formas Geometricas'''
#fil.linear()
#fil.Retangulo(0)
#fil.Texto_escr("Allan",(0,0,255))

#histogrma() not
