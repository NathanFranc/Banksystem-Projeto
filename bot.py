from botcity.core import *
from datetime import datetime
from botcity.plugins.excel import *

class Bot:
    def bot(self):
        # Sequence: Bank system

        # Read Excel Activity
        # Displayname: Read_Excel
        excelBot = BotExcelPlugin()
        file_or_path = "C:\\Users\\JEFFERSON LIMA\\Documents\\Bank\\BankSystem\\extract.xlsx"

        list = excelBot.read(file_or_path=file_or_path).as_list(sheet="extrato")[1:]
        # Open Application Activity
        # Displayname: OpenApplication
        executablePath = "C:\\Users\\JEFFERSON LIMA\\Documents\\Bank\\BankSystem\\BankSystem.exe"
        deskBot = DesktopBot()
        deskBot.execute(executablePath)
        deskBot.connect_to_app(backend=Backend.UIA, timeout=60000, path=executablePath)
        popup_Window = deskBot.find_app_window(waiting_time=10000)

        # Sequence: Mapear elementos

        # Find App Element Activity
        # Displayname: Find_App_Element
        btDebito = deskBot.find_app_element(from_parent_window=popup_Window, waiting_time=10000, auto_id="rbDebito",)

        # Find App Element Activity
        # Displayname: Find_App_Element
        btCredito = deskBot.find_app_element(from_parent_window=popup_Window, waiting_time=10000, auto_id="rbCredito",)

        # Find App Element Activity
        # Displayname: Find_App_Element
        txtDescricao = deskBot.find_app_element(from_parent_window=popup_Window, waiting_time=10000, auto_id="txtDescricao",)

        # Find App Element Activity
        # Displayname: Find_App_Element
        txtValor = deskBot.find_app_element(from_parent_window=popup_Window, waiting_time=10000, auto_id="txtValor",)

        # Find App Element Activity
        # Displayname: Find_App_Element
        TextData = deskBot.find_app_element(from_parent_window=popup_Window, waiting_time=10000, auto_id="PART_TextBox",)

        # Find App Element Activity
        # Displayname: Find_App_Element
        btnConfirmar = deskBot.find_app_element(from_parent_window=popup_Window, waiting_time=10000, title="Confirmar",auto_id="btnConfirmar",)

        # ForEach Activity
        # Displayname: ForEach
        for linha in list:
            # Sequence: Entrada de Dados

            # Sequence: Verifica se é debito ou credito

            # If Activity
            # Displayname: If Condition
            if linha[0] == "Débito":
                # Sequence: Body

                # Click Activity
                # Displayname: Click
                btDebito.click()


            # Else Activity
            # Displayname: Else
            else:
                # Sequence: Body

                # Click Activity
                # Displayname: Click
                btCredito.click()


            # Type Into Activity
            # Displayname: Type_Into
            txtDescricao.type_keys(keys=linha[1], with_spaces=True)

            # Type Into Activity
            # Displayname: Type_Into
            txtValor.type_keys(keys=linha[2], with_spaces=True)

            # Type Into Activity
            # Displayname: Type_Into
            TextData.type_keys(keys=linha[3], with_spaces=True)

            # Click Activity
            # Displayname: Click
            btnConfirmar.click()


        # Wait Activity
        # Displayname: Wait
        deskBot.wait(5000)


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()