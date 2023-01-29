import requests
from bs4 import BeautifulSoup
import discord

client = discord.Client()

def get_news_headlines(keyword):
    url = f"https://news.google.com/search?q={keyword}&hl=en-US&gl=US&ceid=US%3Aen"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []
    for h3_tag in soup.find_all("h3"):
        headline = h3_tag.text.strip()
        headlines.append(headline)
    return headlines[:3]

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.content.startswith("!news"):
        keyword = message.content[6:]
        headlines = get_news_headlines(keyword)
        response = "\n".join([f"{i + 1}. {headline}" for i, headline in enumerate(headlines)])
        await message.channel.send(response)

client.run("YOUR_DISCORD_BOT_TOKEN_GOES_HERE")
