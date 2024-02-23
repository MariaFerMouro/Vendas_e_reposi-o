import os, csv
#importa pastas da pasta venda
caminhovendas = r'C:/Users/Maria Fernanda/PycharmProjects/estudos_independentes/Vendas_e_devolucoes/Vendas'
listavendas = list()
listageral = []
for arquivos in os.listdir(caminhovendas):
    if 'Vendas' in arquivos:
        listavendas.append(arquivos)
        #importa arquivos relacionados a vendas
        caminho = rf'C:/Users/Maria Fernanda/PycharmProjects/estudos_independentes/Vendas_e_devolucoes/Vendas/{arquivos}'
        with open(caminho, 'r') as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                listageral.append(linha)
#Contabiliza os produtos
produto = []
televisao = 0
iphone = 0
notebook =0
smartwatch = 0
tablet = 0
camera =0
android =0
quantidades = {}
for c in listageral:
    if c[2] == 'TelevisÃ£o':
        televisao += int(c[3])
    if c[2] == 'iPhone':
        iphone += int(c[3])
    if c[2] == 'Notebook':
        notebook += int(c[3])
    if c[2] == 'SmartWatch':
        smartwatch += int(c[3])
    if c[2] == 'Tablet':
        tablet += int(c[3])
    if c[2] == 'CÃ¢mera':
        camera += int(c[3])
    if c[2] == 'Android':
        android += int(c[3])
    if c[2] not in produto:
        produto.append(c[2])
quantidades['telvisao'] = televisao
quantidades['iphone'] = iphone
quantidades['notebook'] = notebook
quantidades['smatwatch'] = smartwatch
quantidades['tablet'] = tablet
quantidades['camera'] = camera
quantidades['android'] = android
#analisa qual é o produto mais vendido
maior = 0
prodmvend = 0
contador = 0
for k,v in quantidades.items():
    contador +=1
    if contador == 1:
        prodmvend = k
        maior = v
    if contador > 1 and v > maior:
        prodmvend = k
        maior = v
print(f'O produto mais vendido: {prodmvend} com {maior}'
      '\nO produto que mais faturou: {}'
      '\nLoja que mais vendeu: {}')