contatos = {"alinne@gmail.com": {"nome": "aline", "telefone": "3333-2221"}}

contatos.update({"alinne@gmail.com": {"nome": "line"}})
print(contatos)  # {'alinne@gmail.com': {'nome': 'line'}}

contatos.update({"mello@gmail.com": {"nome": "melo", "telefone": "3322-8181"}})
# {'alinne@gmail.com': {'nome': 'line'}, 'mello@gmail.com': {'nome': 'melo', 'telefone': '3322-8181'}}
print(contatos)
