#Importando biblioteca
import cv2
#Lendo a imagem
imagem = cv2.imread('imagens\\saida.jpg')
#loop passando por cada coluna, indo de 10 a 10 píxels.
for i in range(0, imagem.shape[0], 10):
    #loop passando por cada linha, indo de 10 a 10 píxels.
    for j in range(0, imagem.shape[1], 10):
        #Criando um quadrado de 2 píxels de lado.
        #Note que a tupla representa (0, 255, 255), logo apresenta a maior tonalidade de verde
        #e de vermelho ao mesmo tempo, resultando na cor amarela.
        imagem[i: i+1, j: j+1] = (0, 255, 255)
#Demonstrando a imagem
cv2.imshow('Imagem modificada', imagem)
#Esperando fechar as janelas.
cv2.waitKey(0)