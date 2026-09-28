import cv2
# leer la imagen con cv2 = computer vision
img = cv2.imread('perrodalmata.jpg')
# determinar el tipo de imagen numpy.ndarray
print(type(img))
# mostrar pixeles (554, 554, 3)
print(img.shape)
# mostrar imagen en ventana barra de titulo perro dalmata
cv2.imshow('perrodalmata', img)
## tiempo de espera
cv2.waitKey(0)
# destruir todas las ventana
cv2.destroyAllWindows()