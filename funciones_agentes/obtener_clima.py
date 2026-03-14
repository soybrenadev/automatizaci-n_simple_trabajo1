from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def obtener_clima(driver, consulta):

    ciudad = consulta.replace("clima", "").replace("temperatura", "").replace("en", "").strip()

    if ciudad == "":
        ciudad = "mexico"

    driver.get(f"https://www.google.com/search?q=clima+{ciudad}")

    try:
        wait = WebDriverWait(driver, 10)

        # temperatura
        temperatura = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.iLUpNd.nB7Pqb.aSRlid")
            )
        ).text

        # ciudad
        ciudad_nombre = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "span.iLUpNd.d6Ejqe.aSRlid")
            )
        ).text

        return f"La temperatura en {ciudad_nombre} es {temperatura}"

    except Exception:
        return "No se pudo obtener el clima en este momento."