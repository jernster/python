import os.path

def get_logs():
    result = [name for name in os.listdir(os.getcwd())
        if os.path.isfile(os.path.join(os.getcwd(), name))]
    return result