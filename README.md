# Clone da Netflix

Este é um projeto de clone da Netflix desenvolvido como parte do treinamento oferecido pela Hashtag Treinamentos. O projeto é dividido em duas partes: o backend, construído com Python e Django, e a parte visual, desenvolvida individualmente com HTML, CSS e JavaScript para aprimorar minhas habilidades.

## Funcionalidades

- **Autenticação de Usuário**: O projeto oferece autenticação de usuário, permitindo que os usuários criem contas e façam login de forma segura.

- **Páginas para Usuários Logados**: Após fazer login, os usuários têm acesso a páginas exclusivas com conteúdo relacionado ao serviço de streaming.

- **Redirecionamento**: O projeto implementa redirecionamentos para direcionar os usuários para as páginas corretas com base em suas ações.

## Tecnologias Utilizadas

- **Backend**: O backend é desenvolvido em Python usando o framework Django, que oferece recursos poderosos para criar aplicativos da web.

- **Frontend**: A parte visual do projeto é construída com HTML, CSS e JavaScript, proporcionando uma experiência interativa e atraente aos usuários.

## Como Executar o Projeto

Siga estas etapas para executar o projeto em sua máquina local:

1. Clone o repositório:
git clone https://github.com/michelebswm/site_com_django.git


2. Configure o ambiente virtual (recomendado):
python -m venv venv


3. Ative o ambiente virtual:
- No Windows:
  ```
  venv\Scripts\activate
  ```
- No macOS e Linux:
  ```
  source venv/bin/activate
  ```

4. Instale as dependências:
pip install -r requirements.txt


5. Aplique as migrações do banco de dados:
python manage.py migrate


6. Inicie o servidor de desenvolvimento:
python manage.py runserver


7. Acesse o projeto no seu navegador em `http://localhost:8000/`

## Contribuições

Contribuições são bem-vindas! Se você gostaria de contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

- [Michele Santos](https://github.com/michelebswm) - Desenvolvedor(a) do Projeto

## Agradecimentos

- Hashtag Treinamentos - Pelo treinamento que inspirou este projeto.

