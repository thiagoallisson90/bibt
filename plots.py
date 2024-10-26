from typing import Union
import os

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

def gen_sm_coords(n_sms=1000, axis=7000, seed=42):
	np.random.seed(seed)
	sm_coords = np.random.uniform(0, axis, (n_sms, 2))
	np.random.seed(None)

	return sm_coords

"""
Example

plot_bars_with_err(x=[200, 400, 600, 800, 1000], 
                   y=[[10, 20, 30, 40, 50], [12, 18, 26, 34, 42], 
                      [1, 4, 5, 6, 7], [1, 6, 12, 16, 20]], 
                   xlabel='Number of EDs', ylabel='UL-PDR', 
                   figname=f'/home/thiago/Documentos/nack_psr.png', 
                   unit='%', labels=['KM', 'KMD', 'Place', 'cPlace'])
"""
def plot_bars_with_err(x: Union[list, np.array], y: Union[list, np.array], 
                       xlabel: str, ylabel: str, labels: Union[list, np.array],
                       figname='metric.png', unit='', fig_size=(12, 8)):
    yerr = []
    for value in y:
        yerr.append(np.std(value))

    _, ax = plt.subplots(figsize=fig_size)
    
    markers = ['^--', 'o--', 's--', 'd--']
    colors = ['#0072B2', '#E69F00', '#CC79A7', '#009E73']
    for i, value in enumerate(y):
        ax.errorbar(x, value, yerr=yerr[i], fmt=markers[i], capsize=5, capthick=2, 
                    elinewidth=1.5, label=labels[i], color=colors[i])

    ax.grid(axis='y', linestyle='--', color='gray', alpha=1.0)
    ax.set_xticks(x)

    ax.set_xlabel(xlabel, fontsize=25)
    ax.set_ylabel(f'{ylabel} {"(" + unit + ")" if unit else ""}', fontsize=25)
    ax.legend(fontsize=25)
    
    ax.tick_params(axis='x', labelsize=25)
    ax.tick_params(axis='y', labelsize=25)

    plt.tight_layout()

    plt.savefig(figname)
    plt.close('all')

import numpy as np
import matplotlib.pyplot as plt
from typing import Union

def plot_curves_with_err(x: Union[list, np.array], y: Union[list, np.array], 
                         xlabel: str, ylabel: str, labels: Union[list, np.array],
                         figname='metric.png', unit='', fig_size=(12, 8)):
    yerr = []
    for value in y:
        yerr.append(np.std(value))  # Calcula o desvio padrão como erro para cada conjunto de dados

    _, ax = plt.subplots(figsize=fig_size)

    # Definindo marcadores e cores para as curvas
    markers = ['^', 'o', 's', 'd']  # Apenas os marcadores
    line_styles = ['--', '-.', ':', '-']  # Estilos de linha para diferenciação
    colors = ['#0072B2', '#E69F00', '#CC79A7', '#009E73']  # Cores otimizadas para daltonismo
    
    for i, value in enumerate(y):
        ax.errorbar(x, value, yerr=yerr[i], fmt=markers[i], linestyle=line_styles[i], 
                    capsize=5, capthick=2, elinewidth=1.5, label=labels[i], color=colors[i])

    ax.grid(axis='y', linestyle='--', color='gray', alpha=1.0)  # Grid no eixo y
    ax.set_xticks(x)  # Definindo os ticks do eixo X com base nos valores de `x`

    ax.set_xlabel(xlabel, fontsize=25)
    ax.set_ylabel(f'{ylabel} {"(" + unit + ")" if unit else ""}', fontsize=25)
    ax.legend(fontsize=25)

    ax.tick_params(axis='x', labelsize=25)
    ax.tick_params(axis='y', labelsize=25)

    plt.tight_layout()

    # Salvando o gráfico no arquivo especificado
    plt.savefig(figname)
    plt.close('all')

import numpy as np
import matplotlib.pyplot as plt
from typing import Union

def plot_curves(x: Union[list, np.array], y: Union[list, np.array], 
                xlabel: str, ylabel: str, labels: Union[list, np.array],
                figname='metric.png', unit='', fig_size=(12, 8)):
    _, ax = plt.subplots(figsize=fig_size)

    # Definindo marcadores, estilos de linha e cores
    markers = ['^', 'o', 's', 'd']  # Apenas os marcadores
    line_styles = ['--', '-.', ':', '-']  # Estilos de linha para diferenciação
    colors = ['#0072B2', '#E69F00', '#CC79A7', '#009E73']  # Cores amigáveis para daltonismo
    
    for i, value in enumerate(y):
        ax.plot(x, value, marker=markers[i], linestyle=line_styles[i], 
                label=labels[i], color=colors[i], linewidth=4, markersize=12)

    ax.grid(axis='y', linestyle='--', color='gray', alpha=1.0)  # Grid no eixo y
    ax.set_xticks(x)  # Definindo os ticks do eixo X com base nos valores de `x`

    ax.set_xlabel(xlabel, fontsize=25)
    ax.set_ylabel(f'{ylabel} {"(" + unit + ")" if unit else ""}', fontsize=25)
    ax.legend(fontsize=25)

    ax.tick_params(axis='x', labelsize=25)
    ax.tick_params(axis='y', labelsize=25)

    plt.tight_layout()

    # Salvando o gráfico no arquivo especificado
    plt.savefig(figname)
    plt.close('all')

def save_sfs(data: list[list[float]], n: int, filename: str, mode='a'):
    with open(filename, mode) as file:
        for sublist in data:
            file.write(','.join(map(str, sublist)) + str(n) + '\n')

