import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# asyncio.run(main())


async def task(name, delay):
    print(f"Task {name} start")
    await asyncio.sleep(delay)
    print(f"Task {name} done")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3)
    )

asyncio.run(main())