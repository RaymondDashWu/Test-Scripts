"""
https://docs.python.org/3/library/asyncio.html
Notes:
    Possible uses: 
        -Webpage loading asynchronously. E.g if server is slow load other elements alongside
        -aiohttp
"""
import asyncio

"""
#Without comparison
def find_divisibles(inrange, div_by):
    print("finding numbers divisible by {} throughout range {}".format(div_by, inrange))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
    print("Done with numbers in range {} divisible by {}".format(inrange, div_by))
    return located
def test_dataset():
    divs1 = find_divisibles(500, 3)
    #divs2 = find_divisibles(10023908, 645)
    #divs3 = find_divisibles(125084238907478939, 78934)
"""    

#With comparison
async def find_divisibles(inrange, div_by):
    print("finding numbers divisible by {} throughout range {}".format(div_by, inrange))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)           
    print("Done with numbers in range {} divisible by {}".format(inrange, div_by))
    return located

async def test_dataset():
    divs1 = loop.create_task(find_divisibles(500, 5))
    divs2 = loop.create_task(find_divisibles(10023908, 645))
    divs3 = loop.create_task(find_divisibles(125084238907478939, 78934))
    await asyncio.wait([divs1, divs2, divs3])
    return divs1, divs2, divs3

if __name__ == "__test_dataset__":
    try:
        loop = asyncio.get_event_loop()
        loop.set_debug(1)
        loop.run_until_complete(test_dataset())
    except:
        pass
    finally:
        loop.close()
        