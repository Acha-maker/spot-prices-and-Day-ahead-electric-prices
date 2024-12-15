# Days-ahead Prices  Documentation


 The API Used here is Energy chart AI whic gives prices for electricity as well as the 
 date and time.The API provided were free so the API key was also free

The code writen in python (electricprices.py) fetches the Electricity prices from the Energy
chart API and convert it to a Jason file to be used in the front end.The Jason prices can be accessed here http://127.0.0.1:5000/api/prices

# Battery simullation
The code simmulation.py simulates 

Battery capacity was 20KWh.
charging rate is 2KW. 
The condition for chargy is that the battery only charges when the  price is 5cent/KW
Charging range : Charging happens from 20% to 90% of the batterty capacity

In other to estimate how long it will take to charge the battery from 20% to 90% with a battery capacity of 20kwh and charging rate of 2kw

initially, the battery is 20% which means that the batery is at 20% of 20KWh =4kwh

Final charge capacity is 90% of 20KWh = 18KWh

The charging amount is 18KWh-4Kwh which is 14KWh
in The code, charging only takes place when the price is below 5cent/KWh 
duration of charging for 2KW/h is 7hours.

in the space of 24hours for data for Germany, the price was less than 50cent 8 times on december 15 2024.

Charging duration depends sorely on how long the day ahead price is below 5cent/Kwh

# Challenges
As an Electrical Engineer, it was challenging for me to writte the codes that can fetch data from the back end and display in the front end 
After lot of effort, I was able to code the front end and the back end without the best UI functionality but the logic I explained above is what is the logic I propose for the simullation.
