#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import requests

def main():
    """
    The magic happens here...

    A mágica acontece aqui...
    """

    codes= {
            0: "Céu limpo☀️",
            1: "Parcialmente nublado⛅",
            2: "Parcialmente nublado⛅",
            3: "Parcialmente nublado⛅",
            45: "Neblina🌫️",
            48: "Neblina🌫️",
            51: "Chuvisco🌦️",
            53: "Chuvisco🌦️",
            55: "Chuvisco🌦️",
            56: "Chuvisco congelado❄️",
            57: "Chuvisco congelado❄️",
            61: "Chuva🌧️",
            63: "Chuva🌧️",
            65: "Chuva🌧️",
            66: "Chuva congelada❄️",
            67: "Chuva congelada❄️",
            71: "Neve🌨️",
            73: "Neve🌨️",
            75: "Neve🌨️",
            80: "Chuva forte🌧️",
            81: "Chuva forte🌧️",
            82: "Chuva forte🌧️",
            85: "Nevasca🌨️",
            86: "Nevasca🌨️",
            95: "Tempestade⛈️",
            96: "Tempestade⛈️",
            99: "Tempestade⛈️"
    }

    coordinates= (-29.68, -51.14)

    api= f'https://api.open-meteo.com/v1/forecast?latitude={config_file('LATITUDE')}8&longitude={config_file('LONGITUDE')}&current=temperature_2m,rain,weather_code&timezone=America%2FSao_Paulo&forecast_days=1'

    info= requests.get(api).json()
    
    info['current']['temperature_2m']=  str(info['current']['temperature_2m']).replace('.',',')

    return f'{info["current"]["temperature_2m"]}ºC🌡️ {codes[info["current"]["weather_code"]]}  em {config_file('CITY')} {config_file('STATE')}'

def config_file(parameter):
    config= {}

    with open('weather.config', 'r') as file:
        
        for x in file:
            line = x.rstrip()
            
            if line:
                item= line.split('=')
                
                if len(item) == 2 and item[0][0] != '#':
                    item[1]= item[1].replace(' ', '')
                    item[1]= item[1].replace('\n', '')
                    item[1]= item[1].replace('_', ' ')

                    item= [(item[0], item[1])]
                    config.update(item)
                
    file.close()
    
    try:
        return config[parameter]
    
    except:
        return 'ERROR'

if __name__ == '__main__':
    main()