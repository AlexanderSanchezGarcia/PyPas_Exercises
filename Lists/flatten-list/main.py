# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/16
# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(elements: list) -> list:
    flatten_elements = []
    for element in elements:
        if isinstance(element, list):  
            flatten_elements.extend(element)
        else:
            flatten_elements.append(element)
    return flatten_elements

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez

# Made by DVS
