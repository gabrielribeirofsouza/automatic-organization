import win32serviceutil
import win32service
import win32event
import servicemanager
import threading

import organizador


class OrganizadorService(win32serviceutil.ServiceFramework):
    _svc_name_ = "OrganizadorArquivos"
    _svc_display_name_ = "Organizador Automático de Arquivos"
    _svc_description_ = "Organiza arquivos automaticamente em background."

    def __init__(self, args):
        super().__init__(args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.thread = None
        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        servicemanager.LogInfoMsg("Serviço iniciando...")
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)

    # informa ao Windows que o serviço está rodando
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)

        servicemanager.LogInfoMsg("Serviço em execução")

    # roda o monitoramento em background
        self.thread = threading.Thread(
        target=organizador.start_monitor,
        daemon=True
    )
        self.thread.start()

    # mantém o serviço vivo
        win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)

        

if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(OrganizadorService)