#Importação da biblioteca openCV
import cv2
#Lendo a imagem
imagem = cv2.imread('imagens\\saida.jpg')
#Pegando a informação de cor do píxel na posição (0,0), note que 
# o formato de tuplas é essencial como destructuring e conseguir 
#a quantidade de vermelho, azul e verde da cor.
# Também note que o OpenCV é BGR e não RGB. 
(b, g, r) = imagem[0, 0]

print('O pixel(0, 0) tem as seguintes cores: ')
print('Vermelho: ', r, 'Verde: ', g, 'Azul: ', b)

#Primeiro loop, note que ele primeiro irá passar pelas colunas (imagem.shape[0])
for i in range(0, imagem.shape[0]):
    #Segundo loop, note que ele vai passar por toda linha da matriz de cada coluna.
    for j in range(0, imagem.shape[1]):
        #Agora, repetindo o uso de tuplas, iremos modificar todo píxel da imagem para azul 
        #(Formato BGR)
        imagem[i, j] = (255, 0, 0) 

#Mostrando a imagem.
cv2.imshow('Imagem modificada', imagem)
#Esperando fechar as janelas
cv2.waitKey(0)