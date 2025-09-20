import asyncio

async def make_fried_eggs():
    await asyncio.sleep(2)
    print("Fried eggs are ready!")

async def make_sandwich():
    await asyncio.sleep(1)
    print("Sandwich is ready!")

async def make_coffee():
    await asyncio.sleep(1)
    print("Coffee is ready!")

async def make_breakfast():
    eggs_task = make_fried_eggs()
    coffee_task = make_coffee()
    await make_sandwich()
    await asyncio.gather(eggs_task, coffee_task)

asyncio.run(make_breakfast())
