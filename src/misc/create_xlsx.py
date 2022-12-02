import xlsxwriter
from datetime import datetime

class CreateTable:
    def __init__(self):
        self.record = None
        self.row = 1
        self.col = 0

    def __date(self) -> str:
        return str(datetime.today().strftime('%Y-%m-%d'))

    def __init(self):
        self.workbook = xlsxwriter.Workbook(f'{self.__date()}.xlsx')
        self.worksheet = self.workbook.add_worksheet()
    
    def __create_headers(self):
        headers = ['id', 'transport_id',
                   'before_luch_1_emp_fio', 'before_luch_2_emp_fio',
                   'after_luch_1_emp_fio','after_luch_1_emp_fio', 'added']

        col = 0
        for i in headers:
            self.worksheet.write(0, col, i)
            col += 1        
    
    def __write_record(self):
        for i in self.record:
            self.worksheet.write(self.row, self.col, i.id)
            self.worksheet.write(self.row, self.col + 1, i.transport_id)
            self.worksheet.write(self.row, self.col + 2, i.before_luch_1_emp_fio)
            self.worksheet.write(self.row, self.col + 3, i.before_luch_2_emp_fio)

            self.worksheet.write(self.row, self.col + 4, i.after_luch_1_emp_fio)
            self.worksheet.write(self.row, self.col + 5, i.after_luch_2_emp_fio)
            self.worksheet.write(self.row, self.col + 6, i.added)
            self.row += 1

    def start(self, record: list):
        self.record = record
        self.__init()
        self.__create_headers()
        self.__write_record()
        self.__save()

    def __save(self):
        self.workbook.close()
