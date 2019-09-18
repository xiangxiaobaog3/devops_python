from prometheus_client import start_http_server, Metric, Gauge, REGISTRY
from prometheus_exporter.mysql.commands import mysql_metrices
import os, argparse, sys
sys.path.append('/opt/script/devops_python')

EXPORTER_PORT = 9006
SERVICE_PORT = 3306

class MySQLExporter():
    def collect(self):
        try:
            for metrics in mysql_metrices.mysql_metrices:
                command = os.system(metrics['command'])
                metric = Metric(metrics['name'], metrics['desc'], metrics['type'])
                if metrics['data_type'] == 'integer':
                    metric.add_sample(metrics['name'], value=int(command), labels= {})
                yield metric
        except Exception as err:
            print(err)


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description = 'MySQL Exporter Arguments')
        parser.add_argument('-s','--service-port', type = int, default = SERVICE_PORT)
        parser.add_argument('-e','--exporter-port', type = int, default = EXPORTER_PORT)
        args = parser.parse_args()

        SERVICE_PORT = args.service_port
        EXPORTER_PORT = args.exporter_port

        start_http_server(EXPORTER_PORT)

        REGISTRY.register(MySQLExporter())

        obj = MySQLExporter()

        while True:
            obj.collect()
    except Exception as err:
        print(err)
