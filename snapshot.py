from datetime import datetime
import psutil
import json


class Snapshot:
    """Optional class documentation string"""

    def __init__(self, logtype, count):
        self.count = count
        self.timestamp = datetime.now()
        self.type = logtype
        self.vmem = psutil.virtual_memory()
        self.cpuload = psutil.cpu_percent(interval=1)
        self.net_con = psutil.net_connections(kind='inet')
        self.disk_io = psutil.disk_io_counters(perdisk=False)

    def __str__(self):
        if self.type == 'txt':
            cpuload = str(self.cpuload) + '%'
            vmem = str(int(self.vmem.used / 1024 / 1024)) + 'Mb OF ' + \
                str(int(self.vmem.total / 1024 / 1024)) + ' Mb'
            net_con = self.net_con[1].laddr.ip + self.net_con[1].status + \
                ' at ' + str(self.net_con[1].pid) + ' PID'
            disk_io = 'read count of ' + str(self.disk_io.read_count) + \
                ', write count of ' + str(self.disk_io.write_count)

            return 'SNAPSHOT %d : TIMESTAMP : %s\nCPULOAD : %s\nMEMORY USED : %s\n\
            NETWORK CONNECTIONS : %s\nDISK I/O : %s\n\n' \
                % (self.count, self.timestamp, cpuload, vmem, net_con, disk_io)

    def write_to_file(self, filepath, logtype):
        with open(filepath, "a") as outfile:
            if logtype == 'txt':
                outfile.write(str(self))
            elif logtype == 'json':
                data = {}
                data['SNAPSHOT' + str(self.count)] = []

                data['SNAPSHOT' + str(self.count)].append({
                    'TIMESTAMP': str(self.timestamp),
                    'CPULOAD': str(self.cpuload),
                    'MEMORY': [
                        {'total': str(self.vmem.total)},
                        {'used': str(self.vmem.used)},
                        {'buffers': str(self.vmem.buffers)},
                        {'cached': str(self.vmem.cached)}
                    ],
                    'NETWORK CONNECTIONS': {
                        'inet': [
                            {'local_ip': self.net_con[1].laddr.ip},
                            {'status': str(self.net_con[1].status)},
                            {'pid': str(self.net_con[1].pid)}
                        ],
                        'DISK_IO': [
                            {'read_count': str(self.disk_io.read_count)},
                            {'write_count': str(self.disk_io.write_count)},
                        ]
                    }
                })

                json.dump(data, outfile, indent=1)
                outfile.write("\n")
