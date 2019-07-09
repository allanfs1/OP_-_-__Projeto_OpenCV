import cv2
import numpy as np

img = cv2.imread("C:/Users/Allan/Documents/Allan/OPenCV/Opencv/foto2.jpg")

cv2.imshow("img_foto",img)
cv2.waitKey(0)


def algoritmo(pxr,pxg,pxb):
    return (pxr + pxg + pxb) / 3

def algoritmo_blur(pxes,pxdi,pxci,pxba):
    return  (pxes + pxdi + pxci + pxba) / 4


def algoritmo_Negativo(pxes,pxdi,pxci,pxba):
    return  (8-(pxes + pxdi + pxci + pxba) / 4)

#Regra de Três
def pect(rgb):
    conta=[]
    for i in range(len(rgb)):
      conta.append((rgb[i] * 255)/100)
    return conta


def  algoritmo_Real(px,brilho):
    if(brilho == True):
       if(px >= 240):
        return px
       else:
        px+=15
        return px
    else:
       if(px >= 240):
         return px
       else:
         px-=10
         return px

def algoritmo_Contraste():
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0,4) * 255.0, 0, 255)
    res = cv2.LUT(img, lookUpTable)
    cv2.imshow("Gray",res)
    cv2.waitKey(0)



'''Converte foto em tons de cinza'''
def gray():
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
         img.itemset(i,j,0,algoritmo(img.item(i,j,0),img.item(i,j,1),img.item(i,j,2)))
         img.itemset(i,j,1,algoritmo(img.item(i,j,0),img.item(i,j,1),img.item(i,j,2)))
         img.itemset(i,j,2,algoritmo(img.item(i,j,0),img.item(i,j,1),img.item(i,j,2)))
    cv2.imshow("Gray",img)
    cv2.waitKey(0)

''' Desfoque blur'''
def blur():
    for i in range(int(img.shape[0]-10)):
        for j in range(int(img.shape[1]-10)):
         img.itemset(i,j,0,algoritmo_blur(img.item(i-1,j-1,0),img.item(i+2,j+2,0),img.item(i+1,j+2,0),img.item(i+1,j-2,0)))
         img.itemset(i,j,1,algoritmo_blur(img.item(i-1,j-1,1),img.item(i+2,j+2,1),img.item(i+1,j+2,1),img.item(i+1,j-2,1)))
         img.itemset(i,j,2,algoritmo_blur(img.item(i-1,j-1,2),img.item(i+2,j+2,2),img.item(i+1,j+2,2),img.item(i+1,j-2,2)))
    cv2.imshow("Gray",img)
    cv2.waitKey(0)

'''Negativo'''
def Negativo():
    for i in range(int(img.shape[0]-10)):
        for j in range(int(img.shape[1]-10)):
         img.itemset(i,j,0,algoritmo_Negativo(img.item(i-1,j-1,0),img.item(i+2,j+2,0),img.item(i+1,j+2,0),img.item(i+1,j-2,0)))
         img.itemset(i,j,1,algoritmo_Negativo(img.item(i-1,j-1,1),img.item(i+2,j+2,1),img.item(i+1,j+2,1),img.item(i+1,j-2,1)))
         img.itemset(i,j,2,algoritmo_Negativo(img.item(i-1,j-1,2),img.item(i+2,j+2,2),img.item(i+1,j+2,2),img.item(i+1,j-2,2)))
    cv2.imshow("Gray",img)
    cv2.waitKey(0)



def Real():
    rgb = pect((10,50,70))
    for i in range(int(img.shape[0]-10)):
      for j in range(int(img.shape[1]-10)):
        img.itemset(i,j,0,algoritmo_Real(img.item(i,j,0),False))
        img.itemset(i,j,1,algoritmo_Real(img.item(i,j,1),False))
        img.itemset(i,j,2,algoritmo_Real(img.item(i,j,2),False))




algoritmo_Contraste()
#gray()
#blur()
#Negativo()
