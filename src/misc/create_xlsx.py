import xlsxwriter
from datetime import datetime

class CreateTable:
    def __init__(self):
        self.row = 1
        self.col = 0

    def __date(self) -> str:
        return str(datetime.today().strftime('%Y-%m-%d'))

    def __init(self):
        self.workbook = xlsxwriter.Workbook(f'schedule_logs/{self.__date()}.xlsx')
        self.worksheet = self.workbook.add_worksheet()
    
    def __create_headers(self):
        headers = ['id', 'transport_id',
                   'before_luch_1_emp_fio', 'before_luch_2_emp_fio',
                   'after_luch_1_emp_fio','after_luch_1_emp_fio', 'added']

        col = 0
        for i in headers:
            self.worksheet.write(0, col, i)
            col += 1        
    
    def write_record(self):
        for i in self.record:
            self.worksheet.write(self.row, self.col, i.id)
            self.worksheet.write(self.row, self.col + 1, i.transport_id)
            self.worksheet.write(self.row, self.col + 2, i.before_lunch_1_emp_id)
            self.worksheet.write(self.row, self.col + 3, i.before_lunch_2_emp_id)

            self.worksheet.write(self.row, self.col + 4, i.after_lunch_1_emp_id)
            self.worksheet.write(self.row, self.col + 5, i.after_lunch_2_emp_id)
            self.worksheet.write(self.row, self.col + 6, str(i.added))
            self.row += 1
        

    def start(self, record: list):
        self.record = record
        self.__init()
        self.write_record()
        self.__create_headers()
       
        self.__save()

    def __save(self):
        self.workbook.close()
