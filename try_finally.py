import zipfile

banco_zip = None

try:
    banco_zip = zipfile.ZipFile("Saida.zip")
    banco_zip.extractall(path="banco")
except PermissionError:
    print("aaaaa")
else:
    banco_zip.close()
