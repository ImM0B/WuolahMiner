# WuolahMiner

Este es un script Python que automatiza el proceso de creación de cuentas en Wuolah utilizando cuentas de correo desechables. El script utiliza Selenium y Requests para realizar las siguientes tareas:

- Crea una cuenta de correo desechable en `mail.tm`.
- Extrae el token de autenticación para la cuenta de correo creada.
- Utiliza el token para crear una cuenta en Wuolah usando un enlace de invitación proporcionado.
- Verifica la cuenta de Wuolah a través de un enlace de verificación enviado por correo.
- Acumula WuolahCoins por cada cuenta creada y verificada con tu link de invitación.

## Requisitos

- Python 3.x
- Módulos Python: `requests`, `selenium`, `colorama`, `beautifulsoup4`
- [WebDriver de Selenium compatible con Firefox (geckodriver)](https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html)
Personalmente yo uso la versión 115.6.0esr de firefox con la versión 0.34.0 de geckodriver.

## Uso

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tunombre/WuolahMiner.git
   cd WuolahMiner
   ```

2. Instala las dependencias necesarias:

   ```bash
   pip install bs4 colorama selenium requests
   ```

3. Configura las variables necesarias en el script `wuolah_miner.py`:

   - `invite_link`: Enlace de invitación de tu cuenta de Wuolah.
   - `options.binary_location`: Ruta al binario de firefox | `Ejemplo Windows` : C:\Program Files\Mozilla Firefox\firefox.exe ; `Ejemplo Linux`: /usr/bin/firefox
   - `driver_path`: Ruta al WebDriver de Selenium para Firefox. | `Ejemplo Windows` : C:\Users\m0b\geckodriver.exe ; `Ejemplo Linux`: /home/m0b/geckodriver
   - `userID`: Nombre base para las cuentas de correo desechables. Importante cambiarlo.
   
4. Ejecuta el script:

   ```bash
   python wuolah_miner.py
   ```

## Notas

- Este script está diseñado con propósitos educativos y de prueba. Úsalo bajo tu propio riesgo.

---

*README creado por ChatGPT.*
