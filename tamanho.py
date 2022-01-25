import cv2


def tamanho():
    imagem = cv2.imread("frutas.jpg")
    print(imagem.size)

def forma():
    imagem = cv2.imread("frutas.jpg")
    print(imagem.shape)
