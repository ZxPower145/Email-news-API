import requests as req
import send_email as se

topic = "tesla"

api_key = "79d1f6c78da344299c31ce709ef97daf"

url = f"https://newsapi.org/v2/everything?q={topic}&" \
      "from=2023-04-21&" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      "language=en"

# made a request
request = req.get(url)

# Get a dictionary with data
content = request.json()

body = ""

# Access the article titles and description
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2*"\n"

message = f"""\
Subject: {topic.capitalize()} News Letter

{body}

"""
message = message.encode("utf-8")
se.send_email(message)
