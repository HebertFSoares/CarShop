# CarShop
Uma plataforma web desenvolvida para entusiastas automotivos e compradores em busca de sua próxima jornada sobre rodas. Nossa aplicação oferece uma experiência intuitiva de compra de carros, permitindo que os usuários explorem uma ampla variedade de veículos.


## Funcionalidades
- Cadastro de Usuário: Os usuários podem se cadastrar no sistema fornecendo suas informações básicas, como nome, e-mail e senha.
- Login de Usuário: Os usuários podem fazer login no sistema utilizando seu e-mail e senha.
- Cadastro de Veículos: Os usuários autenticados podem cadastrar novos veículos fornecendo informações como marca, modelo, ano, preço.
- Visualização de Detalhes do Veículo: Os usuários podem visualizar detalhes específicos de um veículo, incluindo todas as suas informações.
- Edição de Veículo: Os usuários autenticados têm a capacidade de editar as informações de um veículo existente.
- Exclusão de Veículo: Os usuários autenticados podem excluir um veículo do sistema.
- Pesquisa de Veículos: Os usuários podem pesquisar veículos com base em critérios específicos, como marca, modelo, ano, etc.

## Tecnologias Utilizadas
- Python
- Django
- Sqlite
- HTML/CSS
- Bootstrap
- OpenAI GPT-3

## Requisitos
### Para executar o projeto em sua máquina local, você precisará ter o Python 3 instalado. Além disso, recomendamos utilizar um ambiente virtual para instalar as dependências necessárias.

## Instalação

### Clone este repositório em sua máquina local.

- Crie um ambiente virtual:
```
python3 -m venv myenv
```
- Ative o ambiente virtual:
```
source myenv/bin/activate
```
- Instale as dependências:
```
pip install -r requirements.txt
```
- Execute as migrações do banco de dados:
```
python manage.py migrate
```
- Crie um superusuário:
```
python manage.py createsuperuser
```
- Execute o servidor:
```
python manage.py runserver
```
## Uso da API da OpenAI
Este projeto também utiliza a API da OpenAI, especificamente o modelo GPT-3, para gerar descrições de venda para os veículos cadastrados. Através dessa integração, as descrições são geradas automaticamente com base nas informações do veículo.

## Contribuição
Este projeto é de código aberto e contribuições são bem-vindas. Se você quiser contribuir com o projeto, por favor, abra uma issue ou um pull request.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
