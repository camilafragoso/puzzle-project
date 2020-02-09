import cv2
import numpy as np
from math import sqrt
import time

tempoi = time.time()
#carregando as imagem e as peças
#img = cv2.imread('imagem.jpg')
img = cv2.imread('testando/quebranovo.png')
cv2.imshow("imagem", img)
print(img.shape)
quebracabeca = cv2.imread("fundo.png")
#quebracabeca[0:quebracabeca.shape[0], 0:quebracabeca.shape[1]] = (255, 255, 255)

qtpecas = 20
'''pecas = []
for i in range(1, qtpecas+1):
    print("novas/" + str(i) + ".jpg")
    image = cv2.imread("testando/peca" + str(i) + ".png")
    pecas.append(image)'''

#ocupado = []
posicao = []
for m in range(1, qtpecas+1):
    peca = cv2.imread("testando/peca" + str(m) + ".png")
    pontos = []
    #checar = (0, 0)
    #pospeca = (0, 0)

    #quarentaporcentodex = (0.44) * (peca.shape[1])
    #sessentaporcentodex = (0.56) * (peca.shape[1])
    #quarentaporcentodey = (0.44) * (peca.shape[0])
    #sessentaporcentodey = (0.56) * (peca.shape[0])
    #for x in range(int(quarentaporcentodex), int(sessentaporcentodex)):
    #    for y in range(int(quarentaporcentodey), int(sessentaporcentodey)):
    #        p = (x, y)
    #        pontos.append(p)
    for x in range(0, peca.shape[1], 10):
        for y in range(0, peca.shape[0], 10):

            pixel = peca[y][x]
            if pixel[0] < 240 or pixel[1] < 240 or pixel[2] < 240:
                p = (x, y)
                pontos.append(p)

    print(len(pontos))


    '''for i in range(200):
        x = np.random.randint(peca.shape[1])
        y = np.random.randint(peca.shape[0])
        p = (x,y)
        pixel = peca[y][x]
        if pixel[0] > 240 and pixel[1] > 240 and pixel[2] > 240:
            i=i-1
        else:
            pontos.append(p)'''

    #percorrendo a imagem com as informações do contorno
    maxdif = 999999999
    dif = 0
    for i in range(0, img.shape[0] - peca.shape[0]):
        print(i)
        for j in range(0, img.shape[1] - peca.shape[1]):
            '''if pospeca[0] ==0 and pospeca[1] ==0:
                pixel_teste = quebracabeca[checar[1]][checar[0]]
                if pixel_teste[0] > 250 and pixel_teste[1] > 250 and pixel_teste[2] > 250:
                    i = i+peca.shape[0]
                    j = i+peca.shape[1]
                    break'''
        #for j in range(0, 3):
            dif = float(0)
            #for k in range(0,len(contornos1[0]),10):
            for k in range(len(pontos)):
                #ponto = contornos1[0][k]
                ponto = pontos[k]
                #ponto = ponto[0]
                x = ponto[0]
                y = ponto[1]

                #print(k, ":", y, x, peca[y][x])

                pixel_img = img[y+i][x+j]
                pixel_peca = peca[y][x]

                #if abs(pixel_img[0]-pixel_peca[0]) > maxdif or abs(pixel_img[1]-pixel_peca[1]) > maxdif or abs(pixel_img[2]-pixel_peca[2]) > maxdif:
                #    dif = 999999999
                #    break
                #else:
                #print(pixel_img[0],pixel_img[1],pixel_img[2],pixel_peca[0],pixel_peca[1],pixel_peca[2])

                parter = (float(pixel_img[0])-float(pixel_peca[0]))**2
                parteg = (float(pixel_img[1]) - float(pixel_peca[1])) ** 2
                parteb = (float(pixel_img[2]) - float(pixel_peca[2])) ** 2

                dif = dif + parter + parteg + parteb

                #cv2.waitKey(0);


            if dif < maxdif:
                maxdif = dif
                pospeca = (i, j)
                #print(i, j, maxdif)


    posicao.append(pospeca)
    print(pospeca)

    '''for i in range(0, 500, 100):
        sair = False
        for j in range(0, 400, 100):
            p = 
            if i<pospeca[0]<i+100 and j<pospeca[1]<j+100:
                quebracabeca[i+30:i+30+peca.shape[0], j+30:j+30+peca.shape[1]] = peca
                cv2.imshow("teste1", quebracabeca)
                cv2.waitKey(10)
                ocupado.append(pospeca)
                sair = True
                break
        if sair ==True: break'''

    #printando o contorno no lugar da peça no quebra cabeça
    po = posicao[m-1]
    pr = ((po[0]+pospeca[0]+10), (po[1]+pospeca[1]+10))
    quebracabeca[pr[0]:pr[0]+peca.shape[0], pr[1]:pr[1]+peca.shape[1]] = peca
    cv2.imshow("teste1", quebracabeca)
    cv2.waitKey(10)

tempof = time.time()
tempo = tempof - tempoi
print (posicao)
print (tempo)
cv2.waitKey(0)