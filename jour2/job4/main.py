N = int(input("Enter a positive integer (N): "))

# Vérifier que N est supérieur à zéro
if N > 0:
    # Afficher les tables de multiplication de 1 à N
    for i in range(1, N + 1):
        print(f"\nMultiplication table for {i} :\n")
        for j in range(1, 11):
            result = i * j
            print(f"{i} x {j} = {result}")
else:
    print("Please enter a positive integer.")