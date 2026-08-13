# Organizador Automático de Arquivos

Automação em Python que monitora uma pasta e organiza arquivos em subpastas de acordo com suas extensões.

## Funcionalidades

- identifica o tipo do arquivo pela extensão;
- cria automaticamente as pastas de destino;
- move arquivos sem sobrescrever itens com o mesmo nome;
- registra as operações em log;
- pode ser executado como serviço do Windows.

## Tecnologias

- Python
- `pathlib`
- `shutil`
- `watchdog`
- `pywin32`

## Execução local

1. Instale as dependências:

```bash
pip install pywin32 watchdog
python -m pywin32_postinstall
```

2. Ajuste no código o caminho da pasta que será monitorada.
3. Execute:

```bash
python organizador.py
```

## Execução como serviço do Windows

Para uso como serviço, execute o terminal como administrador e instale as dependências no Python disponível ao serviço. Ambientes virtuais e variáveis do usuário podem não estar acessíveis ao processo do Windows.

```bash
python service.py install
python service.py start
```

Para interromper ou remover:

```bash
python service.py stop
python service.py remove
```

## Arquivos de demonstração

A pasta `origem` contém arquivos usados para demonstrar a classificação. Logs, caches do Python e ambientes locais não devem ser versionados.

## Limitações

- os caminhos precisam ser configurados para o ambiente de execução;
- a execução como serviço depende do Windows;
- o projeto ainda não possui uma suíte automatizada de testes.
