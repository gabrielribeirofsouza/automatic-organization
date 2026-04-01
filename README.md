# Organizador Automático de Arquivos

Script em Python para organizar arquivos automaticamente com base em suas extensões.

## Funcionalidades
- Varre uma pasta de origem
- Identifica a extensão dos arquivos
- Move para pastas específicas
- Cria pastas automaticamente
- Evita sobrescrever arquivos com o mesmo nome

## Tecnologias
- Python
- pathlib
- shutil

## Como executar

Instalação das Dependências

Execute no **Python global** (fora de qualquer venv):

```bash
pip install pywin32 watchdog
python -m pywin32_postinstall

##  Requisitos Importantes

**Este projeto NÃO deve ser executado a partir de um virtualenv (venv) quando usado como serviço do Windows.**

Execução como Serviço do Windows
    1. Abrir terminal como administrador
    2. Navegar até a pasta do projeto
    3. Instalar serviço
    4. Iniciar o seviço
    
> Serviços do Windows não herdam variáveis de ambiente do usuário, o que causa falhas de inicialização (erro 1053).

```bash
