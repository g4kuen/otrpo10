from prometheus_client import start_http_server, Summary, Gauge
import psutil
import time
import os
from dotenv import load_dotenv

load_dotenv()

EXPORTER_HOST = os.getenv('EXPORTER_HOST')
EXPORTER_PORT = int(os.getenv('EXPORTER_PORT'))


cpu_usage = Gauge('cpu_usage', 'CPU usage in percentage')
total_memory = Gauge('total_memory', 'Total memory in bytes')
used_memory = Gauge('used_memory', 'Used memory in bytes')
total_disk = Gauge('total_disk', 'Total disk space in bytes')
used_disk = Gauge('used_disk', 'Used disk space in bytes')

def collect_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_usage.set(cpu_percent)

    mem_info = psutil.virtual_memory()
    total_memory.set(mem_info.total)
    used_memory.set(mem_info.used)

    disk_info = psutil.disk_usage('/')
    total_disk.set(disk_info.total)
    used_disk.set(disk_info.used)

if __name__ == '__main__':
    start_http_server(EXPORTER_PORT, addr=EXPORTER_HOST)


    while True:
        collect_metrics()
        time.sleep(5)
