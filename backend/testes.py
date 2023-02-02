import requests,json 
herois_data = { "herois": [
            {
                "nome": "3-D Man",
                "descricao": "Desc",
                "imagem": "http://imagem.jpg"
            },
            {
                "nome": "Hulk",
                "descricao": "Desc",
                "imagem": "http://imagem.jpg"
            },
        ]
}

heroi = {
    "equipe": 2,
    "herois": [
    		{
                "nome": "3-D Man",
                "descricao": "Desc",
                "imagem": "http://imagem.jpg"
            },
            {
                "nome": "Hulk",
                "descricao": "Desc",
                "imagem": "http://imagem.jpg"
            },
            ]
}

vinculo = {"equipe":1,"heroi": 1}


equipe_data = {"nome": "equipe04"}

headers = {"Content-Type": "application/json"}
#r=requests.post("http://localhost:5000/equipe", data = json.dumps(equipe_data), headers = headers)
#r=requests.post("http://localhost:5000/heroi", data = json.dumps(heroi), headers = headers)
#r=requests.post("http://localhost:5000/add", data = json.dumps(vinculo), headers = headers)

#r = requests.get("http://localhost:5000/equipe")
#r = requests.get("http://localhost:5000/heroi")

print(r)
print(r.text)