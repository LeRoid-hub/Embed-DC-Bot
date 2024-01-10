from random import choice, randint
from tweetcapture import TweetCapture

async def tweetCapture(url, port):
    tweet = TweetCapture()
    tweet.add_chrome_argument(f"--remote-debugging-port={port}")
    filename = await tweet.screenshot(url, overwrite=True)
    return filename

async def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif lowered.startswith('https://x.com'):
        return await tweetCapture(lowered, 9222)
