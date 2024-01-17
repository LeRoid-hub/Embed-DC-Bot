import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, File
from responses import get_response

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Set up Intents
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("No message")
        return
    if is_private := user_message.startswith("private"):
        user_message = user_message[7:]

    if is_twitter := (user_message.startswith("https://x.com") or user_message.startswith("https://twitter.com")):
        print("Twitter link")

    try:
        response = await get_response(user_message)
        if response is None:
            return
        if is_twitter:
            await message.channel.send(file=File(response), reference=message)
            os.remove(response)
        else:
            await message.author.send(response) if is_private else await message.channel.send(response, reference=message)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'{username} sent a message in {channel}: {user_message}')
    await send_message(message, user_message)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()

