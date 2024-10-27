import requests

def fetch_quote_freeapi():
  url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
  response = requests.get(url)
  rec_data = response.json()
  
  if rec_data["success"] and "data" in rec_data:
    user_data = rec_data["data"]
    quote_data = user_data["content"]
    author = user_data["author"]
    tag = user_data["tags"]
    return quote_data,author,tag
  else:
    raise Exception("Failed to Fetch quote")
  
def main():
  try:
    quote_data, author, tag = fetch_quote_freeapi()
    print(f"Quote of the Day on {tag}: {quote_data} \n{author}")
  except Exception as error:
    print(str(error))

if __name__ == "__main__":
    main()