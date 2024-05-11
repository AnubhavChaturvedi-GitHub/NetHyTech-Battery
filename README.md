
# NetHyTech-Battery

NetHyTech-Battery is a Python package that provides functionalities for monitoring battery status and generating alerts based on battery percentage and power plug status.

## Installation

You can install the package using pip:

```bash
pip install NetHyTech-Battery
```

## Usage

### Importing the Package

```python
import NetHyTech_Battery
```

### Monitoring Battery Status

```python
NetHyTech_Battery.battery_alert()
```

This function continuously monitors the battery status and generates alerts when the battery percentage falls below 30% or 10%, or when it's fully charged (100%).

### Checking Plug-in Status

```python
NetHyTech_Battery.check_plugin_status()
```

This function checks the status of the power plug and generates alerts when the device is plugged in or unplugged.

### Getting Battery Percentage

```python
NetHyTech_Battery.battery_percentage()
```

This function returns the current battery percentage of the device.

## Example

```python
import NetHyTech_Battery

# Continuous monitoring of battery status
NetHyTech_Battery.battery_alert()

# Check plug-in status
NetHyTech_Battery.check_plugin_status()

# Get battery percentage
battery_percent = NetHyTech_Battery.battery_percentage()
print(battery_percent)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
