import os

class MissingEnvVar(Exception):
    pass

def check_env(variable_name):
    if not os.getenv(variable_name, None):
        raise MissingEnvVar(f"{variable_name} environment variable not set!")
    return os.getenv(variable_name)

