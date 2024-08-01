# Python Algorithm Suite for Solving Discrete Logarithms
## Included Algorithms:
- Baby Step Giant Step Algorithm
- Pollard's Rho Algorithm
- Pohlig-Hellman Algorithm
## Dependencies:
The Python script doesn't use any dependencies except the built-in math library.
## Usage:
To use, simply import the script into a Python interpreter and use the functions.\
Example:\
`import dlog_suite`\
`dlog_suite.pohlig_hellman(5448, 6909, 11251)`\
`511`\
To verify that it is correct:\
`pow(5448,511,11251)`\
`6909`
