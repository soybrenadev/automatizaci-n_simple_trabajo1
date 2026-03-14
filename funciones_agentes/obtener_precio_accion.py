from selenium.webdriver.common.by import By
import time

def obtener_precio_accion(driver, consulta):

    # quitar palabras innecesarias
    consulta = consulta.replace("precio", "").replace("accion", "").replace("de", "").strip()

    driver.get(f"https://www.google.com/search?q=precio+accion+{consulta}")

    time.sleep(3)

    try:
        precio = driver.find_element(By.CSS_SELECTOR, "span[jsname='vWLAgc']").text
        empresa = driver.find_element(By.CSS_SELECTOR, "div[data-attrid='title']").text

        return f"{empresa}: ${precio}"

    except Exception:
        return "No se pudo obtener el precio de la acción en este momento."