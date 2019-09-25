import os, argparse, sys,subprocess
sys.path.append('/opt/script/devops_python')
from prometheus_client import start_http_server, REGISTRY
from prometheus_client.core import GaugeMetricFamily


EXPORTER_PORT = 9007

class AsteriskExporter():

    def RunCommand(self, SystemCommand):
        SubprocessObject = subprocess.Popen(SystemCommand, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        try:
            SubprocessObject.wait(3)
        except subprocess.TimeoutExpired as Error:
            SubprocessObject.kill()
            return False, Error
        else:
            RunCommandOut = SubprocessObject.communicate()

            return RunCommandOut

    def GetAsteriskChannel(self):
        RunCommandResult = self.RunCommand(
            "/usr/sbin/asterisk -rx'core show channels' |grep -E 'active channels|active calls'"
        )
        AsteriskChannel = {}
        for iterm in bytes.decode(RunCommandResult[0]).split('\n'):
            if 'active channels' in iterm:
                AsteriskChannel['ActiveChannels'] = iterm.split(' ')[0]
            elif 'active calls' in iterm:
                AsteriskChannel['ActiveCalls'] = iterm.split(' ')[0]
        return AsteriskChannel

    def collect(self):
        AsteriskResult = self.GetAsteriskChannel()
        yield GaugeMetricFamily('Active_Channels', 'Active_Channels', value=AsteriskResult['ActiveChannels'])
        yield GaugeMetricFamily('Active_Calls', 'Active_Calls', value=AsteriskResult['ActiveCalls'])



if __name__ == '__main__':
    try:
        start_http_server(EXPORTER_PORT)

        REGISTRY.register(AsteriskExporter())

        obj = AsteriskExporter()

        while True:
            obj.collect()
    except Exception as err:
        print(err)
    # def AsteriskMetrices(self):
    #     metric = Metric(Asterisk_Metrices[0]['name'], Asterisk_Metrices[0]['desc'], Asterisk_Metrices[0]['type'])