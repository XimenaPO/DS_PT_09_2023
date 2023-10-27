"""Comprueba el entorno para seguir el texto."""

from distutils.version import LooseVersion as Version
import importlib
import sys
import re
import os

# Obtiene la ruta absoluta del script en ejecución
script_dir = os.path.dirname(os.path.abspath(__file__))

# Cambia el directorio de trabajo al directorio del script
os.chdir(script_dir)


OK = '\x1b[42m[ OK ]\x1b[0m'
FAIL = '\x1b[41m[FAIL]\x1b[0m'

github_package_pattern = re.compile(r'(?:\/)([\w*\-*]*)(?:\.git)')

def run_checks(raise_exc=False):
    """
    Comprueba que los paquetes que necesitamos están instalados y que la versión de Python es buena.

    Parámetros
    ----------
    raise_exc : bool, por defecto ``False``
        Si se lanza una excepción si alguno de los paquetes no
        no cumple los requisitos (usado para GitHub Action).
    """
    failures = []

    # comprobar la versión de python
    print('Uso de Python en %s:' % sys.prefix)
    if Version(sys.version) >= '3.7.4' and Version(sys.version) < '3.12.1':
        print(OK, 'Python es la versión %s\n' % sys.version)
    else:
        print(FAIL, 'Se requiere una versión de Python >= 3.7.4 y < 3.12.1, pero %s está instalado.\n' % sys.version)
        failures.append('Python')

    # leer los requisitos
    with open(r'..\requirements.txt', 'r') as file:
        requirements = {}
        for line in file.read().splitlines():
            github_package = re.search(github_package_pattern, line)
            if github_package:
                pkg = github_package.group(1).replace('-', '_')
                version = None
            else:
                if line.startswith('./'):
                    line = line.replace('./', '')
                try:
                    if '>=' in line:
                        pkg, versions = line.split('>=')
                        version = versions.split(',<=')
                    else:
                        pkg, version = line.split('==')
                except ValueError:
                    pkg, version = line, None
                if pkg == 'imbalanced-learn':
                    pkg = 'imblearn'
                elif pkg == 'scikit-learn':
                    pkg = 'sklearn'
                elif pkg == 'python-dotenv':
                    pkg = 'dotenv'

            requirements[pkg.replace('-', '_')] = version

    # compruebe los requisitos
    for pkg, req_version in requirements.items():
        try:
            mod = importlib.import_module(pkg)
            if req_version:
                version = mod.__version__
                if isinstance(req_version, list):
                    min_version, max_version = req_version
                    if Version(version) < min_version or Version(version) > max_version:
                        print(FAIL, '%s se requiere una versión >= %s y <= %s, pero está instalada %s.' % (pkg, min_version, max_version, version))
                        failures.append(pkg)
                        continue
                else:
                    if Version(version) != req_version:
                        print(FAIL, '%s se requiere la versión %s, pero %s está instalada.' % (pkg, req_version, version))
                        failures.append(pkg)
                        continue
            print(OK, '%s' % pkg)
        except ImportError:
            print(FAIL, '%s no instalado.' % pkg)
            failures.append(pkg)

    if failures and raise_exc:
        raise Exception(
            'El entorno no ha superado la inspección debido a versiones incorrectas '
            f'de {len(failures)} item(s): {", ".join(failures)}.'
        )

if __name__ == '__main__':
    run_checks(raise_exc=True)
