## Como Executar?
Abra um terminal de sua preferência e siga as instruções abaixo:

## 1 - Clone o repositório
git clone linkAqui
## 2 - Abra o Projeto no Vscode
code .
## 3 - Instale as dependencias do projeto:
pip install -r requirements.txt
## 4 - Execute as migrações:
python manage.py makemigrations

python manage.py migrate
## 5 - Execute o projeto
python manage.py runserver
##### Caso tenha ocorrido tudo certo, aparecerá um endereço como esse em seu terminal: https://127.0.0.1:8000/
## 6 - Abra o navegador de sua preferência e acesse o endereço disponibilizado na etapa anterior.
