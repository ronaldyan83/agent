# piccola prova di probe che semplicemente prendi i dati da un json dove sono memorizzati ip e porta per test connessione telnet
import telnetlib
import json


class MyProbe:
    test_instance = None
    result = {}

    def __init__(self):
        # file che contiene dati di input della sonda
        file = open('ip.json')
        self.test_instances = json.load(file)

    # verifica dei dati di input
    def check_input(self):
        config = self.test_instances.get('config0')
        assert config is not None
        target = config.get("Ip address")
        print(target)
        assert target is not None
        port = config.get('port', 23)
        assert port is not None
        return target, port
    #metodo per l'esecuzione del telnet allo switch
    def execute(self, inputs):
        switch = inputs[0]
        port = inputs[1]
        try:
            t = telnetlib.Telnet(switch, port, timeout=10)
        except:
            self.rollback()
            exit()
        result = t.read_until(b":", timeout=5)
        return result
    #per settare il file di output con i risultati che non sono altro che la stringa della console dello switch
    def parse(self, inputs):
        str_result = str(inputs)
        result_json = {'status': True}
        result_json['data'] = {'Terminale': str_result}
        json_object = json.dumps(result_json, indent=4)
        outfile = open("output.json", 'w')
        outfile.write(json_object)
        outfile.close()
    #metodo in caso di errore nella connessione allo switche per timeout
    def rollback(self, inputs=None):
        result = {'ERROR': 'No connection'}
        result_json = {}
        result_json['status'] = False
        result_json['data'] = result
        json_object = json.dumps(result_json, indent=4)
        outfile = open("output.json", 'w')
        outfile.write(json_object)
        outfile.close()
