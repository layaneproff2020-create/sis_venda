from datetime import datetime

class Movimentacao:
    def __init__(self, descricao: str, data: datetime = None):
        self._descricao = descricao
        self._data = data or datetime.now()

    def formatar(self):
        return f"{self._data.strftime('%d/%m/%y %H:%M')} - {self._descricao}"
