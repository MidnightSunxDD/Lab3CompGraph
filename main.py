from PIL import Image
import numpy

if __name__ == '__main__':

    angle = numpy.deg2rad(10 * (3 + 1))
    matrix = numpy.matrix([[numpy.cos(angle), numpy.sin(angle), 0],
                           [-numpy.sin(angle), numpy.cos(angle), 0],
                           [480 * (1 - numpy.cos(angle)) + 480 * numpy.sin(angle),
                            480 * (1 - numpy.cos(angle)) - 480 * numpy.sin(angle), 1]])

    with open('matrix.txt', 'w+') as fm:
        for line in matrix:
            numpy.savetxt(fm, line, fmt='%.2f')

    image_before = Image.new('RGB', (960, 960), (255, 255, 255))
    with open('DS3.txt', 'r') as dsf:
        for line in dsf:
            x, y = [int(t) for t in line.split()]
            image_before.putpixel((x, y), (0, 0, 0))
    image_before.save('first.png')
    image_before.close()

    image_after = Image.new('RGB', (960, 960), (255, 255, 255))
    with open('DS3.txt', 'r') as dsf:
        for line in dsf:
            x, y = [int(t) for t in line.split()]
            nx = round(x * matrix.item(0, 0) + y * matrix.item(1, 0) + matrix.item(2, 0))
            ny = round(x * matrix.item(0, 1) + y * matrix.item(1, 1) + matrix.item(2, 1))
            image_after.putpixel((nx, ny), (0, 0, 255))
    image_after.save('second.png')
    image_after.close()
