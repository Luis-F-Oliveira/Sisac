from app.config.python.selenium import Coplan
from app.controller.xlsxtojson import XlsxToJson
from app.view.warning.warning import WarningException
from time import sleep
import json

class Fcommit:
    def __init__(self, xlsx, user, passw):
        self.xlsx = xlsx
        self.user = user
        self.password = passw

    def Commit(self):
        try:
            XlsxToJson.Folha(self.xlsx, 'app/config/json/folha.json')

            with open('app/config/json/folha.json') as file:
                self.dados = json.load(file)

            fp = Coplan(self.user, self.password)
            fp.Open()

            fp.Mouse('//*[@id="myMenuID"]/table/tbody/tr/td[4]')
            fp.Mouse('//*[@id="cmSubMenuID14Table"]/tbody/tr[3]/td[2]')
            fp.Click('//*[@id="cmSubMenuID15Table"]/tbody/tr[1]/td[2]')


            fp.Click('//*[@id="vLANCAMENTOS_0001"]')

            for item in self.dados:
                defensor_atual = item["DEFENSOR"]

                if item['ACUMULO MESES ANTERIORES - 1058'] not in ["sem info", 0]:
                    local = '1058'
                if item['DESCONTO SEM ACUMULAÇÃO ATUAL - 1045'] not in ["sem info", 0]:
                    local = '1045'
                if item['TOTAL A PAGAR - 1056'] not in ["sem info", 0]:
                    local = '1056'
        
        except Exception as e:
            WarningException(e, defensor_atual, local)

        finally:
            fp.Close()