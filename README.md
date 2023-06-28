# pyProva

## Instruções para backend e banco de dados
#### Com o [poetry](https://python-poetry.org) instalado, execute:
```
poetry install
```
#### Inicie o ambiente virtual gerado:
```
poetry shell
```
#### Inicie a aplicação backend:
```
flask run
```
#### Crie a instância de banco de dados:
```
flask db init
```
#### Identifique as [migrações](https://flask-migrate.readthedocs.io/en/latest/) necessárias:
```
flask db migrate -m "alguma mensagem"
```
#### Execute as migrações
```
flask db upgrade
```
## Instruções para o frontend
#### navegue para a pasta da aplicação:
```
cd pyprova-ui
```
#### Instale as dependências (versão utilizada do node: v18.15.0, recomenda-se [nvm](https://github.com/nvm-sh/nvm))
```
npm install
```
#### Inicie a aplicação frontend:
```
npm run dev
```