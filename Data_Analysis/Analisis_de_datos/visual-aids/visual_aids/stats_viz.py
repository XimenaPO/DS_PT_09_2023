"""Funciones para crear ayudas visuales para conceptos estadísticos."""

import itertools
import pkg_resources

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import bernoulli, binom, expon, poisson, norm, skewnorm
import seaborn as sns
from sklearn.metrics import r2_score
from statsmodels.distributions.empirical_distribution import ECDF
from statsmodels.tsa.seasonal import seasonal_decompose

def _non_symmetric_data():
    """Generar datos no simétricos para gráficos"""
    # generar datos
    np.random.seed(0)
    return pd.Series(
        np.random.gamma(7, 5, size=1000) * np.random.choice([-2.2, -1.85, 0, -0.4, 1.33], size=1000), name='x'
    )

def _despine(ax):
    """Quitar los lomos superior y derecho de un objeto Axes de matplotlib"""
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

def anscombes_quartet(r_squared=False):
    """Traza el Cuarteto de Anscombe junto con estadísticas resumidas."""

    # obtener datos
    anscombe = sns.load_dataset('anscombe').groupby('dataset')

    # definir subtramas y títulos
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    axes = axes.flatten()
    titles = ['linear', 'non-linear', 'linear with outlier', 'vertical with outlier']

    for ax, (group_name, group_data), title in zip(axes, anscombe, titles):
        # obtener x, y
        x, y = group_data.x, group_data.y

        # hacer un diagrama de dispersión
        ax.scatter(x, y)

        # añadir título y etiquetas
        ax.set_title(f'{group_name} - {title}')
        ax.set_xlabel('x')
        ax.set_ylabel('y')

        # alinear los límites de los ejes
        ax.set_xlim((3, 19.5))
        ax.set_ylim((2, 13))

        # trazar la recta de regresión
        m, b = np.polyfit(x, y, 1)
        reg_x = np.append([0, 20], x)
        reg_y = [m*num + b for num in reg_x]
        ax.plot(reg_x, reg_y, 'r--')

        # anotar las estadísticas resumidas
        if r_squared:
            ax.annotate(
                f"""ρ = {np.corrcoef(x,y)[0][1]:.2f}\ny = {m:.2f}x + {b:.2f}\n\n{
                    r'$R^2$'
                } = {r2_score(y, [m*num + b for num in x]):.2f}\n\n{
                    r'$μ_x$'
                } = {np.mean(x):.2f} | {
                    r'$σ_x$'
                } = {np.std(x):.2f}\n{
                    r'$μ_y$'
                } = {np.mean(y):.2f} | {r'$σ_y$'} = {np.std(y):.2f}""", xy=(13, 2.5)
            )
        else:
            ax.annotate(
                f"""ρ = {np.corrcoef(x,y)[0][1]:.2f}\ny = {m:.2f}x + {b:.2f}\n\n{
                    r'$μ_x$'
                } = {np.mean(x):.2f} | {
                    r'$σ_x$'
                } = {np.std(x):.2f}\n{
                    r'$μ_y$'
                } = {np.mean(y):.2f} | {r'$σ_y$'} = {np.std(y):.2f}""", xy=(13, 2.5)
            )

    # dar un título a las parcelas
    plt.suptitle("Anscombe's Quartet", fontsize=16, y=0.95)

    return axes

