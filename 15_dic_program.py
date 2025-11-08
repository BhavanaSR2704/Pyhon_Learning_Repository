birth_days ={
    "Bhavana":"27/04/2006",
    "Bharathi":"25/05/1982",
    "Gnanesh": "22/05/2004",
    "Renukappa":"23/07/1967"
}
print(birth_days)
print(birth_days["Bhavana"])
print(birth_days.get("Thanu","sorry not found")) # This is the methode that don't give a key error 
birth_days["Thanu"]="07/07/2010" # adding the key and value in run time
print(birth_days)
birth_days.pop("Thanu") #remove the perticular key and value both
print(birth_days)
print(birth_days.keys())
print(birth_days.items()) # remember it ,it is very importent




d={
    123:456,
    (1):"bhavana",
    789:24.27,
    "bhanu":[27,4,2006]
}     # we can store any thing in dict but not list as a key
print(d)
