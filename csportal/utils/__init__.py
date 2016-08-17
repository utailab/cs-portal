import os

from django.core.exceptions import ImproperlyConfigured


def get_env_var(var):
    try:
        return os.environ[var]
    except KeyError:
        raise ImproperlyConfigured('set the environment variable {}'.format(var))
