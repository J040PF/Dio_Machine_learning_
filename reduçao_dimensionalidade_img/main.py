from PIL import Image

# Load image
img = Image.open('6.jpg')
img_width, img_height = img.size
data = list(img.getdata())

# Converter para escalas de cinza
'''converter utilizando metodo da media, coletando rgb de       cada pixel, e fazendo a media'''

for i in range(len(data)):
    gray_value = int((data[i][0] + data[i][1] + data[i][2]) / 3)
    data[i] = (gray_value, gray_value, gray_value)

# imagem cinza e salvar
img.putdata(data)
img.save('output_grayscale.jpg')

# converter para preto e branco
'''como sera preto e branco, ou seja binario, dividir o espectro de cor por dois, abaixo de 128 preto acima branco '''
threshold = 128

for i in range(len(data)):
    if data[i][0] < threshold:
        data[i] = (0, 0, 0)
    else:
        data[i] = (255, 255, 255)


# imagem preta e branca e salvar
img.putdata(data)
img.save('output.jpg')