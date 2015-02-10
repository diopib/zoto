__author__ = 'ibrahim'

SERVICE_CODE_1 = 786
SERVICE_CODE_2 = 313
SERVICE_CODE_3 = 7007

def BaseServiceClass():
    def __init__(*args, **kwargs):
        pass

def ServiceClass1(BaseServiceClass):
    def process():
        pass

def ServiceClass2(BaseServiceClass):
    def process():
        pass

def ServiceClass3(BaseServiceClass):
    def process():
        pass

def route(*args, **kwargs):
    route_dict = {SERVICE_CODE_1: ServiceClass1, SERVICE_CODE_2: ServiceClass2, SERVICE_CODE_3: ServiceClass3}
    # return class corresponding to parameters

def receive_command(*args, **kwargs):
    service = route(*args, **kwargs)
    service.process()