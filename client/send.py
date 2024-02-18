import random
import asyncio
import aiohttp

URLS = ['http://localhost:8080/messages']#, 'http://localhost:8081/messages']

NAMES = ["Benjamin", "Olivia", "Ethan", "Charlotte", "Liam", "Sophia", "William", "Ava", "James", "Emma"]

TEXT_LIMIT = 1000
FILE_WITH_TEXT = "Hamlet.txt"


def create_data():
    sender_name = random.choice(NAMES)
    with open(FILE_WITH_TEXT, 'r') as f:
        text_limit = random.randint(10, TEXT_LIMIT)
        message = f.read(text_limit)
    data = {'name': sender_name, 'text': message}
    return data


async def send_message():
    async with aiohttp.ClientSession() as session:
        for _ in range(100):
            url = random.choice(URLS)
            data = create_data()
            async with session.post(url, json=data) as response:
                response_data = await response.json()
                # print(response_data) 


async def main():
    tasks = []
    for _ in range(50):
        tasks.append(asyncio.create_task(send_message()))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