def datasaurus_dozen():
    """
    Mostrar el conjunto de datos Datasaurus Dozen
    
    Puesto original de Datasaurus: http://www.thefunctionalart.com/2016/08/download-datasaurus-never-trust-summary.html
    Docena de Datasaurus: https://www.autodeskresearch.com/publications/samestats
    """
    df = pd.read_csv(pkg_resources.resource_stream(__name__, 'data/DatasaurusDozen.tsv'), sep='\t')

    fig, axes = plt.subplots(4, 4, figsize=(12, 12))
    axes = axes.flatten()
    
    for spine in axes[0].spines:
        axes[0].spines[spine].set_visible(False)
    axes[0].xaxis.set_visible(False)
    axes[0].yaxis.set_visible(False)

    # trazar el Datasaurus
    data = df.query('dataset == "dino"')
    ax = data.plot(kind='scatter', x='x', y='y', title='dino', ax=axes[1])
    
    # calcular las estadísticas de síntesis
    x, y = data.x, data.y
    axes[2].text(
        s=f"""ρ  = {np.corrcoef(x,y)[0][1]:.2f}\n{
            r'$μ_x$'
        } = {np.mean(x):.2f}\n{
            r'$σ_x$'
        } = {np.std(x):.2f}\n{
            r'$μ_y$'
        } = {np.mean(y):.2f}\n{r'$σ_y$'} = {np.std(y):.2f}""", x=0.5, y=0.5, fontsize=20, fontfamily='DejaVu Sans Mono'
    )
    for spine in axes[2].spines:
        axes[2].spines[spine].set_visible(False)
    axes[2].xaxis.set_visible(False)
    axes[2].yaxis.set_visible(False)
    axes[2].set_xlim(0.49, 0.58)
    axes[2].set_ylim(0.49, 0.6)

    for spine in axes[3].spines:
        axes[3].spines[spine].set_visible(False)
    axes[3].xaxis.set_visible(False)
    axes[3].yaxis.set_visible(False)

    for (title, data), ax in zip(df.query('dataset != "dino"').groupby('dataset'), axes[4:]):
        data.plot(kind='scatter', x='x', y='y', title=title, ax=ax)
    plt.tight_layout()

    return axes

def cdf_example():
    """Subparcelas para entender la FCD"""
    data = _non_symmetric_data()
    ecdf = ECDF(data)

    fig, axes = plt.subplots(1, 3, figsize=(15, 3))

    for ax in axes:
        ax.plot(ecdf.x, ecdf.y)
        ax.set_xlabel('x')
        ax.set_ylabel('F(x)')

    # inferior o igual al 50
    axes[0].fill_between(ecdf.x[ecdf.x <= 50], ecdf.y[ecdf.x <= 50], 0, alpha=0.5)
    axes[0].axhline(0.93, xmax=0.76, linestyle='dashed')
    axes[0].set_title(r'$P(X \leq 50) \approx 93\%$')

    # igual a 50
    axes[1].fill_between(ecdf.x[ecdf.x == 50], ecdf.y[ecdf.x == 50], 0, alpha=0.5)
    axes[1].set_title(r'$P(X = 50) = 0\%$')

    # superior al 50
    axes[2].fill_between(ecdf.x[ecdf.x >= 50], ecdf.y[ecdf.x >= 50], 0, alpha=0.5)
    axes[2].axhline(0.93, xmax=0.76, linestyle='dashed')
    axes[2].set_title(r'$P(X > 50) = 1 - P(X \leq 50) \approx 7\%$')
    
    plt.suptitle('entendiendo el CDF', y=1.1)
    
    return axes

def common_dists():
    """Mostrar algunas distribuciones de uso común."""
    # preparar los subplots
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()

    # gaussiana
    mu, sigma = 0, 1
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    axes[0].plot(x, norm.pdf(x, mu, sigma))
    axes[0].set_title('Gaussian PDF')
    axes[0].set_ylabel('density')
    axes[0].set_xlabel('x')
    axes[0].annotate(r'$\mu$', xy=(mu, 0.4), xytext=(mu - 0.09, 0.3), arrowprops=dict(arrowstyle='->'))
    axes[0].annotate(
        '', xy=(mu - sigma, 0.25), xytext=(mu + sigma, 0.25),
        arrowprops=dict(arrowstyle='|-|, widthB=0.5, widthA=0.5')
    )
    axes[0].annotate(r'$2\sigma$', xy=(mu - 0.15, 0.22))

    # distribución uniforme definida por min (a) y max (b)
    a, b = 0, 1
    peak = 1 / (b - a)
    axes[1].plot([a, a, b, b], [0, peak, peak, 0])
    axes[1].set_title('Uniform PDF')
    axes[1].set_ylabel('density')
    axes[1].set_xlabel('x')
    axes[1].annotate('min', xy=(a, peak), xytext=(a + 0.2, peak - 0.2), arrowprops=dict(arrowstyle='->'))
    axes[1].annotate('max', xy=(b, peak), xytext=(b - 0.3, peak - 0.2), arrowprops=dict(arrowstyle='->'))
    axes[1].set_ylim(0, 1.5)

    # exponencial
    x = np.linspace(0, 5, 100)
    axes[2].plot(x, expon.pdf(x, scale=1/3))
    axes[2].set_title('Exponential PDF')
    axes[2].set_ylabel('density')
    axes[2].set_xlabel('x')
    axes[2].annotate(r'$\lambda$ = 3', xy=(0, 3), xytext=(0.5, 2.8), arrowprops=dict(arrowstyle='->'))
    
    # Bernoulli de lanzamiento de moneda
    axes[3].bar(['heads', 'tails'], bernoulli.pmf([0, 1], p=0.5))
    axes[3].set_title('Bernoulli with fair coin toss (p = 0.5)')
    axes[3].set_ylabel('probability')
    axes[3].set_xlabel('coin toss result')
    axes[3].set_ylim(0, 1)
    
    # Binomial de lanzar una moneda muchas veces
    x = np.arange(0, 10)
    axes[4].plot(x, binom.pmf(x, n=x.shape, p=0.5), linestyle='--', marker='o')
    axes[4].set_title('Binomial PMF - many Bernoulli trials')
    axes[4].set_ylabel('probability')
    axes[4].set_xlabel('number of heads')

    # Poisson PMF (función de masa de probabilidad) porque se trata de una variable aleatoria discreta
    x = np.arange(0, 10)
    axes[5].plot(x, poisson.pmf(x, mu=3), linestyle='--', marker='o')
    axes[5].set_title('Poisson PMF')
    axes[5].set_ylabel('mass')
    axes[5].set_xlabel('x')
    axes[5].annotate(r'$\lambda$ = 3', xy=(3, 0.225), xytext=(1.9, 0.2), arrowprops=dict(arrowstyle='->'))

    # añadir un titulo
    plt.suptitle('Algunas distribuciones de uso común', fontsize=15, y=0.95)
    
    return axes

