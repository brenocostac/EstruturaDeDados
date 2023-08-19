from pontos import Ponto

def lerArquivo(nomeArquivo):
    with open(nomeArquivo,'r') as arquivo:
        linhas = arquivo.readlines()
    pontos = [Ponto(linhas[i].strip(),*linhas[i+1].strip().split())
                        for i in range(0,len(linhas),2)]
    return pontos


pontos = lerArquivo('pontos.txt')

for ponto in pontos:
    print(ponto)