import datetime
from typing import Counter


class SimpleReport:

    @staticmethod
    def generate(data):
        validade_mais_proxima = []
        fabricacao_mais_antiga = []
        empresa_produtos = []

        for product in data:
            if (
                product['data_de_validade'] >= datetime.date
                .today().isoformat()
            ):
                validade_mais_proxima.append(product['data_de_validade'])

            if (
                product['data_de_fabricacao'] <= datetime.date
                .today().isoformat()
            ):
                fabricacao_mais_antiga.append(product['data_de_fabricacao'])

            empresa_produtos.append(product['nome_da_empresa'])

        empresa_mais_produtos = Counter(empresa_produtos).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {min(fabricacao_mais_antiga)}\n"
            f"Data de validade mais próxima: {min(validade_mais_proxima)}\n"
            f"Empresa com mais produtos: {empresa_mais_produtos}"
        )
