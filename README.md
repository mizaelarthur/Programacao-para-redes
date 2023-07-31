# Programação para redes

**Descrição**

Este projeto é uma aplicação cliente-servidor implementada em Python, utilizando sockets TCP para permitir a comunicação entre os clientes e o servidor. O servidor é capaz de lidar com várias conexões simultâneas e responder aos comandos enviados pelos clientes.

**Configuração**

Antes de executar o servidor e o cliente, é necessário configurar a chave de API e o ID do bot do Telegram. Para isso, abra o arquivo `server.py` e localize as seguintes variáveis globais:

```python
chat_api = "INSIRA_SUA_CHAVE_API_DO_TELEGRAM"
id_chave = "INSIRA_O_ID_DO_CHAT_DO_TELEGRAM"
```

Substitua `"INSIRA_SUA_CHAVE_API_DO_TELEGRAM"` pela chave de API do seu bot do Telegram e `"INSIRA_O_ID_DO_CHAT_DO_TELEGRAM"` pelo ID do chat onde você deseja receber as notificações do servidor.

**Executando o Servidor**

Para executar o servidor, basta executar o arquivo `server.py` no terminal:

```
python server.py
```

O servidor iniciará e estará pronto para receber conexões de clientes.

**Executando o Cliente**

Para executar o cliente, abra um novo terminal e execute o arquivo `client.py`:

```
python client.py
```

O cliente se conectará automaticamente ao servidor e você poderá começar a enviar comandos.

**Comandos Disponíveis**

Aqui estão os comandos disponíveis que você pode enviar pelo cliente:

- `/q`: Desconecta o cliente do servidor.
- `/l`: Lista o IP e a porta de todos os clientes conectados.
- `/m:ip_destino:porta:mensagem`: Envia a mensagem especificada para o IP e porta de destino.
- `/b:mensagem`: Envia a mensagem especificada para todos os clientes conectados.
- `/h`: Lista todas as mensagens e comandos enviados pelo cliente (histórico).
- `/?`: Exibe uma ajuda listando os comandos possíveis.
- `/rss:palavra_chave`: Lista as 10 notícias mais recentes que contenham a palavra-chave.
- `/f`: Lista os arquivos (nome e tamanho) contidos na pasta `/server_files` do servidor.

**Observações**

- Certifique-se de ter o Python instalado em seu sistema.
- O servidor precisa ser executado antes do cliente.
- Verifique se as bibliotecas necessárias (como `requests` e `feedparser`) estão instaladas. Caso contrário, instale-as com `pip install requests feedparser`.

Agora você está pronto para testar esta aplicação cliente-servidor! Divirta-se explorando os comandos e a comunicação entre o cliente e o servidor. Se você tiver alguma dúvida ou encontrar algum problema, fique à vontade para entrar em contato ou abrir uma issue neste repositório.

