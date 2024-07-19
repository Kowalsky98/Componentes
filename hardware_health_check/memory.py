import psutil

def get_memory_info():
    svmem = psutil.virtual_memory()
    memory_info = {
        'total': svmem.total,
        'available': svmem.available,
        'used': svmem.used,
        'percentage': svmem.percent
    }
    return memory_info

def check_memory_health(memory_info):
    memory_usage_threshold = 90  

    if memory_info['percentage'] > memory_usage_threshold:
        return "RAM no está en buen estado"
    return "RAM en optimas condiciones"
