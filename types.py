weather = {

"city":"Москва",
"temperature":"20"
}
print(weather["city"])

weather ["temperature"] = str(int(weather ["temperature"]) - 5)
print(weather)
print(weather.get("contry", "Россия"))
weather["date"] = "25.09.2019"
print(weather)
print(len(weather))
