def towerOfHanoi(n, A, B, C):
    if n == 0:
        return
    
    towerOfHanoi(n-1, A, C, B)
    print(f"Move a Disc from {A} to {C}")
    towerOfHanoi(n-1, B, A, C)

towerOfHanoi(3, 1, 2, 3)