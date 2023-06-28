import csv
import time

from pep_parse.settings import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.data = {}

    def process_item(self, item, spider):
        if item['status'] not in self.data:
            self.data[item['status']] = 0
        self.data[item['status']] += 1
        return item

    def close_spider(self, spider):
        pep_date = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        total_amount = 0
        with open(f'{BASE_DIR}/results/status_summary_{pep_date}.csv',
                  'w',
                  newline='',
                  encoding='utf-8') as csvfile:
            fieldnames = ['Статус', 'Количество']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for status, amount in self.data.items():
                writer.writerow({'Статус': status, 'Количество': amount})
                total_amount += amount
            writer.writerow({'Статус': 'Total', 'Количество': total_amount})
