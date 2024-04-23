from urllib.parse import quote
import random

def getWALink(no: str, title: str) -> str:
    noWA = int(no)
    text = ("Assalamualaikum.\n" +
            f"saya ingin membeli {title} apakah masih ada ?"
            )
    sub = quote(text)
    link = f'https://wa.me/62{str(noWA)}?text={sub}'
    return link

def generateLink(id) -> str:
    generate = ''.join(random.choices('0123456789', k=10))  
    return f'{generate}{str(id)}'


def getRange(result) -> int:
    max_range = 10
    for count in result['dates'] :
        if count['total'] > max_range:
            max_range = count['total'] + 10
    return max_range