def plot_bars(x: Union[list, np.array], y: Union[list, np.array], 
              xlabel: str, ylabel: str, labels: Union[list, np.array],
              figname='metric.png', unit='', fig_size=(12, 8)):
    _, ax = plt.subplots(figsize=fig_size)

    # Definindo as larguras das barras
    bar_width = 0.15
    x_indices = np.arange(len(x))  # Índices das barras

    # Definindo cores e estilos
    colors = ['#0072B2', '#E69F00', '#CC79A7', '#009E73']  # Cores amigáveis para daltonismo
    
    # Plotando as barras
    for i, value in enumerate(y):
        ax.bar(x_indices + i * bar_width, value, width=bar_width, 
               label=labels[i], color=colors[i], edgecolor='black')

    ax.set_xticks(x_indices + bar_width * (len(y) - 1) / 2)  # Centralizando os ticks do eixo X
    ax.set_xticklabels(x)  # Definindo os labels do eixo X

    ax.set_xlabel(xlabel, fontsize=25)
    ax.set_ylabel(f'{ylabel} {"(" + unit + ")" if unit else ""}', fontsize=25)
    ax.legend(fontsize=25)

    ax.tick_params(axis='x', labelsize=25)
    ax.tick_params(axis='y', labelsize=25)

    plt.tight_layout()

    # Salvando o gráfico no arquivo especificado
    plt.savefig(figname)
    plt.close('all')
    

import numpy as np
import matplotlib.pyplot as plt

def plot_stacked_bars(x: list, y: list, labels: list, xlabel: str, 
                      ylabel: str, figname='bars.png', fig_size=(12, 8)):
    # Cores para cada conjunto de valores
    colors = ['#0072B2', '#E69F00', '#CC79A7', '#009E73', '#D55E00']

    # Padrões de hachura para cada conjunto de valores
    hatches = ['/', '\\', '|', '-', '+']
    
    # Definindo a largura das barras e as posições no eixo X
    bar_width = 0.5
    positions = np.arange(len(x))  # Posições das barras no eixo X

    # Criando a figura
    _, ax = plt.subplots(figsize=fig_size)

    # Inicializando a base para as barras empilhadas
    bottom_values = np.zeros(len(x))

    # Iterando sobre as listas de PLR para empilhar as barras com hachuras
    for _, (plr, label, color, hatch) in enumerate(zip(y, labels, colors, hatches)):
        ax.bar(positions, plr, bar_width, bottom=bottom_values, label=label, color=color, hatch=hatch)
        bottom_values += np.array(plr)  # Atualizando a base para a próxima barra

    # Configurando o grid no eixo Y
    ax.grid(axis='y', linestyle='--', color='gray', alpha=1)

    # Definindo rótulos e título com fonte de tamanho 25
    ax.set_xlabel(xlabel, fontsize=25)
    ax.set_ylabel(ylabel, fontsize=25)
    
    ax.legend(fontsize=20, ncol=len(labels), loc='upper center', 
              bbox_to_anchor=(0.5, 1.15), frameon=False)
    
    # Definindo ticks e labels do eixo X para os valores de `x`
    ax.set_xticks(positions)
    ax.set_xticklabels(x, fontsize=25)  # Usando os valores de `x` como labels

    # Configurando o eixo Y para ir de 0 a 100, de 10 em 10
    ax.set_yticks(np.arange(0, 101, 10))  # Definindo os ticks do eixo Y
    ax.set_ylim(0, 100)  # Definindo os limites do eixo Y

    # Ajustando o tamanho da fonte dos ticks nos eixos X e Y
    ax.tick_params(axis='x', labelsize=25)
    ax.tick_params(axis='y', labelsize=25)

    # Ajustando o layout
    plt.tight_layout()

    # Salvando o gráfico no arquivo especificado
    plt.savefig(figname)
    plt.close('all')

def gen_gws_plot(points: np.ndarray, output_file='gws.eps', format='eps',
                 area_size_m=7000, num_clusters=4, point_size=80, dpi=3000):
    # Configurações da imagem
    figsize_inches = (13, 8)  # Tamanho da figura definido para 13x8 polegadas

    # Aplicar K-Means para criar clusters
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    labels = kmeans.fit_predict(points)

    # Paleta de cores acessível para daltônicos
    color_palette = [
        '#0072B2',  # Azul
        '#E69F00',  # Laranja
        '#CC79A7',  # Rosa
        '#009E73'   # Verde
    ]

    # Criar o gráfico
    plt.figure(figsize=figsize_inches, dpi=dpi)
    
    # Desenhar os clusters
    for i in range(num_clusters):
        cluster_points = points[labels == i]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], 
                    s=point_size, color=color_palette[i % len(color_palette)], 
                    edgecolor='black', linewidth=1.5, marker='o')  # Aumentando a largura do contorno

    # Configurações do gráfico com rótulos atualizados
    plt.xlabel("X-position (m)", fontsize=25, fontname='DejaVu Sans')
    plt.ylabel("Y-position (m)", fontsize=25, fontname='DejaVu Sans')
    plt.xlim(0, area_size_m)
    plt.ylim(0, area_size_m)
    plt.xticks(fontsize=25, fontname='DejaVu Sans')
    plt.yticks(fontsize=25, fontname='DejaVu Sans')
    
    # Adicionar grid tracejado e mais fino
    plt.grid(True, linestyle='--', linewidth=0.5)

    # Salvar como EPS
    plt.savefig(output_file, format=format, bbox_inches='tight', dpi=dpi)

    plt.close('all')