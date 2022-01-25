import cv2


def segmentacao_rgb():
    imagem = cv2.imread("frutas.jpg")
    azul, verde, vermelho = cv2.split(imagem)

    imagem = cv2.merge((azul, verde, vermelho))
    cv2.imshow("Imagem", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def segmentacao_g():
    imagem = cv2.imread("frutas.jpg")
    azul, verde, vermelho = cv2.split(imagem)

    cv2.imshow("Canal G", verde)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def segmentacao_b():
    imagem = cv2.imread("frutas.jpg")
    azul, verde, vermelho = cv2.split(imagem)

    cv2.imshow("Canal B", azul)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def segmentacao_r():
    imagem = cv2.imread("frutas.jpg")
    azul, verde, vermelho = cv2.split(imagem)

    cv2.imshow("Canal R", vermelho)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def rgb_para_tons_cinza():
    imagem = cv2.imread("frutas.jpg")

    imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    cv2.imshow("Imagem", imagem)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
