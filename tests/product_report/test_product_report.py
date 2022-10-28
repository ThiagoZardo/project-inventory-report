from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        id=1,
        nome_do_produto='product',
        nome_da_empresa='company',
        data_de_fabricacao='01/01/22',
        data_de_validade='01/01/25',
        numero_de_serie='000',
        instrucoes_de_armazenamento='storage',
    )
    assert product.__repr__() == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
