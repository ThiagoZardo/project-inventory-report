from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_do_produto='nome produto',
        nome_da_empresa='nome empresa',
        data_de_fabricacao='data fabricação',
        data_de_validade='data validade',
        numero_de_serie='000',
        instrucoes_de_armazenamento='armazenamento',
    )
    assert product.id == 1
    assert product.nome_do_produto == 'nome produto'
    assert product.nome_da_empresa == 'nome empresa'
    assert product.data_de_fabricacao == 'data fabricação'
    assert product.data_de_validade == 'data validade'
    assert product.numero_de_serie == '000'
    assert product.instrucoes_de_armazenamento == 'armazenamento'
