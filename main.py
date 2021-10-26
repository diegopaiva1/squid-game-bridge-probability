from scipy.stats import binom
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt

plt.style.use('seaborn')

if __name__ == '__main__':
    n = 18
    p = 0.5

    X = binom(n, p)

    players = ['?', '?', '?', '?', '?', '?', '?', '?', 'Deok-su', '?', 'Mi-nyeo', '?', '?', 'Sang-woo', 'Sae-byeok', 'Gi-hun']

    # Na série, os jogadores são numerados de 1 a 16.
    players_num = range(1, len(players) + 1)

    # Calculando a taxa de sobrevivência pra cada jogador.
    # A função `cdf` do scipy fornece a função de probabilidade acumulada da distribuição.
    survival = [X.cdf(x - 1) * 100.0 for x in players_num]

    fig, ax = plt.subplots(figsize = (19, 10), tight_layout = True)

    fig.suptitle('Round 6: Quais as chances de cada jogador no desafio da ponte de cristal?', fontsize = 24, fontweight = 'bold')

    ax.set_xticks(players_num)
    ax.set_xticklabels([f'{name}\n{i}' for i, name in enumerate(players, 1)])
    ax.set_ylabel('Probabilidade (%)')

    # Anotar as imagens de cada jogador e os valores nas coordenadas (x, y).
    for x, y in zip(players_num, survival):
        img = plt.imread(f'./img/{players[x - 1]}.png')
        im = OffsetImage(img, zoom = 0.5)
        im.image.axes = ax

        ab = AnnotationBbox(
            im, 
            (x, 0),  
            xybox = (0, -60), 
            frameon = False,
            xycoords = 'data',  
            boxcoords = 'offset points', 
            pad = 0
        )

        ax.add_artist(ab)

        ax.annotate(
            '{:.2f}'.format(y),
            (x, y),
            textcoords = 'offset points',
            xytext = (0, 10),
            ha = 'center',
            fontsize = 12
        ) 


    ax.plot(players_num, survival, c = 'orange', marker = 'o')

    ax.tick_params(axis = 'x', which = 'major', pad = 65)
    ax.set_xlabel(
        'Elaborado por Diego Paiva.\nMetodologia utilizada disponível em https://entusiasta.dev/post/round-6-quais-as-chances-de-cada-jogador-no-desafio-da-ponte-de-cristal.',
        color = 'grey',
        labelpad = 20
    )

    fig.savefig('./bridge_prob.png')
