def array_show(array_2d):
    for i in range(len(array_2d)):
        for j in range(len(array_2d[i])):
            print(array_2d[i][j], end='')
        print()

def array_create(rows, lines):
    array_2d = [[" "] * rows for i in range(lines)]
    return array_2d

def array_edit(array_2d):
    filename = "elbitsystems_clean.bin"

    with open(filename,"rb") as file:
        while (bytes := file.read(6)):
            if bytes[0] == 0x3f and bytes[2] == 0x40:
                if bytes[5] == 0:
                    sign = " "
                if bytes[5] == 1 or bytes[5] == 4:
                    sign = ","
                if bytes[5] == 2:
                    sign = "%"
                if bytes[5] == 16:
                    sign = "#"
                if bytes[5] == 32:
                    sign = "("
                if bytes[5] == 64:
                    sign = "/"
                if bytes[5] == 128:
                    sign = "*"
                array_2d[bytes[3]][bytes[1]] = sign
    return a

a = array_create(200, 30)
array_edit(a)
array_show(a)