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
def run(values: list) -> list:
    # Crear una lista con solo los números impares manteniendo el orden original
    odds = []
    for value in values:
        if value % 2 != 0 and value not in odds:  # Evitar duplicados
            odds.append(value)
    return odds

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez

# Made by DVS
