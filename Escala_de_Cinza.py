import cv2
import numpy as np

# Carregar a imagem
imagem_original = cv2.imread('/Users/andersonmarques/Documents/01 - Documentos Pessoais/Eu.jpeg') 

# Converter para níveis de cinza
imagem_cinza = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)

# Aplicar binarização (limiar de 127, ajuste conforme necessário)
_, imagem_binaria = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

# Salvar as imagens resultantes
cv2.imwrite('lena_cinza.jpg', imagem_cinza)
cv2.imwrite('lena_binaria.jpg', imagem_binaria)

# Exibir as imagens (opcional, para visualização)
cv2.imshow('Imagem Original', imagem_original)
cv2.imshow('Imagem Cinza', imagem_cinza)
cv2.imshow('Imagem Binária', imagem_binaria)
cv2.waitKey(0)
cv2.destroyAllWindows()