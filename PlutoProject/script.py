import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("qpsk_symbols.txt")

I = data[:, 0]
Q = data[:, 1]

plt.figure(figsize=(7, 7))
plt.scatter(I, Q, s=15, alpha=0.5)
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.title("QPSK Constellation Diagram")

plt.grid(True)
plt.axis("equal")
plt.show()
