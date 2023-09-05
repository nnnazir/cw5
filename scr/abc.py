# Абстрактные классы
from abc import ABC, abstractmethod


class Employer(ABC):
    """Абстрактный класс для работы с API сайтов"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_employers(self):
        pass

    @abstractmethod
    def get_vacancies(self, url_vac):
        pass