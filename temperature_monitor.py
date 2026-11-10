
# CTE123 PYTHON MINI PROJECT
# MACHINE TEMPERATURE MONITORING SYSTEM
# WITH TRAFFIC LIGHT, DIGITAL GAUGE AND ALARM

def temperature_gauge(temp):
    # Convert temperature into a visual gauge
    value = max(0, min(temp, 100))
    bars = int(value / 5)

    print("\nDIGITAL TEMPERATURE GAUGE")
    print("[" + "█" * bars + "-" * (20 - bars) + "]")
    print(f"Temperature: {temp} °C")


def alarm_sound():
    # Produce an alarm sound on supported systems
    print("\n!!! CRITICAL TEMPERATURE ALARM !!!")

    try:
        import winsound

        # Three warning beeps (Windows)
        for i in range(3):
            winsound.Beep(1000, 500)

    except ImportError:
        # Fallback terminal alert
        print("\a\a\a")
        print("ALARM! CHECK MACHINE TEMPERATURE!")


def monitor_temperature():

    temperatures = []

    safe_limit = 80
    warning_limit = 70

    print("===================================")
    print(" MACHINE TEMPERATURE MONITOR")
    print(" TRAFFIC LIGHT ALARM SYSTEM")
    print("===================================")

    # Collect five temperature readings
    for i in range(5):

        while True:
            try:
                temp = float(input(
                    f"Enter temperature {i + 1} (°C): "
                ))

                if temp < -273.15:
                    print("Invalid temperature!")
                    continue

                temperatures.append(temp)
                break

            except ValueError:
                print("Enter a valid number!")

    # Calculate temperature statistics
    highest = max(temperatures)
    lowest = min(temperatures)
    average = sum(temperatures) / len(temperatures)

    print("\n========== TEMPERATURE REPORT ==========")

    print("Readings:", temperatures)
    print("Highest:", highest, "°C")
    print("Lowest:", lowest, "°C")
    print("Average:", round(average, 2), "°C")

    # Display gauge and traffic light for each reading
    print("\n========== MONITORING SYSTEM ==========")

    for temp in temperatures:

        print("\n-----------------------------------")

        temperature_gauge(temp)

        if temp > safe_limit:

            print("🔴 RED LIGHT")
            print("STATUS: CRITICAL")

            alarm_sound()

        elif temp >= warning_limit:

            print("🟡 YELLOW LIGHT")
            print("STATUS: WARNING")

        else:

            print("🟢 GREEN LIGHT")
            print("STATUS: NORMAL")

    # Overall machine status
    print("\n========== FINAL MACHINE STATUS ==========")

    if highest > safe_limit:

        print("🔴 RED LIGHT - CRITICAL")
        print("Machine requires attention.")

    elif highest >= warning_limit:

        print("🟡 YELLOW LIGHT - WARNING")
        print("Monitor machine temperature.")

    else:

        print("🟢 GREEN LIGHT - NORMAL")
        print("Machine temperature is normal.")

    print("\n===================================")
    print(" MONITORING COMPLETED")
    print("===================================")


# Start the program
monitor_temperature()
      
