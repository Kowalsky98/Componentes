import subprocess

def get_smart_status():
    try:
        result = subprocess.run(['wmic', 'diskdrive', 'get', 'status'], stdout=subprocess.PIPE)
        smart_status = result.stdout.decode().strip().split("\n")[1:]
        return smart_status
    except IndexError:
        return "Información SMART no disponible"

def check_smart_health(smart_status):
    if any(status.strip() != "OK" for status in smart_status):
        return "Estado SMART del disco no está en buen estado"
    return "Discos en optimas condiciones"
