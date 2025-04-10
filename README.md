# Health Monitoring System

A real-time health monitoring system that visualizes vital signs data from multiple sensors.

## Features

- Real-time health data visualization from:
  - MAX30102 (Heart Rate and SpO2)
  - AD8232 (ECG)
  - CJMCU-6701 GSR (Stress Level)
- Web-based dashboard with real-time visualization
- WebSocket-based data streaming
- REST API endpoints for data access
- Environment-based configuration
- Error handling and logging
- Optional sensor data simulation for testing

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for version control)
- Raspberry Pi Pico W (for real sensor data)

## Setup

1. Clone the repository (if using Git):
```bash
git clone <repository-url>
cd health-monitoring-system
```

2. Create a virtual environment:
```bash
# On Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate.bat

# On Windows (PowerShell)
python -m venv venv
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1

# On Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your settings
# Use any text editor to modify the values
```

5. Run the application:

For real sensor data (default):
```bash
python app.py
```

For simulated data:
```bash
python app.py --simulate
```

6. Open your browser and navigate to:
```
http://localhost:5000
```

## API Endpoints

- `GET /api/vitals`: Get the latest health data
- `GET /api/vitals/history`: Get historical health data (placeholder)

## Project Structure

```
health-monitoring-system/
├── app.py                 # Main Flask application
├── config.py             # Configuration management
├── sensor_simulator.py   # Sensor data simulation
├── health_monitor.py     # Real sensor data collection
├── requirements.txt      # Python dependencies
├── .env.example         # Example environment variables
├── .env                 # Your environment variables (create this)
└── templates/
    └── index.html       # Web dashboard
```

## Hardware Setup (for real sensors)

The system is designed to work with the following sensors:

- MAX30102 (I²C):
  - SCL: GP17
  - SDA: GP16
  - Address: 0x57

- AD8232 (Analog):
  - Connected to ADC0/GP26

- CJMCU-6701 GSR (Analog):
  - Connected to ADC1/GP27

All sensors are powered via 3.3V and GND.

## Development

### Modifying Simulation Parameters

When using simulated data, you can modify the parameters in `.env`:
```python
# Example: Modify base values in .env
BASE_BPM=80
BASE_SPO2=99
BASE_GSR=1.2
```

### Customizing the Dashboard

The dashboard is built with:
- Bootstrap 5 for layout
- Plotly.js for charts
- Socket.IO for real-time updates

Modify `templates/index.html` to customize the UI.

### Adding New Features

1. Add new routes in `app.py`
2. Create new simulation methods in `sensor_simulator.py`
3. Update the dashboard in `templates/index.html`

## Troubleshooting

### Virtual Environment Issues

If you encounter permission issues with PowerShell:
1. Open PowerShell as Administrator
2. Run: `Set-ExecutionPolicy RemoteSigned`
3. Type 'Y' to confirm

### Connection Issues

1. Check if the Flask server is running
2. Verify your `.env` configuration
3. Check browser console for WebSocket errors
4. Make sure you're using `localhost:5000` or `127.0.0.1:5000` in your browser

### Sensor Issues

1. For real sensors:
   - Check physical connections
   - Verify sensor power supply
   - Check I2C/ADC connections
   - Review sensor logs

2. For simulated data:
   - Verify environment variables are loaded correctly
   - Check the console for error messages
   - Adjust simulation parameters in `.env`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 