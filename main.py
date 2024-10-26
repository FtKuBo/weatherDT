from requests_html import HTMLSession

s = HTMLSession()

def getCityWeatherData(cityName):
    query = cityName
    url = f'https://www.google.ca/search?q=weather+{query}'

    r = s.get(url, headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'})

    temp, unit, description = data = r.html.find('span#wob_tm', first=True), r.html.find('div.vk_bk.wob-unit span.wob_t', first = True), r.html.find('div.VQF4g', first = True).find('span#wob_dc', first=True)
    
    for i in range(len(data)):
        if data[i]:
            data[i] = data[i].text
        else : return None
    
    return f'{cityName[0].upper()+cityName[1:]} : {temp} {unit} | The city is {description.lower()}'


if __name__ == '__main__':

    city = ""
    while len(city.replace(" ", "") ) <= 0 : 
        city = input("Enter a city of your choice : ")

    output = getCityWeatherData(city)

    print("--------------------------------------------------------------------------------")
    print(output if not output is None else "We couldn't find data for the city you inputed")
    print("--------------------------------------------------------------------------------")