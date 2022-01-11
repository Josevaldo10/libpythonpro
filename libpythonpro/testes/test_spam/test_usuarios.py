from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Josevaldo', email='josevaldopsouza@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Josevaldo', email='josevaldopsouza@hotmail.com'),
                Usuario(nome='Renzo', email='josevaldopsouza@hotmail.com')
                ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()


