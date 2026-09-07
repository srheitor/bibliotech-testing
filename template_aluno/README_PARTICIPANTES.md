# BiblioTech — Missão QA

Projeto criado como atividade prática para a UC de de Qualidade de Software com o sistema de biblioteca BiblioTech.

## Integrantes da equipe

Gustavo Edson 325111696 e Heitor Souza 325124517

## Objetivo

Realizar a análise e os testes da biblioteca BiblioTech, aplicando técnicas de teste de caixa preta e caixa branca, testes de fronteira, testes automatizados e análise de cobertura.

## Atividades realizadas

- Elaboração do Mini Plano de Testes;
- Criação dos roteiros e casos de teste;
- Construção da matriz de rastreabilidade;
- Implementação de testes automatizados utilizando `pytest`;
- Análise de cobertura de linhas e branches;
- Identificação e documentação de defeitos;
- Elaboração do parecer final de QA.

## Resultados

Foram executados **11 testes**:

- ✅ 10 testes aprovados;
- ❌ 1 teste reprovado;

O teste reprovado identificou um defeito no RF01 relacionado ao status do aluno.

## Estrutura do código
.
├── docs/
│   ├── plano_testes.md
│   ├── roteiro_testes.md
│   ├── matriz_rastreabilidade.md
│   └── parecer_qa.md
│
├── src/
│   └── bibliotech.py
│
├── tests/
│   ├── test_bibliotech.py
│   └── test_smoke.py
│
└── .github/
    └── workflows/
        └── tests.yml