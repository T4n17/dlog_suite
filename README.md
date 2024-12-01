# Discrete Logarithm Algorithm Suite

A Python implementation of various algorithms for solving the discrete logarithm problem. This suite provides efficient solutions for finding x in the equation g^x ≡ h (mod p).

## Algorithms

### Baby-Step Giant-Step (BSGS)
- Time complexity: O(√n) where n is the group order
- Memory complexity: O(√n)
- Best suited for medium-sized prime moduli
- Uses a space-time tradeoff approach

### Pollard's Rho
- Probabilistic algorithm with expected runtime O(√n)
- Low memory requirements: O(1)
- Particularly effective for medium-sized groups
- Uses random walks to find collisions

### Pohlig-Hellman
- Reduces the discrete log problem in a group to smaller subgroups
- Very efficient when the group order factors into small primes
- Combines results using the Chinese Remainder Theorem
- Time complexity depends on the largest prime factor of the group order

## Dependencies
- Python 3.x
- Only uses the built-in `math` library

## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/dlog_suite.git
cd dlog_suite
```

## Usage Examples

### Basic Usage
```python
import dlog_suite

# Find x where 5448^x ≡ 6909 (mod 11251)
result = dlog_suite.pohlig_hellman(5448, 6909, 11251)
print(result)  # Output: 511

# Verify the result
verification = pow(5448, 511, 11251)
print(verification)  # Output: 6909
```

### Choosing the Right Algorithm

1. For small to medium groups with sufficient memory:
```python
x = dlog_suite.BSGS(g, h, p)
```

2. For medium-sized groups with memory constraints:
```python
x = dlog_suite.pollard_p(g, h, p)
```

3. For groups with smooth order (factors into small primes):
```python
x = dlog_suite.pohlig_hellman(g, h, p)
```

## Helper Functions

The suite also includes several useful helper functions:
- `GCD(a, b)`: Computes greatest common divisor
- `XGCD(a, b)`: Extended Euclidean algorithm
- `ElementOrder(x, p)`: Computes multiplicative order
- `GroupOrder(n)`: Calculates group order
- `PrimeFactorization(n)`: Returns prime factors
- `CRT(x, q, N)`: Chinese Remainder Theorem implementation

## Performance Considerations

- BSGS is memory-intensive but deterministic
- Pollard's Rho is memory-efficient but probabilistic
- Pohlig-Hellman's performance heavily depends on the group order's factorization
