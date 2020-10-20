import  configparser

def get_config():
    config = configparser.ConfigParser()
    config.read(r'C:\Users\VENKAT\PycharmProjects\pythonJIRA\properties\properties.ini')
    return config
