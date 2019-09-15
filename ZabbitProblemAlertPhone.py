import requests,json

class ZabbixProblemAerlter(object):

    def __init__(self):
        self.ZabbixUsername = 'Admin'
        self.ZabbixPassword = 'zabbix'
        self.ZabbixApiUrl = 'http://192.168.128.73/zabbix/api_jsonrpc.php'
        self.ZabbixApiheaders = {'Content-Type': 'application/json'}

    def GetZabbixProblem(self):
        ZabbixGetAuthData = {'jsonrpc': '2.0',
                             'method': 'user.login',
                             'params': {'user': self.ZabbixUsername,
                                        'password': self.ZabbixPassword
                             },
                             "id": 1,
                             "auth": None
                            }
        RequestResult = requests.post(self.ZabbixApiUrl, data=json.dumps(ZabbixGetAuthData), headers=self.ZabbixApiheaders)
        ZabbixApiAuth = json.loads(RequestResult.text)['result']
        ZabbixGetProblemData = {"jsonrpc": "2.0",
                                "method": "problem.get",
                                "params": {"output": "extend"},
                                "auth": ZabbixApiAuth,
                                "id": 1}
        RequestResult = requests.post(self.ZabbixApiUrl, data=json.dumps(ZabbixGetProblemData),
                                      headers=self.ZabbixApiheaders)
        for iterm in json.loads(RequestResult.text)['result']:
            print(iterm)

ZabbixProblemAerlter().GetZabbixProblem()