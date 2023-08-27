import asyncio as ai

def prints():
    print('shtok')

def method():
    for i in range(0, 10):
        if i == 2:
            ai.run(prints())
        print('method 1!')
    ai.run(prints())

async def method2():
    for i in range(0, 10):
        await ai.sleep(0.07)
        print('method 2!')

async def method3():
    for i in range(0, 1):
        await ai.sleep(0.002)
        print('method 3!')


async def main():
   ai.run(method())
   await ai.gather(method3())

   await ai.gather(method2(), method3())

ai.run(main())
