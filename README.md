# blitz_auto

Automação Blitz RH (Sydle + rotinas).
# Blitz Auto — Organizador

Organiza relatórios baixados do SYDLE: move/renomeia e registra log.

## Como rodar
- Via Python: `python -m src.run_all`
- Via atalho: `run_all.bat` (ativa venv e roda tudo)

Logs: `R:\User\bases\Logs automação\log sydle.txt`  
Formato: `YYYY-MM-DD HH:MM:SS | ACTION | filename | folder`  
Ações: `HIST`, `BASES`, `ATUAL`, `R2`, `MISS`, `START`, `DONE`.

## Regras
- **Relatório 01 – DCex – Dados do monitoramento de demandas**
  - Histórico → `R:\User\bases\Relatórios sydle\01 - historico`  
    Nome: `… # dd.mm.aa-x` (não sobrescreve; incrementa `x`).
  - 01 – mais atual → `R:\User\bases\Relatórios sydle\01 - mais atual`  
    Nome: `… # dd.mm.aa` (1 por dia; sobrescreve do mesmo dia).
  - Bases Comuns SYDLE → `R:\User\bases\Relatórios sydle\Bases Comuns SYDLE`  
    Nome: **sem data** (sempre sobrescreve).

- **Relatórios 2** (arquivos que começam por `02`–`12`, `07`, `13`, `14`, `15`)
  - Destino → `R:\User\bases\Relatórios sydle\Relatórios 2`  
    Mantém **nome original** (sobrescreve).  
  - Se não encontrado: log `MISS`.

- **Bases extras**  
  - `Painel geral de demandas`, `Demandas canceladas`,  
    `Demandas por Empresa e Centro de custo`, `Painel de demandas não trabalhadas`  
  - Destino → **Bases Comuns SYDLE** (mantém nome; sobrescreve).  
  - Se não encontrado: `MISS`.

## Config
- Editar caminhos em `src/utils/paths.py` (Downloads, pastas da rede).
