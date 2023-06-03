import psutil
import getpass
import datetime
import platform
import socket

def get_system_data():
    # Total and available RAM
    mem = psutil.virtual_memory()
    total_ram = mem.total
    available_ram = mem.available

    # User name of the PC
    username = getpass.getuser()

    # Storage of the PC
    storage = psutil.disk_usage('/')

    # System time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Platform information
    platform_info = platform.platform()

    # Hostname
    hostname = socket.gethostname()

    # Network addresses
    network_addresses = socket.gethostbyname_ex(hostname)[-1]

    # CPU information
    cpu_info = {
        'brand': platform.processor(),
        'cores': psutil.cpu_count(logical=False),
        'threads': psutil.cpu_count(logical=True)
    }

    # Return the data
    data = {
        'battery_level': f'{psutil.sensors_battery().percent}%',
        'total_ram': total_ram / (1024 ** 3),
        'available_ram': available_ram / (1024 ** 3),
        'username': username,
        'storage': storage.total / (1024 ** 3),
        'current_time': current_time,
        'current_date': current_date,
        'platform_info': platform_info,
        'hostname': hostname,
        'network_addresses': network_addresses,
        'cpu_info': cpu_info
    }

    return data