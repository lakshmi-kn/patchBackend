import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Flask server configuration
# Flask server config
FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')
FLASK_PORT = int(os.getenv('FLASK_PORT', '5000'))
FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

# Sensor configuration
MAX_SAMPLES = int(os.getenv('MAX_SAMPLES', '100'))
SAMPLE_INTERVAL = float(os.getenv('SAMPLE_INTERVAL', '5'))
SIMULATION_INTERVAL = float(os.getenv('SIMULATION_INTERVAL', '5'))

# Hardware addresses & pins
MAX30102_ADDR = int(os.getenv('MAX30102_ADDR', '0x57'), 16)
AD8232_PIN = int(os.getenv('AD8232_PIN', '26'))  # ECG → GP26
GSR_PIN = int(os.getenv('GSR_PIN', '27'))        # GSR → GP27
I2C_SCL_PIN = int(os.getenv('I2C_SCL_PIN', '5')) # MAX30102 SCL → GP5
I2C_SDA_PIN = int(os.getenv('I2C_SDA_PIN', '4')) # MAX30102 SDA → GP4

# Simulation parameters
BASE_BPM = float(os.getenv('BASE_BPM', '75'))
BASE_SPO2 = float(os.getenv('BASE_SPO2', '98'))
BASE_ECG_MV = float(os.getenv('BASE_ECG_MV', '0.0'))
BASE_GSR_V = float(os.getenv('BASE_GSR_V', '1.5'))

# Database configuration (for future use)
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///health_data.db')