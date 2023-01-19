import requests
import pprint


link = "https://servicodados.ibge.gov.br/api/v3/agregados/1278/periodos/2006/variaveis/323?localidades=N1[all]"

requisição = requests.get(link)
requi_dic = requisição.json()


pprint.pprint(requi_dic[0]["resultados"])