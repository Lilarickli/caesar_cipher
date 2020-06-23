# UTF-8
import urllib.request, urllib.parse, json, hashlib, requests
with urllib.request.urlopen("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=4b0899f17b073a88147af476e113975a36c74087") as url:
    data = json.loads(url.read().decode())
    # print(data)


cifrado = data["cifrado"]
casas = data["numero_casas"]
alfabeto = list(map(chr, range(97, 123)))


decifrado = ""
for i in cifrado:
    if i in alfabeto:
        index = alfabeto.index(i)
        decifrado = decifrado + alfabeto[index - casas]
    else:
        decifrado = decifrado + i

data["decifrado"] = decifrado

hash = hashlib.sha1(decifrado.encode()).hexdigest()
data["resumo_criptografico"] = hash

data_string = json.dumps(data).encode('utf-8')
print(data_string)
print(data)

# def writeToJSONFile(path, answer, decifrado):
#     filePathNameWExt = './' + '' + '/' + answer + '.json'
#     with open(filePathNameWExt, 'w') as fp:
#         json.dump(data, fp)
#

answer = {'answer': open('answer.json', 'rb')}
url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=4b0899f17b073a88147af476e113975a36c74087'
submit = requests.post(url, files=answer)
print(submit.text)


# O primeiro passo é você salvar o conteúdo do JSON em um arquivo com o nome answer.json, que irá usar no restante do desafio.
# Você deve usar o número de casas para decifrar o texto e atualizar o arquivo JSON, no campo decifrado.
# O próximo passo é gerar um resumo criptográfico do texto decifrado usando o algoritmo sha1 e atualizar novamente o arquivo JSON.
# OBS: você pode usar qualquer biblioteca de criptografia da sua linguagem de programação favorita para gerar o resumo sha1 do texto decifrado.
# a API espera um arquivo sendo enviado como multipart/form-data, como se fosse enviado por um formulário HTML,
# com um campo do tipo file com o nome answer. Considere isso ao enviar o arquivo


