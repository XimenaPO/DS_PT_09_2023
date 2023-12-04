"""Visualizaciones para ilustrar seaborn, líneas de referencia e itertools."""

import itertools

import matplotlib.pyplot as plt
import seaborn as sns


def reg_resid_plots(data):
    """
    Usando `seaborn`, traza los gráficos de regresión y residuos
    lado a lado para cada permutación de 2 columnas en los datos.
    
    Parámetros:
        - Datos: Un `pandas.DataFrame`.

    Devuelve:
        Un objeto `Axes` de matplotlib.
    """
    num_cols = data.shape[1]
    permutation_count = num_cols * (num_cols - 1)

    fig, ax = plt.subplots(permutation_count, 2, figsize=(15, 8))

    for (x, y), axes, color in zip(
        itertools.permutations(data.columns, 2), 
        ax,
        itertools.cycle(['royalblue', 'darkorange'])
    ):
        for subplot, func in zip(axes, (sns.regplot, sns.residplot)):
            func(x=x, y=y, data=data, ax=subplot, color=color)

            if func == sns.residplot:
                # marcar los residuos como tales
                subplot.set_ylabel('residuals')
    return fig.axes


def std_from_mean_kde(data):
    """
    Trazar el KDE junto con las líneas verticales de referencia
    para cada desviación estándar de la media.
    
    Parámetros:
        - Datos: `pandas.Series` con datos numéricos
    
    Devuelve:
        Objeto `Axes` de Matplotlib.
    """
    mean_mag, std_mean = data.mean(), data.std()
    
    ax = data.plot(kind='kde')
    ax.axvline(mean_mag, color='b', alpha=0.2, label='mean')
    
    colors = ['green', 'orange', 'red']
    multipliers = [1, 2, 3]
    signs = ['-', '+']
    linestyles = [':', '-.', '--']
    
    for sign, (color, multiplier, style) in itertools.product(
        signs, zip(colors, multipliers, linestyles)
    ):
        adjustment = multiplier * std_mean
        if sign == '-':
            value = mean_mag - adjustment
            label = '{} {}{}{}'.format(
                r'$\mu$',
                r'$\pm$',
                multiplier,
                r'$\sigma$'
            )
        else:
            value = mean_mag + adjustment
            label = None
        ax.axvline(value, color=color, linestyle=style, label=label, alpha=0.5)
    
    ax.legend()
    return ax