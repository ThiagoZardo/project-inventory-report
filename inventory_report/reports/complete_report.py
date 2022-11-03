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

        empresa_mais_produtos = Counter(empresa_produtos).most_common()
        string_response = ''
        for empresa in empresa_mais_produtos:
            string_response += f"- {empresa[0]}: {empresa[1]}\n"

        return (
            f"{SimpleReport.generate(data)}\n"
            f"Produtos estocados por empresa:\n"
            f"{string_response}"
        )
