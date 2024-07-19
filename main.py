from hardware_health_check.cpu import get_cpu_info, check_cpu_health
from hardware_health_check.memory import get_memory_info, check_memory_health
from hardware_health_check.smart import get_smart_status, check_smart_health

def main():
    
    cpu_info = get_cpu_info()
    print("Estado del CPU:", check_cpu_health(cpu_info))

    memory_info = get_memory_info()
    print("Estado de la RAM:", check_memory_health(memory_info))

    smart_status = get_smart_status()
    print("Estado SMART del Disco Duro:", check_smart_health(smart_status))

if __name__ == '__main__':
    main()
