import unicodedata

def sanitizar(text):
    # convertir a minúsculas
    text = text.lower()

    # eliminar acentos y caracteres especiales
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")

    return text