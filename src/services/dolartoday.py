import requests

# Dolar today wrapper
class DolartodayService:
  def __init__(self):
    self.apiurl = "https://s3.amazonaws.com/dolartoday/data.json"

  def __getData(self):
    return requests.get(self.apiurl).json()

  # Get current dollar price
  def getDolarPrice(self):
    data = self.__getData()
    return {
      "price": data["USD"]["dolartoday"]
    }

  # Get current eur price
  def getEuroPrice(self):
    data = self.__getData()
    return {
      "price": data["EUR"]["dolartoday"]
    }
