#Importando Biblióteca
import cv2
#Lendo imagem
imagem = cv2.imread('imagens\\saida.jpg')
#Primeiro loop, passando pelas colunas
for i in range(0, imagem.shape[0]):
    #Segundo loop, passando pelas linhas
    for j in range(0, imagem.shape[1]):
        #Modificando a cor em tons de verde.
        imagem[i, j] = (0, (i*j)%256, 0)
#Mostrando a imagem
cv2.imshow('Imagem modificada', imagem)
#Esperando fechar as janelas
cv2.waitKey(0)
