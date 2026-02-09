import sys
import math

def main():
    m, b = map(int, sys.stdin.readline().split())
    weights = list(map(int, sys.stdin.readline().split()))
    
    if m == 0:
        print(0)
        print()
        return
    
    # Compute the residues modulo b
    residues = [w % b for w in weights]
    
    # Compute GCD of all residues
    current_gcd = residues[0]
    for r in residues[1:]:
        current_gcd = math.gcd(current_gcd, r)
    
    # Compute GCD with b
    final_gcd = math.gcd(current_