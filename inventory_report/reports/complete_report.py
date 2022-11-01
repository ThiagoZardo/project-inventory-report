import datetime
from typing import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

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

        empresa_mais_produtos = Counter(empresa_produtos).most_common(3)

        return (
            f"Data de fabricação mais antiga: {min(fabricacao_mais_antiga)}\n"
            f"Data de validade mais próxima: {min(validade_mais_proxima)}\n"
            f"Empresa com mais produtos: {empresa_mais_produtos[0][0]}\n"
            f"Produtos estocados por empresa:\n"
            f"- {empresa_mais_produtos[0][0]}: {empresa_mais_produtos[0][1]}\n"
            f"- {empresa_mais_produtos[1][0]}: {empresa_mais_produtos[1][1]}\n"
            f"- {empresa_mais_produtos[2][0]}: {empresa_mais_produtos[2][1]}\n"
        )
