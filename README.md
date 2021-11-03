# Andromeda Server

## Utilização

A utilização de containers docker no desenvovimento da aplicação facilitam a configuração de um ambiente unificado, sendo assim, para iniciar o desenvolvimento
é necessário buildar a aplicação com o seguinte comando:

`docker-compose build`

Após a execução do comando basta subir o serviço com o comando:

`docker-compose up`

## Testes

A ferramenta selecionada para a construção dos testes unitários foi a biblioteca Pytest, sendo assim,
para executar os testes da aplicação basta executar seguinte comando no terminal:

`docker-compose run gui pytest`

## Deploy

Com a finalidade de criar um fluxo automático de deploy e estar alinhado com as tendências de CI/CD foi
desenvolvida uma pipelina de deploy contínuo baseado em tags nas branches `main` e `devel`. As tags geradas
na branch `devel` devem seguir o padrão `vX.Y.Z-dev.A` e representam o ambiente de staging da aplicação,
já as tags criadas na branch `main` devel seguir o padrão de `vX.Y.Z` e representam o ambiente de production da aplicação.

Em ambos os casos ao gerar uma nova tag uma action Action é disparada usando GitHub Actions, dentro dessa
action são executados os testes unitários e em caso de sucesso são executados os passos de `build` e `deploy`.
No passo de `build` é gerada uma imagem docker para a versão em questão que posteriomente é enviada para o
[registry do próprio repositório](https://github.com/medeiroslucas/andromeda-server/packages/1073996).
E por fim no passo de `deploy` a imagem gerada no passo de build é enviada para um servidor Heroku onde
o deploy é feito automaticamente, disponibilizando a aplicação para uso.

## Ambientes

**Staging:** https://staging-pi2-andromeda-server.herokuapp.com/

**Production:** https://pi2-andromeda-server.herokuapp.com/
