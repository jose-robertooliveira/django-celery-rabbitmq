# Gestão de Proposta
Execução e comandos da API do projeto.

# O projeto na sua maior parte pode ser executado com docker compose:
1 -Para executar o projeto a primeira vez:    - docker compose up --build.

2 -Para reexecutar após buildar a primeira vez isso em background:
- docker compose up -d ou
- docker compose up --build --force-recreate "vizualisando os outputs"

3 -Criar um super usuário para o admin do django use o seguinte comando com docker:
- docker compose run djsource python manage.py createsuperuser.
Após isso é possivel acessar o admin, com as cridênciais que foram setadas.

4 -Será necessário instalar o Celery use o comando:
- pip3 install celery, após instalar o celery, entre na pasta raiz "djsource"e veja a execução das tasks, também é possivel acompanhar a fila na interface do rabbitmq usando as credencias do .env.