def correlation_coefficient_examples():
    """Muestra algunos ejemplos de gráficos de dispersión con coeficientes de correlación."""
    # datos de partida
    np.random.seed(0)
    x = np.random.normal(size=100)
    y = np.random.normal(size=100)

    # crear subplots
    fig, axes = plt.subplots(1, 4, figsize=(16, 3))
    
    # ninguna correlación
    axes[0].scatter(x, y)
    axes[0].set_title(f'ρ = {np.round(np.corrcoef(x, y)[0][1], 2)}')
    
    # correlación negativa débil
    a, b = x, (x + y*2)*-1
    axes[1].scatter(a, b)
    axes[1].set_title(f'ρ = {np.round(np.corrcoef(a, b)[0][1], 2)}')
    
    # fuerte correlación positiva
    s, t = x, (x - np.random.uniform(1, 3, size=100))
    axes[2].scatter(s, t)
    axes[2].set_title(f'ρ = {np.round(np.corrcoef(s, t)[0][1], 2)}')
    
    # correlación negativa perfecta
    c, d = x, (x - y*.1) * -1
    axes[3].scatter(c, d)
    axes[3].set_title(f'ρ = {np.round(np.corrcoef(c, d)[0][1], 2)}')
    
    for ax in axes:
        ax.set_xlabel('x')
        ax.set_ylabel('y')
    
    return axes

def different_modal_plots():
    """Mostrar distribuciones de ejemplo unimodales, bimodales y multimodales."""

    # detalles de distribución
    x = np.linspace(-4, 4, 500)
    loc1, scale1, size1 = (-2, 0.75, 150)
    loc2, scale2, size2 = (3, 0.5, 50)
    loc3, scale3, size3 = (0.4, 1, 150)

    # crear subplots
    fig, axes = plt.subplots(1, 3, figsize=(15, 3))

    # gráfico unimodal
    axes[0].plot(x, norm.pdf(x))

    # gráfico bimodal
    bimodal_pdf = norm.pdf(x, loc=loc1, scale=scale1) * float(size1) / (size1 + size2) + \
       norm.pdf(x, loc=loc2, scale=scale2) * float(size2) / (size1 + size2)
    axes[1].plot(x, bimodal_pdf)

    # gráfico multimodal
    multimodal_pdf = bimodal_pdf + norm.pdf(x, loc=loc3, scale=scale3) * float(size3) / (size1 + size2)
    axes[2].plot(x, multimodal_pdf)

    # etiquetar todo y formatear
    for ax, title in zip(axes, ['unimodal', 'bimodal', 'multimodal']):
        ax.set_ylim(0, 0.45)
        ax.set_xlabel('x')
        ax.set_ylabel('density')
        ax.set_title(title)
        _despine(ax)

    return axes

