# Rest2d-for-python

Uma engine 2D simples e leve para Python, inspirada na filosofia da LÖVE2D.

A REST Engine foi criada para tornar o desenvolvimento de jogos 2D em Python mais simples, permitindo criar jogos usando apenas arquivos Python comuns, sem a necessidade de aprender uma linguagem própria ou uma API complexa.

## Características

* Interface simples inspirada em engines como LÖVE2D.
* Desenvolvimento usando Python puro.
* Loop de jogo com `load()`, `update(dt)` e `draw()`.
* Sistema de gráficos 2D.
* Renderização de formas geométricas.
* Suporte a imagens e sprites.
* Entrada de teclado e mouse.
* Controle de FPS e tempo.
* Carregamento automático de arquivos da pasta `assets`.
* Cache automático de recursos.
* Estrutura pequena e fácil de modificar.

## Exemplo

```python

x = 100
y = 100


def update(dt):

    global x

    if rest.keyboard.isDown("d"):
        x += 200 * dt

    if rest.keyboard.isDown("a"):
        x -= 200 * dt


def draw():

    rest.graphics.clear(30,30,40)

    rest.graphics.color(255,0,0)

    rest.graphics.rectangle(
        "fill",
        x,
        y,
        50,
        50
    )
```
## Filosofia

A REST Engine não tenta substituir engines grandes.

O objetivo é oferecer uma ferramenta pequena, rápida e fácil de entender, onde o programador controla o jogo diretamente usando Python.

A engine evita criar sistemas desnecessários que já existem na linguagem. Recursos como arquivos, matemática, estruturas de dados e lógica continuam sendo feitos usando o próprio Python, e sim foi feito com ia mais foi para um bem maior.
