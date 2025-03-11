import asyncio

async def say_hello():
    print('Hello!')
    await asyncio.sleep(5)
    print('World!')

asyncio.run(say_hello())