def effect_of_std_dev():
    """Mostrar dos distribuciones normales con diferentes desviaciones estándar."""
    np.random.seed(0)
    data = pd.DataFrame({
        'σ = 0.5': np.random.normal(scale=0.5, size=1000),
        'σ = 2': np.random.normal(scale=2, size=1000)
    })

    ax = data.plot(kind='density', title='Diferentes desviaciones típicas de la población', figsize=(5, 2), colormap='brg')
    plt.xlabel('x')
    _despine(ax)

    return ax

def example_boxplot():
    """Generar un gráfico de caja de ejemplo."""
    non_symmetric = _non_symmetric_data()

    # hallar los cuartiles y el iqr
    q1_y, median_y, q3_y = non_symmetric.quantile([0.25, 0.5, 0.75])
    iqr = q3_y - q1_y

    # crear una boxplot
    ax = non_symmetric.plot(kind='box', figsize=(6, 6), title='Box plot')

    # etiquetar la caja
    ax.annotate('median', xy=(0.945, median_y + 2))
    ax.annotate(r'$Q_3$', xy=(1, q3_y), xytext=(1.08, q3_y - 5))
    ax.annotate(r'$Q_1$', xy=(1, q1_y), xytext=(1.08, q1_y))
    ax.annotate(
        'IQR', xy=(0.9, (q3_y + q1_y)/2), xytext=(0.8, (q3_y + q1_y)/2 - 2.85),
        arrowprops=dict(arrowstyle='-[, widthB=3.3, lengthB=0.5')
    )

    # etiquetar los bigotes
    ax.annotate(r'$Q_3 + 1.5 * IQR$', xy=(1.05, q3_y + 1.5 * iqr - 7))
    ax.annotate(r'$Q_1 - 1.5 * IQR$', xy=(1.05, q1_y - 1.5 * iqr - 2))

    # etiquetar los valores atípicos
    ax.annotate(
        'outlier', xy=(0.99, non_symmetric.min()), xytext=(0.8, non_symmetric.min() - 2.1),
        arrowprops=dict(arrowstyle='->')
    )

    for i, val in enumerate(non_symmetric[non_symmetric > q3_y + 1.5*iqr]):
        if not i: 
            text = 'outliers' 
            x, y = 0.75, 102
        else:
            text = '' 
            x, y = 0.87, 103
        ax.annotate(
            text, xy=(0.99, val), xytext=(x, y),
            arrowprops=dict(facecolor='black', arrowstyle='-|>')
        )

    _despine(ax)
    ax.set_ylabel('x')
    ax.xaxis.set_visible(False)

    return ax

def example_histogram():
    """Generar un histograma de ejemplo."""
    non_symmetric = _non_symmetric_data()

    # obtener bins
    bins = np.histogram_bin_edges(non_symmetric)

    # trazar los datos
    ax = non_symmetric.plot(
        kind='hist', legend=False, figsize=(15, 3),
        title=f'Histograma con 10 intervalos (each of width {bins[1] - bins[0]:.2f})'
    )
    ax.set_xlabel('x')

    # anotar las medidas de tendencia central
    x_mode, x_mean, x_median = non_symmetric.mode(), non_symmetric.mean(), non_symmetric.median()
    ax.annotate(
        f'mode ({x_mode.iat[0]:.0f})', xy=(x_mode, 210), xytext=(x_mode + 5, 250), arrowprops=dict(arrowstyle='->')
    )
    ax.annotate(
        f'mean ({x_mean:.0f})', xy=(x_mean, 180), xytext=(x_mean - 20, 220), arrowprops=dict(arrowstyle='->')
    )
    ax.annotate(
        f'median ({x_median:.0f})', xy=(x_median, 180), xytext=(x_median - 12, 280), arrowprops=dict(arrowstyle='->')
    )
    plt.ylim((0, 320))
    _despine(ax)

    return ax

