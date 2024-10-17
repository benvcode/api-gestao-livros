import pytest
from flask import json

@pytest.mark.parametrize(
   "test_app", ["config.DevConfig"], indirect=True
)
def test_api_create_livro(test_app):
   client = test_app.test_client()

   # --- Seção de Criação do Livro ---
   novo_livro = {
      "isbn": "1234567890123",
      "titulo": "Teste de Livro",
      "num_paginas": 200,
      "autores": [{"nome": "Autor Teste"}] 
   }

   # Chamar a API para criar um novo livro
   response = client.post('gestao-livros/api/v1/livros', json=novo_livro)
   assert response.status_code == 201 

   # --- Seção de Listagem de Livros ---
   response = client.get('gestao-livros/api/v1/livros')
   assert response.status_code == 200 

   data = json.loads(response.data)
   print("\nDados retornados da API de Livros:", data)  

   # --- Seção de Listagem de Autores ---
   response = client.get('gestao-livros/api/v1/autores')
   assert response.status_code == 200 

   data = json.loads(response.data)
   print("\nDados retornados da API de Autores:", data)