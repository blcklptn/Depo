from db import db
from models.pydantic_models import Transport, Employees, Schedule
from sqlalchemy.exc import NoResultFound
from core import config
from typing import Union
import logging
from misc import create_xlsx

session = db.create_database()


class ManageEmployees:
    def add_employeer(self, emp: Employees) -> None:
        try:
            session.add(emp)
            session.commit()
        except Exception as ex:
            logging.error(f'Какие-то данные пользователя введены неверно: {ex}')

    def remove_employeer(self, emp_id: str) -> None:
        try:
            query: str = session.query(Employees).filter(Employees.id == emp_id).one()
            session.delete(query)
            session.commit()

        except NoResultFound:
            logging.error('Не удалось найти пользователя...')
        except Exception as ex:
            logging.error(f'Неудача в удалении пользователя: {ex}')

    def update_employeer(self, emp_id: str, emp: Employees) -> None:
        try:
            upd_dict = emp.dict()
            session.query(Employees).filter(Employees.id == emp_id).update(upd_dict)
            session.commit()
        except NoResultFound:
            logging.error('Не удалось найти пользователя...')
        except Exception as ex:
            logging.error(f'Неудача в обновлении пользователя: {ex}')
        
    def get_emp_by_id(self, emp_id: str) -> Union[Employees, None]:
        try:
            employer = session.query(Employees).filter(Employees.id == emp_id).one()
            return employer
        except NoResultFound:
            logging.error('Не удалось найти пользователя...')
        except Exception as ex:
            logging.error(f'Неудача в получении пользователя: {ex}')


class ManageTransport:
    def add_transport(self, tr: Transport) -> None:
        try:
            session.add(tr)
            session.commit()
        except Exception as ex:
            logging.error('Какие-то данные введены неверно: {ex}')

    def remove_transport(self, tr_id: str) -> None:
        try:
            query: str = session.query(Transport).filter(Transport.id == tr_id).one()
            session.delete(query)
            session.commit()

        except NoResultFound:
            logging.error('Не удалось найти транспорт...')
        except Exception as ex:
            logging.error(f'Неудача в удалении транспорта: {ex}')

    def update_transport(self, tr_id: str, tr: Transport) -> None:
        try:
            upd_dict = tr.dict()
            session.query(Transport).filter(Transport.id == tr_id).update(upd_dict)
            session.commit()
        except NoResultFound:
            logging.error('Не удалось найти транспорт...')
        except Exception as ex:
            logging.error(f'Неудача в обновлении транспорта: {ex}')

    def get_tr_by_id(self, tr_id: str) -> Union[Transport, None]:
        try:
            employer = session.query(Employees).filter(Employees.id == tr_id).one()
            return employer
        except NoResultFound:
            logging.error('Не удалось найти транспорт...')
        except Exception as ex:
            logging.error(f'Неудача в получении транспорта: {ex}')


class ManageSchedule:
    def add_row(self, sch: Schedule) -> None:
        try:
            session.add(sch)
            session.commit()
        except Exception as ex:
            logging.error(f'Какие-то данные введены неверно: {ex}', )
    
    def remove_row(self, sch_id: str) -> None:
        try:
            query: str = session.query(Schedule).filter(Schedule.id == sch_id).one()
            session.delete(query)
            session.commit()

        except NoResultFound:
            logging.error('Не удалось найти расписание...')
        except Exception as ex:
            logging.error(f'Неудача в удалении расписания:', ex)

    def get_sch_by_id(self, sch_id: str) -> Union[Schedule, None]:
        try:
            schedule = session.query(Schedule).filter(Schedule.id == sch_id).one()
            return schedule
        except NoResultFound:
            logging.error('Не удалось найти расписание...')
        except Exception as ex:
            logging.error(f'Неудача в получении расписания: {ex}')


class Manage(ManageEmployees, ManageTransport, ManageSchedule):
    def __init__(self) -> None:
        super().__init__()

    
    def __str__(self) -> str:
        return 'Класс объединяет все другие объекты Manage в один'


    def drop_schedule(self):
        record = session.query(Schedule).all()
        create_xlsx.CreateTable().start(record)
        
        """
        try:
            session.query(Schedule).delete()
            session.commit()
        except Exception as ex:
            logging.error(f'Неудача в удалении расписания: {ex}')
        """
        