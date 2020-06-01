import requests
import pandas

# Relatório de Taxa de Juros - Pessoa Física - Financiamento imobiliário com taxas de mercado
# https://www.bcb.gov.br/estatisticas/reporttxjuros?path=conteudo%2Ftxcred%2FReports%2FTaxasCredito-Consolidadas-porTaxasAnuais-ModalidadeMensal.rdl&nome=Pessoa%20F%C3%ADsica%20-%20Financiamento%20imobili%C3%A1rio%20com%20taxas%20de%20mercado&parametros=tipopessoa:1;modalidade:903;encargo:201&exibeparametros=false&exibe_paginacao=false
url = 'https://www.bcb.gov.br/api/relatorio/pt-br/contaspub?path=conteudo/txcred/Reports/TaxasCredito-Consolidadas-porTaxasAnuais-ModalidadeMensal.rdl&parametros=tipopessoa:1;modalidade:903;encargo:201&exibeparametros=false'
conteudo_pagina = requests.get(url).json()

df_list = pandas.read_html(conteudo_pagina['conteudo'], decimal=',', thousands='.')
df = df_list[9]
df.head()

print('\n*** Taxas de Mercado para Financiamento Imobiliário ***\nURL = ' + url)
for i in range(2, len(df)):
    print(df.iloc[i][0], df.iloc[i][1], df.iloc[i][2], df.iloc[i][3])

# Relatório de Taxa de Juros - Pessoa Física - Cheque especial
# https://www.bcb.gov.br/estatisticas/reporttxjuros/?path=conteudo%2Ftxcred%2FReports%2FTaxasCredito-Consolidadas-porTaxasAnuais.rdl&nome=Pessoa%20F%C3%ADsica%20-%20Cheque%20especial&parametros=tipopessoa:1;modalidade:216;encargo:101&exibeparametros=false&exibe_paginacao=false
url = 'https://www.bcb.gov.br/api/relatorio/pt-br/contaspub?path=conteudo/txcred/Reports/TaxasCredito-Consolidadas-porTaxasAnuais.rdl&parametros=tipopessoa:1;modalidade:216;encargo:101&exibeparametros=false'
conteudo_pagina = requests.get(url).json()

df_list = pandas.read_html(conteudo_pagina['conteudo'], decimal=',', thousands='.')
df = df_list[10]
df.head()

print('\n*** Taxa de Juros para Cheque Especial ***\nURL = ' + url)
for i in range(2, len(df)):
    print(df.iloc[i][0], df.iloc[i][1], df.iloc[i][2], df.iloc[i][3])
