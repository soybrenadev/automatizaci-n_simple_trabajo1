from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from funciones_agentes.obtener_clima import obtener_clima
from funciones_agentes.obtener_precio_accion import obtener_precio_accion
from utils.sanitizar import sanitizar


# Configuración de Selenium
options = Options()
#options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0")
options.add_argument("--disable-blink-features=AutomationControlled")


# Inicializar navegador
service = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        return obtener_precio_accion
    return None


print("Hola, soy tu asistente virtual 🤖")
print("Puedes preguntarme por el clima o el precio de acciones.")
print("Escribe 'salir' para terminar.\n")


while True:

    user_input = sanitizar(input("---> "))

    if user_input in ["salir", "exit", "quit", "adios"]:
        print("Hasta luego 👋")
        break

    funcion_agente = procesar_input(user_input)

    if funcion_agente is None:
        print("No entendí tu solicitud. Intenta nuevamente.")
    else:
        respuesta = funcion_agente(driver, user_input)
        print(f">>> {respuesta}")


driver.quit()