import pytest
from src.bibliotech import pode_emprestar, calcular_multa, classificar_atraso

def test_rf01_usuario_ativo_sem_pendencia_zero_emprestimos():
    assert pode_emprestar(usuario_ativo=True, possui_pendencia=False, emprestimos_ativos=0) is True

def test_rf01_usuario_inativo():
    assert pode_emprestar(usuario_ativo=False, possui_pendencia=False, emprestimos_ativos=0) is False

def test_rf01_usuario_com_pendencia():
    assert pode_emprestar(usuario_ativo=True, possui_pendencia=True, emprestimos_ativos=0) is False

def test_rf01_fronteira_tres_emprestimos():
    # Este teste vai falhar intencionalmente para revelar o defeito do sistema
    assert pode_emprestar(usuario_ativo=True, possui_pendencia=False, emprestimos_ativos=3) is False

def test_rf02_multa_sem_atraso():
    assert calcular_multa(0) == 0.0
    assert calcular_multa(-1) == 0.0

def test_rf02_multa_atraso_leve_fronteira():
    assert calcular_multa(1) == 2.0
    assert calcular_multa(7) == 14.0

def test_rf02_multa_atraso_excedente():
    assert calcular_multa(8) == 17.0
    assert calcular_multa(10) == 23.0

def test_rf03_classificacao_sem_atraso():
    assert classificar_atraso(0) == "sem atraso"

def test_rf03_classificacao_atraso_leve():
    assert classificar_atraso(1) == "atraso leve"
    assert classificar_atraso(7) == "atraso leve"

def test_rf03_classificacao_atraso_moderado():
    assert classificar_atraso(8) == "atraso moderado"
    assert classificar_atraso(30) == "atraso moderado"

def test_rf03_classificacao_atraso_grave():
    assert classificar_atraso(31) == "atraso grave"