def example_kde():
    """Generar un KDE de ejemplo."""
    non_symmetric = _non_symmetric_data()

    # plot the data
    ax = non_symmetric.plot(
        kind='kde', legend=False, figsize=(15, 3), 
        title='Estimación de la densidad del núcleo', bw_method=0.1, ylim=(0, 0.02)
    )
    ax.set_xlabel('x')

    # encontrar medidas de tendencia central
    x_mode, x_mean, x_median = non_symmetric.mode(), non_symmetric.mean(), non_symmetric.median()

    # marque las medidas de tendencia central con líneas discontinuas verticales
    ax.axvline(x_mean, ymax=0.195, color='orange', linestyle='dashed')
    ax.axvline(x_median, ymax=0.5, color='orange', linestyle='dashed')
    ax.axvline(x_mode.iat[0], ymax=0.868, color='orange', linestyle='dashed')

    # anotar las medidas de tendencia central
    ax.annotate('mode', xy=(x_mode - 11, 0.0178))
    ax.annotate('mean', xy=(x_mean, 0.0015), xytext=(x_mean - 70, 0.001), arrowprops=dict(arrowstyle='->'))
    ax.annotate('median', xy=(x_median, 0.01), xytext=(x_median - 50, 0.013), arrowprops=dict(arrowstyle='->'))

    _despine(ax)

    return ax

def example_regression():
    """Mostrar ejemplo de regresión."""
    # generar datos
    np.random.seed(0)
    ice_cream_sales = pd.DataFrame({
        'temps': np.linspace(20, 40, num=30),
        'sales': np.abs(np.append(np.arange(2, 22), np.arange(22, 32)) + np.random.randint(-10, 10, size=30))
    })
    
    # hacer el diagrama de dispersión
    ax = ice_cream_sales.plot(
        kind='scatter', x='temps', y='sales', xlim=(15, 45), ylim=(0, 40), figsize=(12, 5),
        title='Uso de la regresión para predecir las ventas de helados'
    )

    # trazar línea de regresión
    m, b = np.polyfit(ice_cream_sales.temps, ice_cream_sales.sales, 1)
    reg_x = ice_cream_sales.temps
    reg_y = [m*num + b for num in reg_x]
    ax.plot(reg_x, reg_y, 'r-', label='línea de regresión')
    
    # observe la ecuación de la recta de regresión
    ax.annotate(f'y = {m:.2f}x + {b:.2f}', xy=(15.5, 32))

    # ampliar la línea para mostrar la extrapolación
    ax.plot([-b/m, 20], [0, 20*m + b], 'r:', label='línea de regresión extrapolada')
    ax.plot([40, 45], [m*x + b for x in [40, 45]], 'r:')

    # etiquetado
    plt.legend()
    plt.xlabel('temperatura en °C')
    plt.ylabel('venta de helados')
    
    return ax

def example_scatter_plot():
    """Mostrar ejemplo de gráfico de dispersión."""
    # generar datos
    np.random.seed(0)
    ice_cream_sales = pd.DataFrame({
        'temps': np.linspace(20, 40, num=30),
        'sales': np.abs(np.append(np.arange(2, 22), np.arange(22, 32)) + np.random.randint(-10, 10, size=30))
    })
    
    # hacer el diagrama de dispersión
    ax = ice_cream_sales.plot(
        kind='scatter', x='temps', y='sales', xlim=(15, 45), ylim=(0, 40), figsize=(12, 5),
        title='venta de helados a una temperatura determinada'
    )

    # etiquetado
    plt.xlabel('temperatura en °C')
    plt.ylabel('venta de helados')
    
    return ax

def hist_and_kde():
    """Mostrar histograma con KDE."""
    # obtener datos
    data = _non_symmetric_data()

    # trazar histograma y KDE
    ax = data.plot(kind='hist', density=True, bins=12, alpha=0.5, title='Estimación de la distribución', figsize=(15, 3))
    data.plot(kind='kde', ax=ax, color='blue').set_xlabel('x')
    _despine(ax)

    return ax

def non_linear_relationships():
    """Representar gráficamente datos logarítmicos y exponenciales junto con los coeficientes de correlación."""
    # crear subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 3))

    # trazado logarítmico
    log_x = np.linspace(0.01, 10)
    log_y = np.log(log_x)
    axes[0].scatter(log_x, log_y)
    axes[0].set_title(f'ρ = {np.round(np.corrcoef(log_x, log_y)[0][1], 2):.2f}')

    # trazado exponencial
    exp_x = np.linspace(0, 10)
    exp_y = np.exp(exp_x)
    axes[1].scatter(exp_x, exp_y)
    axes[1].set_title(f'ρ = {np.round(np.corrcoef(exp_x, exp_y)[0][1], 2):.2f}')

    # etiquetado
    for ax in axes:
        ax.set_xlabel('x')
        ax.set_ylabel('y')

    return axes

