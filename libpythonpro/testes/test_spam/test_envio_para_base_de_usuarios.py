from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
      [
        Usuario(nome='Josevaldo', email='josevaldopsouza@hotmail.com'),
        Usuario(nome='Renzo', email='renzo@python,pro.br')
       ],
       [
        Usuario(nome='Josevaldo', email='josevaldopsouza@hotmail.com')
       ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam= EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'josevaldopsouza@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_paramentros_de_spam(sessao):
    usuario = Usuario(nome='Josevaldo', email='josevaldopsouza@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam= EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with (
        'renzo@python.pro.br',
        'josevaldopsouza@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )