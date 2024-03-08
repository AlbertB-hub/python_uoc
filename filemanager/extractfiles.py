import tarfile
import zipfile


def extract_zip(path):
    """Extraer zip o tar.gz de la ubicación indicada en el mismo directorio"""

    if path.endswith('.zip'):
        with zipfile.ZipFile(path, 'r') as zip_file:
            zip_file.extractall()
        return 'Zip extraído'
    elif path.endswith('.tar.gz'):
        tarfile.open(path)
        return '.tar extraído'
    else:
        raise ValueError("Formato no soportado")
