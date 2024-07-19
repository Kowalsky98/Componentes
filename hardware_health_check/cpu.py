import psutil

def get_cpu_info():
    cpu_info = {
        'physical_cores': psutil.cpu_count(logical=False),
        'total_cores': psutil.cpu_count(logical=True),
        'max_frequency': psutil.cpu_freq().max,
        'current_frequency': psutil.cpu_freq().current,
        'cpu_usage': psutil.cpu_percent(interval=1)
    }
    return cpu_info

def check_cpu_health(cpu_info):
    cpu_usage_threshold = 90 
    min_frequency_ratio = 0.5  

    if cpu_info['cpu_usage'] > cpu_usage_threshold:
        return "CPU no está en buen estado"
    if cpu_info['current_frequency'] < min_frequency_ratio * cpu_info['max_frequency']:
        return "CPU no está en buen estado"
    return "CPU en optimas condiciones"