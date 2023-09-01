class Parte():
    def __init__(self, nome=str, nivel_ataque=0, nivel_defesa=0, energia_consumida=0):
        self.nome = nome
        self.nivel_ataque = nivel_ataque
        self.nivel_defesa = nivel_defesa
        self.energia_consumida = energia_consumida

    def obter_status_dict(self):
        nome_formatado = self.nome.replace(' ', '').lower()
        return {
            f'nome_{nome_formatado}': self.nome.upper(),
            f'status_{nome_formatado}': self.esta_disponivel(),
            f'ataque_{nome_formatado}': self.nivel_ataque,
            f'defesa_{nome_formatado}': self.nivel_defesa,
            f'energia_{nome_formatado}': self.energia_consumida
        }

    def reducao_defesa(self, nivel_ataque):
        self.nivel_defesa = self.nivel_defesa - nivel_ataque
        if self.nivel_defesa <= 0:
            self.nivel_defesa = 0

    def esta_disponivel(self):
        return self.nivel_defesa <= 0

class Robo:
    def __init__(self, nome, codigo_cor):
        self.nome = nome
        self.codigo_cor = codigo_cor
        self.energia = 100
        self.partes = [
            Parte('Cabeça', nivel_ataque=5, nivel_defesa=10, energia_consumida=5),
            Parte('Arma', nivel_ataque=15, nivel_defesa=0, energia_consumida=10),
            Parte('Arma esquerda', nivel_ataque=3, nivel_defesa=20, energia_consumida=10),
            Parte('Arma direita', nivel_ataque=6, nivel_defesa=20, energia_consumida=10),
            Parte('Perna esquerda', nivel_ataque=4, nivel_defesa=20, energia_consumida=15),
            Parte('Perna direita', nivel_ataque=8, nivel_defesa=20, energia_consumida=15)
        ]

    def mostrar_status(self):
        print(self.codigo_cor)
        str_robo = robo_art.format(**self.obter_status_parte())
        self.saudar()
        self.mostrar_energia()
        print(str_robo)
        print(cores['Branco'])

    def saudar(self):
        print('Oi, meu nome é', self.nome)

    def mostrar_energia(self):
        print('Temos', self.energia, '% de energia disponível!')

    def atacar(self, robo_inimigo, parte_para_usar, parte_para_atacar):
        robo_inimigo.partes[parte_para_atacar].reducao_defesa(self.partes[parte_para_usar].nivel_ataque)
        self.energia -= self.partes[parte_para_usar].energia_consumida

    def obter_status_parte(self):
        status_parte = {}
        for parte in self.partes:
            status_dict = parte.obter_status_dict()
            status_parte.update(status_dict)
        return status_parte

    def ha_uma_peca_disponivel(self):
        for parte in self.partes:
            if parte.esta_disponivel():
                return True
        return False

    def esta_ligado(self):
        return self.energia >= 0

robo_art = r"""
    (o conteúdo da variável 'robo_art' permanece o mesmo)
"""

cores = {
    "Preto": '\x1b[90m',
    "Azul": '\x1b[94m',
    "Ciano": '\x1b[96m',
    "Verde": '\x1b[92m',
    "Magenta": '\x1b[95m',
    "Vermelho": '\x1b[91m',
    "Branco": '\x1b[97m',
    "Amarelo": '\x1b[93m'
}

def jogar():
    jogando = True
    print('Bem vindo ao Jogo!')
    print('Dados do jogador 1:')
    robo_um = construir_robo()
    print('Dados do jogador 2:')
    robo_dois = construir_robo()

    robo_atual = robo_um
    robo_inimigo = robo_dois
    rodada = 0

    while jogando:
        if rodada % 2 == 0:
            robo_atual = robo_um
            robo_inimigo = robo_dois
        else:
            robo_atual = robo_dois
            robo_inimigo = robo_um
        robo_atual.mostrar_status()
        print('Qual parte devo usar para atacar?')
        parte_para_usar = int(input('Escolha uma parte para atacar o inimigo:'))

        robo_inimigo.mostrar_status()
        print('Qual parte do inimigo devo atacar?')
        parte_para_atacar = int(input('Escolha uma peça do inimigo para atacar:'))

        robo_atual.atacar(robo_inimigo, parte_para_usar, parte_para_atacar)
        rodada += 1
        if not robo_inimigo.esta_ligado() or not robo_inimigo.ha_uma_peca_disponivel():
            jogando = False
            print('Parabéns, você ganhou!')

def construir_robo():
    robo_nome = input('Nome do robô: ')
    codigo_cor = escolha_cor()
    robo = Robo(robo_nome, codigo_cor)
    robo.mostrar_status()
    return robo

def escolha_cor():
    print('Cores disponíveis: ')
    for cor in cores:
        print(cor)
    escolha_cor = input('Escolha uma cor: ')
    codigo_cor = cores.get(escolha_cor.capitalize(), cores['Branco'])
    return codigo_cor

jogar()
