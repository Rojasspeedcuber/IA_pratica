import time


def expandir_modificando(estado):
    """
    Expande o estado atual modificando diretamente o estado do pai,
    mas criando cópias para não afetar outros caminhos.
    """
    filhos = []
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:  # Encontra a posição do espaço vazio
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Movimentos possíveis
                    x, y = i + dx, j + dy
                    if 0 <= x < 3 and 0 <= y < 3:  # Verifica se o movimento é válido
                        estado_copia = [linha[:] for linha in estado]  # Cria uma cópia do estado
                        estado_copia[i][j], estado_copia[x][y] = estado_copia[x][y], estado_copia[i][j]  # Troca as peças
                        filhos.append(estado_copia)  # Adiciona o novo estado à lista de filhos
    return filhos



def expandir_copiando(estado):
    """
    Expande o estado atual criando uma cópia do estado do pai e editando a cópia.

    Args:
        estado (list): Estado atual do quebra-cabeça de 8 peças.

    Returns:
        list: Lista de estados filhos.
    """
    filhos = []
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:  # Encontra a posição do espaço vazio
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Movimentos possíveis
                    x, y = i + dx, j + dy
                    if 0 <= x < 3 and 0 <= y < 3:  # Verifica se o movimento é válido
                        estado_copia = [linha[:] for linha in estado]  # Cria uma cópia do estado
                        estado_copia[i][j], estado_copia[x][y] = estado_copia[x][y], estado_copia[i][
                            j]  # Troca as peças
                        filhos.append(estado_copia)
    return filhos


def busca_profundidade_iterativa(estado_inicial, funcao_expansao, limite=20):
    pilha = [(estado_inicial, [], 0)]  # Adicionando profundidade inicial
    visitados = set()

    while pilha:
        estado, caminho, profundidade = pilha.pop()

        estado_tuple = tuple(tuple(linha) for linha in estado)

        if estado_tuple in visitados:
            continue

        visitados.add(estado_tuple)

        if estado == [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 0]]:  # Verifica se o estado é a solução
            return caminho + [estado]

        if profundidade < limite:  # Só expande se não ultrapassou o limite
            for filho in funcao_expansao(estado):
                pilha.append((filho, caminho + [estado], profundidade + 1))

    return None





estado_inicial = [[4, 1, 3], [7, 2, 6], [5, 8, 0]]

inicio = time.time()
solucao_copiando = busca_profundidade_iterativa(estado_inicial, expandir_copiando)
fim = time.time()
print(f"Tempo de execução com expansão copiando: {fim - inicio} segundos")

inicio = time.time()
solucao_modificando = busca_profundidade_iterativa(estado_inicial, expandir_modificando)
fim = time.time()
print(f"Tempo de execução com expansão modificando: {fim - inicio} segundos")

solucao = busca_profundidade_iterativa(estado_inicial, expandir_copiando)
print("Solução copiando:")
i = 1
for estado in solucao:
    print(f"Estado {i}:")
    print(estado[0], '\n',
          estado[1], '\n',
          estado[2])
    print("--------------------")
    i += 1

solucao = busca_profundidade_iterativa(estado_inicial, expandir_modificando)
print("Solução modificando:")
i = 1
for estado in solucao:
    print(f"Estado {i}:")
    print(estado[0], '\n',
          estado[1], '\n',
          estado[2])
    print("--------------------")
    i += 1

