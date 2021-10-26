import telnetlib
import json


class MyProbe:
    test_instance = None
    result = {}

    def __init__(self):
        file = open('ip.json')
        self.test_instances = json.load(file)

    def check_input(self):
        config = self.test_instances.get('config0')
        assert config is not None
        target = config.get("Ip address")
        print(target)
        assert target is not None
        port = config.get('port', 23)
        assert port is not None
        return target, port


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


    def parse(self, inputs):
        str_result = str(inputs)
        result_json = {'status': True}
        result_json['data'] = {'Terminale': str_result}
        json_object = json.dumps(result_json, indent=4)
        outfile = open("output.json", 'w')
        outfile.write(json_object)
        outfile.close()

    def rollback(self, inputs=None):
        result = {'ERROR': 'No connection'}
        result_json = {}
        result_json['status'] = False
        result_json['data'] = result
        json_object = json.dumps(result_json, indent=4)
        outfile = open("output.json", 'w')
        outfile.write(json_object)
        outfile.close()




