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
def run(player1: str, player2: str) -> int:
    player1 = player1.lower()
    player2 = player2.lower()
    if player1 == player2:
        return 0
    elif player1 == 'rock' and player2 == 'scissors':
        return 1
    elif player1 == 'rock' and player2 == 'paper':
        return 2
    elif player1 == 'scissors' and player2 == 'rock':
        return 2
    elif player1 == 'scissors' and player2 == 'paper':
        return 1
    elif player1 == 'paper' and player2 == 'rock':
        return 1
    elif player1 == 'paper' and player2 == 'scissors':
        return 2
    else:
        return -1
    return winner


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez

# Made by DVS
