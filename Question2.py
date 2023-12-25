def square_and_multiply(x, b, n):
    result = 1
    x = x % n  # Réduire x modulo n pour optimiser le calcul
    while b > 0:
        # Si le bit de poids faible de b est 1, multiplier le résultat actuel par x modulo n
        if b % 2 == 1:
            result = (result * x) % n
        # Élever x au carré modulo n
        x = (x * x) % n
        # Diviser b par 2 (décaler les bits vers la droite)
        b = b // 2
    return result
# Demander à l'utilisateur d'entrer les valeurs
x = int(input("Entrez la valeur de x : "))
b = int(input("Entrez la valeur de b : "))
n = int(input("Entrez la valeur de n : "))
# Appeler la fonction et afficher le résultat
resultat = square_and_multiply(x, b, n)
print(f"Le résultat de ({x}^{b} mod {n}) est : {resultat}")
