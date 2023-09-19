This app is responsible for downloading data from okx.
It's check every N seconds the most resent data in database.
Compere difference betwen current date and the most resent data in database. 
Calculate count requests to be done and limit requested data per call.
Calculate datetime to start (most resent datetime + TF)
After all data is loaded in memory, service try to save it into database.

N = 180
TF = 5*60

