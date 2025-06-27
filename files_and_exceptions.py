def read_file_to_dict(filename):
    with open(filename,'r') as f:
        file = f.read()
    file = file.split(';')
    file_dict = {}
    for item in file:
        if item.strip() != '':
            item = item.split(':')
            if item[0] in file_dict:
                file_dict[item[0]].append(float(item[1]))
            else:
                file_dict[item[0]] = [float(item[1])]
    return file_dict

def process_dict(data):
    for producto, ventas in data.items():
        total = sum(ventas)
        promedio = total / len(ventas)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
