def feistel_key_generation(key, permutation, left_shift, right_shift):
    # Appliquer la permutation à la clé
    permuted_key = [key[permutation[i]] for i in range(len(permutation))]
    # Diviser la clé permutée en deux blocs de 4 bits
    k1 = permuted_key[:4]
    k2 = permuted_key[4:]
    # Calculer k1 et k2 selon les opérations spécifiées
    k1 = [k1[i] ^ k2[i] for i in range(4)]
    k2 = [(k2[i] & k1[i]) for i in range(4)]
    # Appliquer les décalages
    k1 = k1[left_shift:] + k1[:left_shift]
    k2 = k2[-right_shift:] + k2[:-right_shift]
    return k1, k2
key = [1, 0, 1, 0, 0, 1, 1, 0]
permutation = [6, 5, 2, 7, 4, 1, 3, 0] # Fonction de permutation
left_shift = 2
right_shift = 1
subkey1, subkey2 = feistel_key_generation(key, permutation, left_shift, right_shift)
print("Sous-clé 1:", subkey1)
print("Sous-clé 2:", subkey2)
def feistel_cipher(input_block, permutation, left_shift, right_shift, k1, k2):
    # Appliquer la permutation à l'entrée
    permuted_input = [input_block[permutation[i]] for i in range(len(permutation))]
    # Diviser l'entrée permutée en deux blocs de 4 bits
    g0 = permuted_input[:4]
    d0 = permuted_input[4:]
    # Premier Round
    d1 = [g0[i] ^ k1[i] for i in range(4)]
    g1 = [d0[i] ^ (g0[i] | k1[i]) for i in range(4)]
    # Deuxième Round
    d2 = [g1[i] ^ k2[i] for i in range(4)]
    g2 = [d1[i] ^ (g1[i] | k2[i]) for i in range(4)]
    # Concaténer les résultats du deuxième Round
    ciphertext = g2 + d2
    # Appliquer l'inverse de la permutation à C
    inverse_permutation = [permutation.index(i) for i in range(len(permutation))]
    ciphertext = [ciphertext[inverse_permutation[i]] for i in range(len(inverse_permutation))]
    return ciphertext
input_block = [1, 0, 1, 0, 0, 1, 1, 0]  # Bloc N de longueur 8
permutation = [4, 6, 0, 2, 7, 3, 1, 5]  # Permutation spécifiée (π = 46027315)
left_shift = 2
right_shift = 1
k1 = [1, 1, 1, 1]  # Sous-clé k1 de longueur 4
k2 = [1, 0, 0, 0]  # Sous-clé k2 de longueur 4
ciphertext = feistel_cipher(input_block, permutation, left_shift, right_shift, k1, k2)
print("Texte clair:", input_block)
print("Texte chiffré:", ciphertext)
def feistel_decipher(ciphertext, permutation, left_shift, right_shift, k1, k2):
    # Appliquer l'inverse de la permutation à C
    inverse_permutation = [permutation.index(i) for i in range(len(permutation))]
    ciphertext = [ciphertext[inverse_permutation[i]] for i in range(len(inverse_permutation))]
    # Diviser C en deux blocs de 4 bits
    g2 = ciphertext[:4]
    d2 = ciphertext[4:]
    # Deuxième Round
    g1 = [d2[i] ^ k2[i] for i in range(4)]
    d1 = [g2[i] ^ (g1[i] | k2[i]) for i in range(4)]
    # Premier Round
    g0 = [d1[i] ^ k1[i] for i in range(4)]
    d0 = [g1[i] ^ (g0[i] | k1[i]) for i in range(4)]
    # Concaténer les résultats du premier Round
    plaintext = g0 + d0
    return plaintext
ciphertext = [1, 1, 0, 1, 0, 0, 1, 0]  # Bloc C de longueur 8
permutation = [4, 6, 0, 2, 7, 3, 1, 5]  # Permutation spécifiée (π = 46027315)
left_shift = 2
right_shift = 1
k1 = [1, 1, 1, 1]  # Sous-clé k1 de longueur 4
k2 = [1, 0, 0, 0]  # Sous-clé k2 de longueur 4
plaintext = feistel_decipher(ciphertext, permutation, left_shift, right_shift, k1, k2)
print("Texte déchiffré:", plaintext)