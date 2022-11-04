import json
import csv
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory():

    @staticmethod
    def import_data(path, type):
        # with open(path, encoding='utf-8') as file:
        if path.endswith('.csv'):
            with open(path, encoding='utf-8') as file:
                resultado = list(
                    csv.DictReader(file, delimiter=',', quotechar='"')
                )
        elif path.endswith('.json'):
            with open(path, encoding='utf-8') as file:
                resultado = json.load(file)
        elif path.endswith('.xml'):
            with open(path, encoding='utf-8') as file:
                resultado = xmltodict.parse(file.read())['dataset']['record']
        if type == 'simples':
            return SimpleReport.generate(resultado)
        else:
            return CompleteReport.generate(resultado)
