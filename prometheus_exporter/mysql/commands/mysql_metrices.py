
mysql_metrices = [
    {
        'name': 'slave_status',
        'command': "python3 /opt/script/devops_python/prometheus_exporter/mysql/commands/mysql_commands.py --slave-status",
        'desc': 'mysql slave status',
        'type': 'gauge',
        'data_type': 'integer'
    }
]