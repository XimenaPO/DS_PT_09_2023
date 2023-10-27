"""Ayudas visuales para la simulación"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def show_distributions():
    """Genera un gráfico para cada una de las distribuciones utilizadas en la simulación."""

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    fig.delaxes(axes[-2])

    # distribución triangular definida por el mínimo (a), el máximo (b) y la moda
    a, b, mode = 1.5, 5, 2.75
    peak = 2 / (b - a)# peak of PDF is at 2/(b-a)
    axes[0].plot([a, mode, b], [0, peak, 0])
    axes[0].set_title('Triangular PDF')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('densidad')
    axes[0].annotate('min', xy=(a, 0), xytext=(a + 1, 0), arrowprops=dict(arrowstyle='->'))
    axes[0].annotate('max', xy=(b, 0), xytext=(b - 1.25, 0), arrowprops=dict(arrowstyle='->'))
    axes[0].annotate('peak', xy=(mode, peak), xytext=(mode - 0.2, peak - 0.2), arrowprops=dict(arrowstyle='->'))

    # distribución uniforme definida por min (a) y max (b)
    a, b = 0, 1
    peak = 1 / (b - a)
    axes[1].plot([a, a, b, b], [0, peak, peak, 0])
    axes[1].set_title('Uniform PDF')
    axes[1].set_ylabel('densidad')
    axes[1].set_xlabel('x')
    axes[1].annotate('min', xy=(a, peak), xytext=(a + 0.2, peak - 0.2), arrowprops=dict(arrowstyle='->'))
    axes[1].annotate('max', xy=(b, peak), xytext=(b - 0.3, peak - 0.2), arrowprops=dict(arrowstyle='->'))
    axes[1].set_ylim(0, 1.5)

    # gaussiana
    mu, sigma = 1.01, 0.01
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    axes[2].plot(x, stats.norm.pdf(x, mu, sigma) / 100)
    axes[2].set_title('Gaussian PDF')
    axes[2].set_ylabel('densidad')
    axes[2].set_xlabel('x')
    axes[2].annotate(r'$\mu$', xy=(mu, 0.4), xytext=(mu - 0.001, 0.3), arrowprops=dict(arrowstyle='->'))
    axes[2].annotate(
        '', xy=(mu-sigma, 0.25), xytext=(mu + 0.01, 0.25),
        arrowprops=dict(arrowstyle='|-|, widthB=0.5, widthA=0.5')
    )
    axes[2].annotate(r'$2\sigma$', xy=(mu - 0.002, 0.22))

    # exponencial
    x = np.linspace(0, 5, 100)
    axes[3].plot(x, stats.expon.pdf(x, scale=1/3))
    axes[3].set_title('Exponential PDF')
    axes[3].set_ylabel('densidad')
    axes[3].set_xlabel('x')
    axes[3].annotate(r'$\lambda$ = 3', xy=(0, 3), xytext=(0.5, 2.8), arrowprops=dict(arrowstyle='->'))

    # Poisson PMF (función de masa de probabilidad) porque se trata de una variable aleatoria discreta
    x = np.arange(0, 10)
    axes[5].plot(x, stats.poisson.pmf(x, mu=3), linestyle='--', marker='o')
    axes[5].set_title('Poisson PMF')
    axes[5].set_ylabel('mass')
    axes[5].set_xlabel('x')
    axes[5].annotate(r'$\lambda$ = 3', xy=(3, 0.225), xytext=(1.9, 0.2), arrowprops=dict(arrowstyle='->'))

    plt.suptitle('Comprender las distribuciones utilizadas para la simulación', fontsize=15, y=0.95)

    return axes