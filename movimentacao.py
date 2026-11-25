from datetime import date, datetime

class Movimento :

  def__init__(self,descricao:str,data:datetime=.now()):
  self._descricao = descricao
  self._data = date # type: ignore

  def formatar(self):
     return f"{self._data.strtime('%d/%m/%y %H:%M')} - {self._descricao}"