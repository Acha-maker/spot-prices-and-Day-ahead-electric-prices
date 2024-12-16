# Days-ahead Prices  Documentation


 The API Used here is Energy chart API which gives Electricity spot prices and  day ahead  prices for electricity as well as the 
 date and time.The API provided were free so the API key was also free to be used for this purpose and not for commercial use.

The code writen in python (electricityprices.py) fetches the Electricity prices from the Energy
chart API and convert it to a Json file to be used in the frontend.The Jason prices can be accessed here http://127.0.0.1:5000/api/prices

# Battery simullation
The code simmulation.py simulates 

Battery capacity was 20KWh.
charging rate is 2KW. 
The condition for chargy is that the battery only charges when the  price is 5cent/KW
Charging range : Charging happens from 20% to 90% of the batterty capacity

In other to estimate how long it will take to charge the battery from 20% to 90% with a battery capacity of 20kwh and charging rate of 2kw

Initially, the battery is 20% which means that the batery is at 20% of 20KWh =4kwh

Final charge capacity is 90% of 20KWh = 18KWh

The charging amount is 18KWh-4Kwh which is 14KWh

In The code, charging only takes place when the price is below 5cent/KWh 
duration of charging for 2KW per hour of charging  is normally supposed to be 7hours.

In the space of 24hours for data fo Germany fetched from the API, the price was less than 50cent four times on December 10-2024.
charging duration for this day starting the charging from 9am will take 11hours to reach battery capacity of 90% .

Charging duration depends sorely on how long the day ahead price is below 5cent/Kwh and also the price during the period where the battery is being charged

# Programming languages used

Backend: python for fetching data from API and simmulation

Front end: Html for the web page, Css for styling and Java fro fetching JSON data from the backend and display in front end.

# Challenges
As an Electrical Engineer, it was challenging for me to write the codes that can fetch data from the backend and display in the frontend 
After lot of effort, I was able to code the frontend and the backend without the best UI functionality but the logic I explained above is what is the logic I propose for the simullation.
