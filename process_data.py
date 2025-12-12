import pandas as pd 

def process_weather_data(raw_data):
    if 'error' in raw_data:
        return raw_data
    
    processed_data = {
        "City": raw_data['name'],
        "Temperature": raw_data['main']['temp'],
        "Humidity": raw_data['main']['humidity'],
        "weather": raw_data['weather'][0]['description']
    }
    
    data = pd.DataFrame([processed_data])
    data.fillna("Unknown", inplace=True)
    return data