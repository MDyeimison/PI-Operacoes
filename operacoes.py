import numpy as np
from PIL import Image

def showImage(array, txt):
    pil_image=Image.fromarray(array)
    pil_image.save(txt + '.png')

def plageRat(img, img2):
    ar = np.array(img)
    ar2 = np.array(img2)
    h, w = ar.shape
    h2, w2 = ar2.shape

    B = np.zeros((h, w))
    B2 = np.zeros((h2, w2))
    B[0:h, 0:w] = ar[0:h, 0:w]
    B2[0:h2, 0:w2] = ar2[0:h2, 0:w2]

    B = B.astype(np.uint8)
    B2 = B2.astype(np.uint8)
    subtraction(B, B2)
    addiction(B, B2)
    reflection(B)

def subtraction(B, B2):
    h, w = B.shape
    aux = np.zeros((h, w))

    aux[0:h, 0:w] = B[0:h, 0:w] - B2[0:h, 0:w]
    aux = aux.astype(np.uint8)
    txt = 'sub'
    showImage(aux, txt)

def addiction(B, B2):
    h, w = B.shape
    aux = np.zeros((h, w))

    aux[0:h, 0:w] = (B[0:h, 0:w] + B2[0:h, 0:w])//2
    aux = aux.astype(np.uint8)
    txt = 'add'
    showImage(aux, txt)


def reflection(B):
    h, w = B.shape
    aux = np.zeros((h, w))

    aux[0:h, 0:w:] = np.flip(B[::-1])
    #aux = np.flip(B)
    aux = aux.astype(np.uint8)
    txt = 'reflec'
    showImage(aux, txt)


img = Image.open(r"/home/marc/Documents/UFT/5 PERIODO/Processamento de Imagens/trab PI/trab PI - Operacoes/imagem1.jpg").convert('L')
img2 = Image.open(r"/home/marc/Documents/UFT/5 PERIODO/Processamento de Imagens/trab PI/trab PI - Operacoes/imagem2.jpg").convert('L')
plageRat(img, img2)