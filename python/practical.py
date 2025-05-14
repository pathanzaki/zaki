def average_weekend_temperature(temperatures):
    """
    Function to calculate the average temperature over the weekend.
    """
   
    weekend_days = ['Saturday', 'Sunday']
    
    
    weekend_temps = [temp for day, temp in temperatures.items() if day in weekend_days]
    
    if not weekend_temps:
        return None  
    average_temp = sum(weekend_temps) / len(weekend_temps)
    return average_temp


def main():
    temperatures = {
        'Monday': 70,
        'Tuesday': 68,
        'Wednesday': 75,
        'Thursday': 72,
        'Friday': 74,
        'Saturday': 78,
        'Sunday': 80
    }
    
    avg_temp = average_weekend_temperature(temperatures)
    
    if avg_temp is not None:
        print(f"Average weekend temperature: {avg_temp:.2f}°F")
    else:
        print("No weekend data available to calculate average temperature.")

        
if __name__ == "__main__":
    main()