def skew_examples():
    """Visualiza distribuciones a la izquierda, a la derecha y sin sesgo."""

    # crear subplots
    fig, ax = plt.subplots(1, 3, figsize=(20, 4))

    # determina skew
    a = 4

    # buscar estadísticas para la anotación
    mean_skew_val = skewnorm.mean(a)
    median_skew_val = skewnorm.median(a)

    # obtener datos x donde PDF tiene valor
    x = np.linspace(skewnorm.ppf(0.001, a), skewnorm.ppf(0.999, a), 100)

    # plot left skew
    ax[0].plot(x * -1, skewnorm.pdf(x, a))
    ax[0].set_title('izquierda/Negativa Skewed')

    # anotar el modo de inclinación a la izquierda
    ax[0].axvline(-0.42, 0.72, 0.925, color='orange')
    ax[0].text(s='mode', x=-0.49, y=0.44, rotation=90)
    ax[0].axvline(-0.42, 0, 0.53, color='orange')

    # anotar la mediana del sesgo izquierdo
    ax[0].axvline(median_skew_val * -1, 0.52, 0.83, color='orange')
    ax[0].text(s='median', x=-0.74, y=0.26, rotation=90)
    ax[0].axvline(median_skew_val * -1, 0, 0.3, color='orange')

    # anotar la media de la desviación a la izquierda
    ax[0].axvline(mean_skew_val * -1, 0.26, 0.77, color='orange')
    ax[0].text(s='mean', x=-0.84, y=0.1, rotation=90)
    ax[0].axvline(mean_skew_val * -1, 0, 0.09, color='orange')

    # plot no skew normal
    ax[1].plot(x, norm.pdf(x, loc=x.mean(), scale=0.56))
    ax[1].set_title('No Skew')

    # anotar la media, la mediana y la moda
    ax[1].text(s='  mean\nmedian\n  mode', x=x.mean() - 0.25, y=0.25)
    ax[1].axvline(x.mean(), 0.5, 0.94, color='orange')
    ax[1].axvline(x.mean(), 0, 0.3, color='orange')

    # plot right skew
    ax[2].plot(x, skewnorm.pdf(x, a))
    ax[2].set_title('Right/Positive Skewed')

    # anotar el modo de inclinación a la derecha
    ax[2].axvline(0.42, 0.72, 0.925, color='orange')
    ax[2].text(s='mode', x=0.35, y=0.44, rotation=90)
    ax[2].axvline(0.42, 0, 0.53, color='orange')

    # anotar la mediana de la desviación a la derecha
    ax[2].axvline(median_skew_val, 0.52, 0.83, color='orange')
    ax[2].text(s='median', x=0.6, y=0.26, rotation=90)
    ax[2].axvline(median_skew_val, 0, 0.3, color='orange')

    # anotar la media de la desviación a la derecha
    ax[2].axvline(mean_skew_val, 0.26, 0.77, color='orange')
    ax[2].text(s='mean', x=0.72, y=0.1, rotation=90)
    ax[2].axvline(mean_skew_val, 0, 0.09, color='orange')

    # etiquetar los ejes y fijar los límites del eje y
    for axes in ax:
        axes.set_xlabel('x')
        axes.set_ylabel('f(x)')
        axes.set_ylim(0, 0.75)
        _despine(axes)

    return ax
    
def time_series_decomposition_example():
    """Mostrar un ejemplo de descomposición de series temporales."""
    # generar una serie temporal aleatoria
    np.random.seed(0)
    ts = pd.DataFrame({'timestamp' : pd.date_range('2018-01-01', periods=365, freq='D')})
    for i, drift, seasonality, noise in zip(
        ts.index, 
        np.linspace(0, 1, num=365), 
        itertools.cycle(np.append(np.linspace(0, np.pi, num=25), np.linspace(np.pi, 0, num=25, endpoint=False))),
        np.random.uniform(-10, 10, size=365)
    ):
        if i in [0]:
            ts.loc[i, 'value'] = i
        else:
            ts.loc[i, 'value'] = ts.loc[i - 1, 'value'] + drift + np.sin(seasonality) + noise

    # trazar el resultado
    plt.rcParams['figure.figsize'] = [10, 6]
    result = seasonal_decompose(ts.set_index('timestamp').value.rename('Descomposición de series temporales'), period=50)
    plot = result.plot()
    plt.rcdefaults()
    return plot.axes