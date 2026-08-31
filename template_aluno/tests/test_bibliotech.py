import pytest
from src.bibliotech import pode_emprestar, calcular_multa, classificar_atraso

# ==============================================================================
# 1. TESTES PARA: pode_emprestar (RF01)
# Requisito: Usuário ativo, sem pendência e com MENOS de 3 empréstimos (< 3)
# ==============================================================================

def test_pode_emprestar_cenario_valido():
    """
    [Cenário Válido]
    Usuário atende a todas as condições ideais: ativo, sem pendências e com 0 empréstimos.
    """
    resultado = pode_emprestar(usuario_ativo=True, possui_pendencia=False, emprestimos_ativos=0)
    assert resultado is True


def test_pode_emprestar_cenario_invalido():
    """
    [Cenário Inválido]
    Usuário inativo e com pendência, mesmo que tenha 0 empréstimos ativos.
    """
    resultado = pode_emprestar(usuario_ativo=False, possui_pendencia=True, emprestimos_ativos=0)
    assert resultado is False


def test_pode_emprestar_limite_inferior():
    """
    [Limite Inferior de Negação]
    Usuário com 2 empréstimos ativos (é o maior valor válido antes do limite).
    Deve retornar True.
    """
    resultado = pode_emprestar(usuario_ativo=True, possui_pendencia=False, emprestimos_ativos=2)
    assert resultado is True


def test_pode_emprestar_limite_superior():
    """
    [Limite Superior / Fronteira - REVELA O DEFEITO PROPOSITAL]
    Usuário com exatamente 3 empréstimos ativos.
    Como o requisito exige "menos de 3", o retorno deve ser False.
    Nota: Este teste irá FALHAR no código original devido ao defeito (> LIMITE em vez de >= LIMITE).
    """
    resultado = pode_emprestar(usuario_ativo=True, possui_pendencia=False, emprestimos_ativos=3)
    assert resultado is False


# ==============================================================================
# 2. TESTES PARA: calcular_multa (RF02)
# Requisito:
# - <= 0 dias: R$ 0.00
# - 1 a 7 dias: R$ 2.00 por dia
# - > 7 dias: R$ 14.00 + R$ 3.00 por dia excedente
# ==============================================================================

def test_calcular_multa_cenario_valido():
    """
    [Cenário Válido]
    Atraso intermediário de 3 dias (faixa de R$ 2,00 por dia).
    Esperado: 3 * 2.0 = R$ 6,00.
    """
    resultado = calcular_multa(dias_atraso=3)
    assert resultado == pytest.approx(6.0)


def test_calcular_multa_cenario_invalido():
    """
    [Cenário Inválido / Sem Multa]
    Devolução antecipada ou no prazo (dias negativos ou zero).
    Esperado: R$ 0,00.
    """
    resultado = calcular_multa(dias_atraso=-2)
    assert resultado == pytest.approx(0.0)


def test_calcular_multa_limite_inferior():
    """
    [Limite Inferior da Faixa Leve]
    Exatamente 1 dia de atraso (início da cobrança).
    Esperado: 1 * 2.0 = R$ 2,00.
    """
    resultado = calcular_multa(dias_atraso=1)
    assert resultado == pytest.approx(2.0)


def test_calcular_multa_limite_superior():
    """
    [Limite Superior da Faixa Leve / Transição]
    Exatamente 7 dias de atraso (fronteira entre taxa simples e taxa excedente).
    Esperado: 7 * 2.0 = R$ 14,00.
    """
    resultado = calcular_multa(dias_atraso=7)
    assert resultado == pytest.approx(14.0)


# ==============================================================================
# 3. TESTES PARA: classificar_atraso (RF03)
# Requisito:
# - 0 dias: "sem atraso"
# - 1 a 7: "atraso leve"
# - 8 a 30: "atraso moderado"
# - > 30: "atraso grave"
# ==============================================================================

def test_classificar_atraso_cenario_valido():
    """
    [Cenário Válido / Faixa Intermediária]
    Atraso de 15 dias (se enquadra no meio da faixa "atraso moderado").
    """
    resultado = classificar_atraso(dias_atraso=15)
    assert resultado == "atraso moderado"


def test_classificar_atraso_cenario_invalido():
    """
    [Cenário Inválido / Sem Atraso]
    Zero ou dias negativos não configuram atraso.
    """
    resultado = classificar_atraso(dias_atraso=0)
    assert resultado == "sem atraso"


def test_classificar_atraso_limite_inferior():
    """
    [Limite Inferior de Atraso Leve]
    Exatamente 1 dia de atraso.
    """
    resultado = classificar_atraso(dias_atraso=1)
    assert resultado == "atraso leve"


def test_classificar_atraso_limite_superior():
    """
    [Limite Superior de Atraso Grave]
    Exatamente 31 dias de atraso (primeiro valor da faixa "atraso grave").
    """
    resultado = classificar_atraso(dias_atraso=31)
    assert resultado == "atraso grave"
