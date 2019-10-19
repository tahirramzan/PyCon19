import asyncio

async def nested():
    return 42

async def main():

    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())
