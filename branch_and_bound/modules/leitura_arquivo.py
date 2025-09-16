# leitura_arquivo
def ler_arquivo(path):
  try:
    with open(path, 'r') as arquivo:
      # Lê a primeira linha: quantidade de variáveis (n) e quantidade de restrições (m)
      n, m = map(int, arquivo.readline().strip().split())

      # Lê a segunda linha: coeficientes das variáveis na função objetivo
      coeficientes_objetivo = list(map(int, arquivo.readline().strip().split()))

      # Lê as próximas linhas: coeficientes das variáveis em cada uma das restrições e os termos independentes em cada uma das restrições também
      restricoes = []
      valores_direita = []
      for _ in range(m):
        linha = list(map(float, arquivo.readline().strip().split()))
        restricoes.append(linha[:-1])  # coeficientes das variáveis (lista de listas) - retira o último elemento da linha, que é o termo independente
        valores_direita.append(linha[-1])  # valor à direita da desigualdade - só recebe o último elemento da linha

      # Retorna os dados lidos
      return n, m, coeficientes_objetivo, restricoes, valores_direita

  except FileNotFoundError:
    print(f"O arquivo {path} não foi encontrado.")
    return None, None, None, None, None
  except ValueError:
    print(f"Erro ao processar o arquivo '{path}'. Verifique o formato.")
    return None, None, None, None, None