class Parte():
    def __init__(self, nome, nivel_ataque, nivel_defesa, energia_consumida):
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
        print(f'Nivel de defesa parte :{self.nivel_defesa} ')


    def esta_disponivel(self):
        return self.nivel_defesa > 0
    print('Arma está disponível!')

    def __str__(self):
        return f"{self.nome} - Ataque: {self.nivel_ataque}, Defesa: {self.nivel_defesa}, Energia Consumida: {self.energia_consumida}"

class Robo:
    def __init__(self, nome, codigo_cor):
        self.nome = nome
        self.codigo_cor = codigo_cor
        self.energia = 100
        self.partes = [
            Parte('Cabeça', nivel_ataque=5, nivel_defesa=10, energia_consumida=5),
            Parte('Arma', nivel_ataque=15, nivel_defesa=25, energia_consumida=10),
            Parte('Arma esquerda', nivel_ataque=3, nivel_defesa=20, energia_consumida=10),
            Parte('Arma direita', nivel_ataque=6, nivel_defesa=20, energia_consumida=10),
            Parte('Perna esquerda', nivel_ataque=4, nivel_defesa=20, energia_consumida=15),
            Parte('Perna direita', nivel_ataque=8, nivel_defesa=20, energia_consumida=15)
        ]

    def mostrar_status(self):
        print(self.codigo_cor)
        self.saudar()
        self.mostrar_energia()

        print(cores['Branco'])

    def saudar(self):
        print('Oi, meu nome é', self.nome)

    def mostrar_energia(self):
        print('Possuo', self.energia, '% de energia disponível!')

    def atacar(self, robo_inimigo, parte_para_usar, parte_para_atacar):
        parte_usada = self.partes[parte_para_usar]
        parte_alvo = robo_inimigo.partes[parte_para_atacar]
        energia_gasta = parte_usada.energia_consumida
        mensagem = f"{self.nome} usou {parte_usada.nome} para atacar {robo_inimigo.nome}'s o {parte_alvo.nome} e gastou {energia_gasta} % de energia."
        print(mensagem)
        robo_inimigo.partes[parte_para_atacar].reducao_defesa(self.partes[parte_para_usar].nivel_ataque)
        self.energia -= energia_gasta

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

    def mostrar_partes(self):
        print("Partes do Robô:")
        for i, parte in enumerate(self.partes):
            print(f"{i}: {parte}")

    def verificar_vencedor(self):
        if not self.esta_ligado():
            print(f"{self.nome} está desligado. {self.nome} perdeu o jogo!")
            return True
        if not self.ha_uma_peca_disponivel():
            print(f"{self.nome} não tem mais peças disponíveis. {self.nome} perdeu o jogo!")
            return True
        return False


robo_art = r"""
          0: {nome_cabeca}
          Is available: {status_cabeca}
          Attack: {ataque_cabeca}
          Defense: {defesa_cabeca}
          Energy consumption: {energia_cabeca}
                  ^
                  |              |1: {nome_arma}
                  |              |Is available: {status_arma}
         ____     |    ____    |Attack: {ataque_arma}
        |oooo|  ____  |oooo| --> |Defense: {defesa_arma}
        |oooo| '    ' |oooo|     |Energy consumption: {energia_arma}
        |oooo|/\_||_/\|oooo|
        `----' / __ \  `----'     |2: {nome_arma_esq}
       '/  |#|/\/__\/\|#|  \'     |Is available: {status_arma_esq}
       /  \|#|| |/\| ||#|/  \     |Attack: {ataque_arma_esq}
      / \_/|_|| |/\| ||_|\_/ \    |Defense: {defesa_arma_esq}
     |_\/    O\=----=/O    \/_|   |Energy consumption: {energia_arma_esq}
     <_>      |=\__/=|      <_> --> |
     <_>      |------|      <_>     |3: {nome_arma_dir}
     | |   ___|======|___   | |     |Is available: {status_arma_dir}
    // \\ / |O|======|O| \  //\\    |Attack: {ataque_arma_dir}
    |  |  | |O+------+O| |  |  |    |Defense: {defesa_arma_dir}
    |\/|  \_+/        \+_/  |\/|    |Energy consumption: {energia_arma_dir}
    \__/  _|||        |||_  \__/
          | ||        || |          |4: {nome_perna_esq}
         [==|]        [|==]         |Is available: {status_perna_esq}
         [===]        [===]         |Attack: {ataque_perna_esq}
          >_<          >_<          |Defense: {defesa_perna_esq}
         || ||        || ||         |Energy consumption: {energia_perna_esq}
         || ||        || || --> |
         || ||        || ||         |5: {nome_perna_dir}
       __|\_/|__    __|\_/|__       |Is available: {status_perna_dir}
      /___n_n___\  /___n_n___\      |Attack: {ataque_perna_dir}
                                    |Defense: {defesa_perna_dir}
                                    |Energy consumption: {energia_perna_dir}
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
    print(robo_art)
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

        print('Escolha a parte para usar e a parte do inimigo para atacar:')
        parte_para_usar = int(input('Escolha uma parte para atacar o inimigo:'))
        parte_para_atacar = int(input('Escolha uma peça do inimigo para atacar:'))

        if parte_para_usar < 0 or parte_para_usar >= len(
                robo_atual.partes) or parte_para_atacar < 0 or parte_para_atacar >= len(robo_inimigo.partes):
            print('Escolha inválida. Tente novamente.')
            continue

        robo_atual.atacar(robo_inimigo, parte_para_usar, parte_para_atacar)
        rodada += 1

        if robo_atual.verificar_vencedor():
            jogando = False


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
