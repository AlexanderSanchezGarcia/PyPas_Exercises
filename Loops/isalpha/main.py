# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha actual: 2024/10/10
def run(text: str) -> bool:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    isalpha = True
    for letter in text:
        if letter.lower() not in ALPHABET:
            isalpha = False
            break
    return isalpha


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
