#Importação da biblioteca OpenCV
import cv2

#cv2.imread() é um método que pega uma imagem do seu computador e a converte
#para uma matriz tridimensional, com as informações de cada pixel:
#cor, posição vertical e posição horizontal.
imagem = cv2.imread('imagens\\dados.png')

print('Largura em pixels: ',end='')
#imagem.shape[1] é um atributo da matriz, que significa a largura da imagem em pixels.
print(imagem.shape[1]) 
print('Altura em pixels: ',end='')
#imagem.shape[0] é um atributo da matriz, que significa a altura da imagem em pixels.
print(imagem.shape[0]) 
print('Qtde de canais: ',end='')
#Significa quantos canais de cor a matriz tem, no caso de uma imagem RGB, terá 3 canais de cores.
print(imagem.shape[2]) 

#O método cv2.imshow() é o que possibilita a visualização da imagem.
cv2.imshow("Nome da janela", imagem) 
#O método cv2.waitKey() para o programa até receber um input do teclado, 
# como colocamos 0, o programa para até as janelas serem fechadas.
cv2.waitKey(0)

#O método cv2.imwrite() serve justamente para salvar a imagem no seu computador, sendo bastante útil 
# quando modificamos a imagem e queremos salvar o resultado.
cv2.imwrite('imagens\\saida.jpg', imagem) 
