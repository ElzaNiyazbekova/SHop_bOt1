from bs4 import BeautifulSoup
import requests
from config import HEADERS, URL, DOMEN, LIST_BRANDS
from products import insert_product

def get_html(URL, headers=HEADERS, params=' '):
    html = requests.get(URL, headers=headers, params=params)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup



def get_data(soup, brand):
    data = []
    items = soup.find_all('div', class_='item-card')

    for item in items:
        try:
           name = item.find('div', class_='item-card__info').find('a').get_text(strip=True).split()[:-1]

           right_name = ''
           memory = ''
           color = name[-1]
           call_back = '_'.join(name[:3]).lower()
           brand = brand
           for i in name[:-1]:
                if 'gb' in i.lower() or 'гб' in i.lower():
                    memory += i
                else:
                    right_name += i+' '


        except:
            right_name = None
            memory = None
            color = None
            call_back = None
            brand = None
        
        try:
            url = DOMEN + item.find('a', class_='item-card__image-wrapper').get('href')
        except:
            url = 'None'

        try:
            price = item.find('span', class_='item-card__prices-price').get_text(strip=True).replace('₸', '').replace(' ','')
        except:
            price = 0
        local_data = get_html(url)
        img = local_data.find_all('meta')[12].get('content')
        description = local_data.find('div', class_='item__description-text').get_text(strip=True)
        if right_name is not None:
            data.append({
                'name': right_name,
                'description': description,
                'price': int(price),
                'photo': img,
                'memory': memory,
                'color': color,
                'brand': brand,
                'call_back': call_back,
                'url': url})
    return data
        
# soup = get_html(URL+'apple')
# print(get_data(soup, 'apple'))

def parse(LIST_BRANDS, page):
    contents = []
    for brand in LIST_BRANDS:
        for page in range(1 , page+1):
            html = get_html(URL+brand, params={'page': page})
            content = get_data(html, brand)
            contents.extend(content)
            print(f"Страница Бренд {brand} {page} готово!")
        return contents


def add_products_db(items: list[dict]):
    for item in items:
        insert_product(
            name=item['name'],
            description=item['description'],
            price=item['price'],
            photo=item['photo'],
            memory=item['memory'],
            color=item['color'],
            brand=item['brand'],
            call_back=item['call_back'],
            url=item['url'])
        print(f"{item['name']} добавлен в базу данных")


# from pprint import pprint
# pprint(parse(LIST_BRANDS, page=2))
data = [{'brand': 'apple',
  'call_back': 'apple_iphone_11',
  'color': 'черный',
  'description': '- тип экрана: сенсорный мультитач цветной IPS, Liquid Retina '
                 'HD- диагональ: 6.1 дюйм- размер оперативной памяти: 4 ГБ- '
                 'технология nfc: да- цвет: черный- процессор: 6-ядерный Apple '
                 'A13 Bionic- объем встроенной памяти: 128 ГБ- емкость '
                 'аккумулятора: 3110 мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 11 Slim Box ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h1f/hed/26542732345374/apple-iphone-11-128gb-slim-box-cernyj-100692388-1-Container.png',
  'price': 298612,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-11-128gb-slim-box-chernyi-100692388/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_13',
  'color': 'черный',
  'description': '- тип экрана: OLED, Super Retina XDR- диагональ: 6.1 дюйм- '
                 'размер оперативной памяти: 4 ГБ- технология nfc: да- цвет: '
                 'черный- процессор: 6-ядерный Apple A15 Bionic- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 3095 мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 13 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h01/h94/45664460734494/apple-iphone-13-128gb-cernyj-102298404-1-Container.jpg',
  'price': 417330,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-13-128gb-chernyi-102298404/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_11',
  'color': 'белый',
  'description': '- тип экрана: сенсорный мультитач цветной IPS, Liquid Retina '
                 'HD- диагональ: 6.1 дюйм- размер оперативной памяти: 4 ГБ- '
                 'технология nfc: да- цвет: белый- процессор: 6-ядерный Apple '
                 'A13 Bionic- объем встроенной памяти: 128 ГБ- емкость '
                 'аккумулятора: 3110 мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 11 Slim Box ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h37/h96/26544853909534/apple-iphone-11-128gb-slim-box-belyj-100692385-1-Container.png',
  'price': 306399,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-11-128gb-slim-box-belyi-100692385/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_11',
  'color': 'черный',
  'description': '- тип экрана: сенсорный мультитач цветной IPS, Liquid Retina '
                 'HD- диагональ: 6.1 дюйм- размер оперативной памяти: 4 ГБ- '
                 'технология nfc: да- цвет: черный- процессор: 6-ядерный Apple '
                 'A13 Bionic- объем встроенной памяти: 64 ГБ- емкость '
                 'аккумулятора: 3110 мАч',
  'memory': '64Gb',
  'name': 'Apple iPhone 11 Slim Box ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h3c/ha0/26542964768798/apple-iphone-11-64gb-slim-box-cernyj-100692387-1-Container.png',
  'price': 264220,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-11-64gb-slim-box-chernyi-100692387/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_13',
  'color': 'зеленый',
  'description': '- тип экрана: OLED, Super Retina XDR- диагональ: 6.1 дюйм- '
                 'размер оперативной памяти: 4 ГБ- технология nfc: да- цвет: '
                 'зеленый- процессор: 6-ядерный Apple A15 Bionic- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 3095 мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 13 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h56/hbd/49319164444702/apple-iphone-13-128gb-zelenyj-104078887-1.png',
  'price': 421212,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-13-128gb-zelenyi-104078887/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_13',
  'color': 'белый',
  'description': '- тип экрана: OLED, Super Retina XDR- диагональ: 6.1 дюйм- '
                 'размер оперативной памяти: 4 ГБ- технология nfc: да- цвет: '
                 'белый- процессор: 6-ядерный Apple A15 Bionic- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 3095 мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 13 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h33/hed/45664374849566/apple-iphone-13-128gb-belyj-102298420-1-Container.jpg',
  'price': 416440,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-13-128gb-belyi-102298420/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_13',
  'color': 'синий',
  'description': '- тип экрана: OLED, Super Retina XDR- диагональ: 6.1 дюйм- '
                 'размер оперативной памяти: 4 ГБ- технология nfc: да- цвет: '
                 'синий- процессор: 6-ядерный Apple A15 Bionic- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 3095 мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 13 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hc5/h40/45664453296158/apple-iphone-13-128gb-sinij-102298364-1-Container.jpg',
  'price': 417000,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-13-128gb-sinii-102298364/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_14',
  'color': 'фиолетовый',
  'description': '- тип экрана: OLED, Super Retina XDR display с возможностью '
                 'постоянной работы- диагональ: 6.1 дюйм- размер оперативной '
                 'памяти: 6 ГБ- технология nfc: да- цвет: фиолетовый- '
                 'процессор: 6-ядерный Apple A16 Bionic- объем встроенной '
                 'памяти: 256 ГБ- емкость аккумулятора: 3125 мАч',
  'memory': '256Gb',
  'name': 'Apple iPhone 14 Pro ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h8f/he0/62948396630046/apple-iphone-14-pro-128gb-fioletovyj-106363319-1.png',
  'price': 769990,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-14-pro-256gb-fioletovyi-106363319/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_12',
  'color': 'черный',
  'description': '- тип экрана: сенсорный, мультитач OLED Super Retina XDR- '
                 'диагональ: 6.1 дюйм- размер оперативной памяти: 4 ГБ- '
                 'технология nfc: да- цвет: черный- процессор: 6-ядерный Apple '
                 'A14 Bionic- объем встроенной памяти: 128 ГБ- емкость '
                 'аккумулятора: 2775 мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 12 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h02/h40/17090574778398/apple-iphone-12-128gb-cernyj-100656960-1-Container.png',
  'price': 370742,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-12-128gb-chernyi-100656960/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_14',
  'color': 'фиолетовый',
  'description': '- тип экрана: OLED, Super Retina XDR display с возможностью '
                 'постоянной работы- диагональ: 6.7 дюйм- размер оперативной '
                 'памяти: 6 ГБ- технология nfc: да- цвет: фиолетовый- '
                 'процессор: 6-ядерный Apple A16 Bionic- объем встроенной '
                 'памяти: 256 ГБ- емкость аккумулятора: 3095 мАч',
  'memory': '256Gb',
  'name': 'Apple iPhone 14 Pro Max ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/he7/hd7/62948780638238/apple-iphone-14-pro-max-128gb-fioletovyj-106363342-1.png',
  'price': 839990,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-14-pro-max-256gb-fioletovyi-106363342/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_11',
  'color': 'белый',
  'description': '- тип экрана: сенсорный мультитач цветной IPS, Liquid Retina '
                 'HD- диагональ: 6.1 дюйм- размер оперативной памяти: 4 ГБ- '
                 'технология nfc: да- цвет: белый- процессор: 6-ядерный Apple '
                 'A13 Bionic- объем встроенной памяти: 64 ГБ- емкость '
                 'аккумулятора: 3110 мАч',
  'memory': '64Gb',
  'name': 'Apple iPhone 11 Slim Box ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h86/h65/26545004314654/apple-iphone-11-64gb-slim-box-belyj-100692384-1-Container.png',
  'price': 260888,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-11-64gb-slim-box-belyi-100692384/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_13',
  'color': 'зеленый',
  'description': '- тип экрана: OLED, Super Retina XDR- диагональ: 6.7 дюйм- '
                 'размер оперативной памяти: 6 ГБ- технология nfc: да- цвет: '
                 'зеленый- процессор: 6-ядерный Apple A15 Bionic- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 4352 мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 13 Pro Max ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hd9/h6c/49319414202398/apple-iphone-13-pro-max-128gb-zelenyj-104079084-1.png',
  'price': 622880,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-13-pro-max-128gb-zelenyi-104079084/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_14',
  'color': 'черный',
  'description': '- тип экрана: OLED, Super Retina XDR display- диагональ: 6.1 '
                 'дюйм- размер оперативной памяти: 6 ГБ- технология nfc: да- '
                 'цвет: черный- процессор: 6-ядерный Apple A15 Bionic- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 3279 мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 14 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hab/hda/63072540033054/apple-iphone-14-128gb-cernyj-106363023-1.png',
  'price': 476908,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-14-128gb-chernyi-106363023/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_12',
  'color': 'синий',
  'description': '- тип экрана: сенсорный, мультитач OLED Super Retina XDR- '
                 'диагональ: 6.1 дюйм- размер оперативной памяти: 4 ГБ- '
                 'технология nfc: да- цвет: синий- процессор: 6-ядерный Apple '
                 'A14 Bionic- объем встроенной памяти: 128 ГБ- емкость '
                 'аккумулятора: 2775 мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 12 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h17/h81/26538141745182/apple-iphone-12-128gb-sinij-100656957-1-Container.png',
  'price': 370750,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-12-128gb-sinii-100656957/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_14',
  'color': 'фиолетовый',
  'description': '- тип экрана: OLED, Super Retina XDR display с возможностью '
                 'постоянной работы- диагональ: 6.7 дюйм- размер оперативной '
                 'памяти: 6 ГБ- технология nfc: да- цвет: фиолетовый- '
                 'процессор: 6-ядерный Apple A16 Bionic- объем встроенной '
                 'памяти: 128 ГБ- емкость аккумулятора: 3095 мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 14 Pro Max ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h80/h4e/62948780015646/apple-iphone-14-pro-max-128gb-fioletovyj-106363303-1.png',
  'price': 769990,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-14-pro-max-128gb-fioletovyi-106363303/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_14',
  'color': 'фиолетовый',
  'description': '- тип экрана: OLED, Super Retina XDR display с возможностью '
                 'постоянной работы- диагональ: 6.1 дюйм- размер оперативной '
                 'памяти: 6 ГБ- технология nfc: да- цвет: фиолетовый- '
                 'процессор: 6-ядерный Apple A16 Bionic- объем встроенной '
                 'памяти: 128 ГБ- емкость аккумулятора: 3125 мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 14 Pro ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h0f/h8c/62948389650462/apple-iphone-14-pro-128gb-fioletovyj-106363283-1.png',
  'price': 699990,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-14-pro-128gb-fioletovyi-106363283/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_14',
  'color': 'черный',
  'description': '- тип экрана: OLED, Super Retina XDR display с возможностью '
                 'постоянной работы- диагональ: 6.7 дюйм- размер оперативной '
                 'памяти: 6 ГБ- технология nfc: да- цвет: черный- процессор: '
                 '6-ядерный Apple A16 Bionic- объем встроенной памяти: 256 ГБ- '
                 'емкость аккумулятора: 3095 мАч',
  'memory': '256Gb',
  'name': 'Apple iPhone 14 Pro Max ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hea/h1a/63073422901278/apple-iphone-14-pro-max-128gb-cernyj-106363289-1.png',
  'price': 869990,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-14-pro-max-256gb-chernyi-106363289/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_13',
  'color': 'розовый',
  'description': '- тип экрана: OLED, Super Retina XDR- диагональ: 6.1 дюйм- '
                 'размер оперативной памяти: 4 ГБ- технология nfc: да- цвет: '
                 'розовый- процессор: 6-ядерный Apple A15 Bionic- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 3095 мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 13 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h9f/h49/45664456704030/apple-iphone-13-128gb-rozovyj-102298145-1-Container.jpg',
  'price': 417463,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-13-128gb-rozovyi-102298145/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_12',
  'color': 'белый',
  'description': '- тип экрана: сенсорный, мультитач OLED Super Retina XDR- '
                 'диагональ: 6.1 дюйм- размер оперативной памяти: 4 ГБ- '
                 'технология nfc: да- цвет: белый- процессор: 6-ядерный Apple '
                 'A14 Bionic- объем встроенной памяти: 128 ГБ- емкость '
                 'аккумулятора: 2775 мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 12 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hf8/h86/17090588213278/apple-iphone-12-128gb-belyj-100656959-1-Container.png',
  'price': 370670,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-12-128gb-belyi-100656959/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_12',
  'color': 'черный',
  'description': '- тип экрана: сенсорный, мультитач OLED, Super Retina XDR- '
                 'диагональ: 6.1 дюйм- размер оперативной памяти: 4 ГБ- '
                 'технология nfc: да- цвет: черный- процессор: 6-ядерный Apple '
                 'A14 Bionic- объем встроенной памяти: 64 ГБ- емкость '
                 'аккумулятора: 2775 мАч',
  'memory': '64Gb',
  'name': 'Apple iPhone 12 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h9c/h0c/26538910941214/apple-iphone-12-64gb-cernyj-100656839-1-Container.png',
  'price': 339000,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-12-64gb-chernyi-100656839/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_13',
  'color': 'зеленый',
  'description': '- тип экрана: OLED, Super Retina XDR- диагональ: 6.7 дюйм- '
                 'размер оперативной памяти: 6 ГБ- технология nfc: да- цвет: '
                 'зеленый- процессор: 6-ядерный Apple A15 Bionic- объем '
                 'встроенной памяти: 256 ГБ- емкость аккумулятора: 4352 мАч',
  'memory': '256Gb',
  'name': 'Apple iPhone 13 Pro Max ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h61/hb9/49319418429470/apple-iphone-13-pro-max-256gb-zelenyj-104079153-1.png',
  'price': 691870,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-13-pro-max-256gb-zelenyi-104079153/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_14',
  'color': 'сиреневый',
  'description': '- тип экрана: OLED, Super Retina XDR display- диагональ: 6.1 '
                 'дюйм- размер оперативной памяти: 6 ГБ- технология nfc: да- '
                 'цвет: сиреневый- процессор: 6-ядерный Apple A15 Bionic- '
                 'объем встроенной памяти: 128 ГБ- емкость аккумулятора: 3279 '
                 'мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 14 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h42/h2a/63072545636382/apple-iphone-14-128gb-sirenevyj-106363117-1.png',
  'price': 480935,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-14-128gb-sirenevyi-106363117/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_14',
  'color': 'черный',
  'description': '- тип экрана: OLED, Super Retina XDR display с возможностью '
                 'постоянной работы- диагональ: 6.1 дюйм- размер оперативной '
                 'памяти: 6 ГБ- технология nfc: да- цвет: черный- процессор: '
                 '6-ядерный Apple A16 Bionic- объем встроенной памяти: 128 ГБ- '
                 'емкость аккумулятора: 3125 мАч',
  'memory': '128Gb',
  'name': 'Apple iPhone 14 Pro ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h5c/hed/63073437515806/apple-iphone-14-pro-128gb-cernyj-106363245-1.png',
  'price': 699990,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-14-pro-128gb-chernyi-106363245/?c=750000000'},
 {'brand': 'apple',
  'call_back': 'apple_iphone_14',
  'color': 'черный',
  'description': '- тип экрана: OLED, Super Retina XDR display с возможностью '
                 'постоянной работы- диагональ: 6.1 дюйм- размер оперативной '
                 'памяти: 6 ГБ- технология nfc: да- цвет: черный- процессор: '
                 '6-ядерный Apple A16 Bionic- объем встроенной памяти: 256 ГБ- '
                 'емкость аккумулятора: 3125 мАч',
  'memory': '256Gb',
  'name': 'Apple iPhone 14 Pro ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h40/hd1/63073435156510/apple-iphone-14-pro-128gb-cernyj-106363265-1.png',
  'price': 764222,
  'url': 'https://kaspi.kz/shop/p/apple-iphone-14-pro-256gb-chernyi-106363265/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_note',
  'color': 'серый',
  'description': '- тип экрана: AMOLED, сенсорный, мультитач- диагональ: 6.67 '
                 'дюйм- размер оперативной памяти: 8 ГБ- технология nfc: да- '
                 'цвет: серый- процессор: MediaTek Helio G96- объем встроенной '
                 'памяти: 128 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Xiaomi Redmi Note 11 Pro 8 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/he0/h58/51166990270494/xiaomi-redmi-note-11-pro-8-128gb-seryj-103971386-1.png',
  'price': 135811,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-note-11-pro-8-gb-128-gb-seryi-103971386/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_10c',
  'color': 'серый',
  'description': '- тип экрана: IPS, сенсорный, мультитач- диагональ: 6.71 '
                 'дюйм- размер оперативной памяти: 4 ГБ- технология nfc: нет- '
                 'цвет: серый- процессор: 8-ядерный Qualcomm Snapdragon 680- '
                 'объем встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 '
                 'мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Xiaomi Redmi 10C 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hde/h4c/49939925008414/xiaomi-redmi-10c-4-gb-128-gb-seryj-104417231-1.jpg',
  'price': 74990,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-10c-4-gb-128-gb-seryi-104417231/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_note',
  'color': 'серый',
  'description': '- тип экрана: AMOLED, сенсорный, Corning Gorilla Glass 3- '
                 'диагональ: 6.43 дюйм- размер оперативной памяти: 4 ГБ- '
                 'технология nfc: нет- цвет: серый- процессор: 8-ядерный '
                 'Qualcomm Snapdragon 680- объем встроенной памяти: 128 ГБ- '
                 'емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Xiaomi Redmi Note 11 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h83/hc4/48472414093342/smartfon-xiaomi-redmi-note-11-4-128-graphite-gray-103541773-1.jpg',
  'price': 101650,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-note-11-4-gb-128-gb-seryi-103541773/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_9a',
  'color': 'серый',
  'description': '- тип экрана: сенсорный, мультитач, IPS- диагональ: 6.53 '
                 'дюйм- размер оперативной памяти: 2 ГБ- технология nfc: нет- '
                 'цвет: серый- процессор: 8-ядерный MediaTek Helio G25- объем '
                 'встроенной памяти: 32 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/32ГБ',
  'name': 'Xiaomi Redmi 9A 2 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h28/h55/26546736234526/xiaomi-redmi-9a-2-32gb-seryj-100399600-1-Container.png',
  'price': 47900,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-9a-2-gb-32-gb-seryi-100399600/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_10c',
  'color': 'голубой',
  'description': '- тип экрана: IPS, сенсорный, мультитач- диагональ: 6.71 '
                 'дюйм- размер оперативной памяти: 4 ГБ- технология nfc: нет- '
                 'цвет: голубой- процессор: 8-ядерный Qualcomm Snapdragon 680- '
                 'объем встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 '
                 'мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Xiaomi Redmi 10C 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h40/h1d/49939926384670/xiaomi-redmi-10c-4-gb-128-gb-goluboj-104417308-1.jpg',
  'price': 74890,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-10c-4-gb-128-gb-goluboi-104417308/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_10c',
  'color': 'зеленый',
  'description': '- тип экрана: IPS, сенсорный, мультитач- диагональ: 6.71 '
                 'дюйм- размер оперативной памяти: 4 ГБ- технология nfc: нет- '
                 'цвет: зеленый- процессор: 8-ядерный Qualcomm Snapdragon 680- '
                 'объем встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 '
                 'мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Xiaomi Redmi 10C 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h3c/h86/51348549763102/xiaomi-redmi-10c-4-gb-128-gb-zelenyj-104443164-1.png',
  'price': 79800,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-10c-4-gb-128-gb-zelenyi-104443164/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_10c',
  'color': 'серый',
  'description': '- тип экрана: IPS, сенсорный, мультитач- диагональ: 6.71 '
                 'дюйм- размер оперативной памяти: 4 ГБ- технология nfc: нет- '
                 'цвет: серый- процессор: 8-ядерный Qualcomm Snapdragon 680- '
                 'объем встроенной памяти: 64 ГБ- емкость аккумулятора: 5000 '
                 'мАч',
  'memory': 'ГБ/64ГБ',
  'name': 'Xiaomi Redmi 10C 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hc3/h11/49939919503390/xiaomi-redmi-10c-4-gb-64-gb-seryj-104417151-1.jpg',
  'price': 69890,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-10c-4-gb-64-gb-seryi-104417151/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_note',
  'color': 'серый',
  'description': '- тип экрана: AMOLED, сенсорный, мультитач- диагональ: 6.43 '
                 'дюйм- размер оперативной памяти: 6 ГБ- технология nfc: нет- '
                 'цвет: серый- процессор: 8-ядерный Qualcomm Snapdragon 680- '
                 'объем встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 '
                 'мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Xiaomi Redmi Note 11 6 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h08/h00/49181185638430/redmi-note-11-6-128gb-grey-103995646-1.png',
  'price': 105420,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-note-11-6-gb-128-gb-seryi-103995646/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_9c',
  'color': 'серый',
  'description': '- тип экрана: IPS, сенсорный- диагональ: 6.53 дюйм- размер '
                 'оперативной памяти: 3 ГБ- технология nfc: нет- цвет: серый- '
                 'процессор: 8-ядерный MediaTek Helio G35- объем встроенной '
                 'памяти: 64 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/64ГБ',
  'name': 'Xiaomi Redmi 9C 3 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/haa/h6f/50514293653534/xiaomi-redmi-9c-3-64gb-seryj-100500084-1-Container.png',
  'price': 66455,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-9c-3-gb-64-gb-seryi-100500084/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_10',
  'color': 'серый',
  'description': '- тип экрана: сенсорный, мультитач, IPS- диагональ: 6.5 '
                 'дюйм- размер оперативной памяти: 4 ГБ- технология nfc: нет- '
                 'цвет: серый- процессор: MediaTek Helio G88- объем встроенной '
                 'памяти: 128 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Xiaomi Redmi 10 2022 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/he0/hf2/51310464598046/xiaomi-redmi-10-2022-4-gb-128-gb-seryj-105170511-1.jpg',
  'price': 89580,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-10-2022-4-gb-128-gb-seryi-105170511/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_9a',
  'color': 'голубой',
  'description': '- тип экрана: 6.53" (1600x720), HD, IPS- диагональ: 6.53 '
                 'дюйм- размер оперативной памяти: 2 ГБ- технология nfc: нет- '
                 'цвет: голубой- процессор: MediaTek Helio G25- объем '
                 'встроенной памяти: 32 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/32ГБ',
  'name': 'Xiaomi Redmi 9A 2 Glacial Blue ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h07/h52/51359755272222/xiaomi-redmi-9a-2-gb-32-gb-zelenyj-105202550-1.jpg',
  'price': 48990,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-9a-2-gb-32-gb-glacial-blue-goluboi-105202550/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_note',
  'color': 'серый',
  'description': '- тип экрана: цветной AMOLED, сенсорный- диагональ: 6.67 '
                 'дюйм- размер оперативной памяти: 8 ГБ- технология nfc: да- '
                 'цвет: серый- процессор: 8-ядерный Qualcomm Snapdragon 732G- '
                 'объем встроенной памяти: 128 ГБ- емкость аккумулятора: 5020 '
                 'мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Xiaomi Redmi Note 10 Pro 8 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h07/h8f/50628796743710/xiaomi-redmi-note-10-pro-8-gb-128-gb-seryi-101371869-1.png',
  'price': 129618,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-note-10-pro-8-gb-128-gb-seryi-101371869/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_10a',
  'color': 'графит',
  'description': '- тип экрана: IPS- диагональ: 6.53 дюйм- размер оперативной '
                 'памяти: 3 ГБ- технология nfc: нет- цвет: серый- процессор: '
                 'MediaTek Helio G25- объем встроенной памяти: 64 ГБ- емкость '
                 'аккумулятора: 5000 мАч',
  'memory': 'ГБ/64ГБ',
  'name': 'Xiaomi Redmi 10A 3 серый ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h62/he1/52289124302878/xiaomi-redmi-10a-3-gb-64-gb-seryi-grafit-105711712-1.jpg',
  'price': 59990,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-10a-3-gb-64-gb-seryi-grafit-105711712/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_note',
  'color': 'белый',
  'description': '- тип экрана: AMOLED, сенсорный, мультитач- диагональ: 6.67 '
                 'дюйм- размер оперативной памяти: 8 ГБ- технология nfc: да- '
                 'цвет: белый- процессор: 8-ядерный MediaTek Helio G96- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Xiaomi Redmi Note 11 Pro 8 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h4e/h1d/49217235451934/xiaomi-redmi-note-11-pro-8-128gb-seryj-104020427-1.png',
  'price': 139661,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-note-11-pro-8-gb-128-gb-belyi-104020427/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_note',
  'color': 'серый',
  'description': '- тип экрана: AMOLED, сенсорный, мультитач- диагональ: 6.43 '
                 'дюйм- размер оперативной памяти: 6 ГБ- технология nfc: нет- '
                 'цвет: серый- процессор: 8-ядерный Mediatek Helio G96- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Xiaomi Redmi Note 11S 6 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hc2/h11/49414417088542/xiaomi-redmi-note-11s-6-gb-128-gb-seryj-104154272-1.png',
  'price': 118710,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-note-11s-6-gb-128-gb-seryi-104154272/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_note',
  'color': 'серый',
  'description': '- тип экрана: цветной AMOLED, сенсорный- диагональ: 6.67 '
                 'дюйм- размер оперативной памяти: 8 ГБ- технология nfc: да- '
                 'цвет: серый- процессор: 8-ядерный Qualcomm Snapdragon 732G- '
                 'объем встроенной памяти: 256 ГБ- емкость аккумулятора: 5020 '
                 'мАч',
  'memory': 'ГБ/256ГБ',
  'name': 'Xiaomi Redmi Note 10 Pro 8 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h10/he1/64487157628958/xiaomi-redmi-note-10-pro-8-gb-128-gb-seryi-107221005-1.png',
  'price': 142850,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-note-10-pro-8-gb-256-gb-seryi-107221005/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_10',
  'color': 'белый',
  'description': '- тип экрана: сенсорный, мультитач, IPS- диагональ: 6.5 '
                 'дюйм- размер оперативной памяти: 4 ГБ- технология nfc: нет- '
                 'цвет: белый- процессор: MediaTek Helio G88- объем встроенной '
                 'памяти: 128 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Xiaomi Redmi 10 2022 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hf3/h28/51310465286174/xiaomi-redmi-10-2022-4-gb-128-gb-belyj-105170514-1.jpg',
  'price': 89878,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-10-2022-4-gb-128-gb-belyi-105170514/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_10',
  'color': 'голубой',
  'description': '- тип экрана: сенсорный, мультитач, IPS- диагональ: 6.5 '
                 'дюйм- размер оперативной памяти: 4 ГБ- технология nfc: нет- '
                 'цвет: голубой- процессор: MediaTek Helio G88- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Xiaomi Redmi 10 2022 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h78/h65/51310202748958/xiaomi-redmi-10-2022-4-gb-128-gb-goluboj-105170401-1.jpg',
  'price': 89839,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-10-2022-4-gb-128-gb-goluboi-105170401/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_10c',
  'color': 'голубой',
  'description': '- тип экрана: LCD IPS- диагональ: 6.71 дюйм- размер '
                 'оперативной памяти: 4 ГБ- технология nfc: нет- цвет: '
                 'голубой- процессор: 8-ядерный Qualcomm Snapdragon 680- объем '
                 'встроенной памяти: 64 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/64ГБ',
  'name': 'Xiaomi Redmi 10C 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/ha0/hdd/49939924090910/xiaomi-redmi-10c-4-gb-64-gb-goluboj-104417182-1.jpg',
  'price': 68900,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-10c-4-gb-64-gb-goluboi-104417182/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_9a',
  'color': 'зеленый',
  'description': '- тип экрана: сенсорный, мультитач, IPS- диагональ: 6.53 '
                 'дюйм- размер оперативной памяти: 2 ГБ- технология nfc: нет- '
                 'цвет: зеленый- процессор: 8-ядерный MediaTek Helio G25- '
                 'объем встроенной памяти: 32 ГБ- емкость аккумулятора: 5000 '
                 'мАч',
  'memory': 'ГБ/32ГБ',
  'name': 'Xiaomi Redmi 9A 2 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h54/h27/50489568264222/xiaomi-redmi-9a-2-32gb-zelenyj-100436948-1-Container.png',
  'price': 47900,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-9a-2-gb-32-gb-zelenyi-100436948/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_note',
  'color': 'серый',
  'description': '- тип экрана: AMOLED, сенсорный, мультитач- диагональ: 6.43 '
                 'дюйм- размер оперативной памяти: 8 ГБ- технология nfc: нет- '
                 'цвет: серый- процессор: 8-ядерный Mediatek Helio G96- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Xiaomi Redmi Note 11S 8 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h03/hff/49684457062430/xiaomi-redmi-note-11s-6-gb-128-gb-seryj-104292774-1.png',
  'price': 120739,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-note-11s-8-gb-128-gb-seryi-104292774/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_10c',
  'color': 'зеленый',
  'description': '- тип экрана: IPS, сенсорный, мультитач- диагональ: 6.71 '
                 'дюйм- размер оперативной памяти: 4 ГБ- технология nfc: нет- '
                 'цвет: зеленый- процессор: 8-ядерный Qualcomm Snapdragon 680- '
                 'объем встроенной памяти: 64 ГБ- емкость аккумулятора: 5000 '
                 'мАч',
  'memory': 'ГБ/64ГБ',
  'name': 'Xiaomi Redmi 10C 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h7f/h0e/50498249621534/xiaomi-redmi-10c-4-gb-64-gb-zelenyj-104417193-1.png',
  'price': 69890,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-10c-4-gb-64-gb-zelenyi-104417193/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_10a',
  'color': 'голубой',
  'description': '- тип экрана: IPS- диагональ: 6.53 дюйм- размер оперативной '
                 'памяти: 3 ГБ- технология nfc: нет- цвет: голубой- процессор: '
                 'MediaTek Helio G25- объем встроенной памяти: 64 ГБ- емкость '
                 'аккумулятора: 5000 мАч',
  'memory': 'ГБ/64ГБ',
  'name': 'Xiaomi Redmi 10A 3 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hb2/hef/52369629052958/xiaomi-redmi-10a-3-gb-64-gb-goluboj-105545057-1.png',
  'price': 59990,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-10a-3-gb-64-gb-goluboi-105545057/?c=750000000'},
 {'brand': 'xiaomi',
  'call_back': 'xiaomi_redmi_9a',
  'color': 'синий',
  'description': '- тип экрана: сенсорный, мультитач, IPS- диагональ: 6.53 '
                 'дюйм- размер оперативной памяти: 2 ГБ- технология nfc: нет- '
                 'цвет: синий- процессор: 8-ядерный MediaTek Helio G25- объем '
                 'встроенной памяти: 32 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/32ГБ',
  'name': 'Xiaomi Redmi 9A 2 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h38/h4e/50488588828702/xiaomi-redmi-9a-2-32gb-sky-sinij-100399568-1-Container.png',
  'price': 47900,
  'url': 'https://kaspi.kz/shop/p/xiaomi-redmi-9a-2-gb-32-gb-sinii-100399568/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a13',
  'color': 'черный',
  'description': '- тип экрана: PLS TFT LCD- диагональ: 6.6 дюйм- размер '
                 'оперативной памяти: 4 ГБ- технология nfc: да- цвет: черный- '
                 'процессор: 8-ядерный Exynos 850- объем встроенной памяти: 64 '
                 'ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/64ГБ',
  'name': 'Samsung Galaxy A13 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h7c/hdd/49613684899870/smartfon-samsung-galaxy-a13-64gb-sm-a135fzkvskz-black-104253246-1.png',
  'price': 79890,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a13-4-gb-64-gb-chernyi-104253246/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a13',
  'color': 'черный',
  'description': '- тип экрана: PLS TFT LCD сенсорный, мультитач- диагональ: '
                 '6.6 дюйм- размер оперативной памяти: 4 ГБ- технология nfc: '
                 'да- цвет: черный- процессор: 8-ядерный MediaTek MT6833- '
                 'объем встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 '
                 'мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Samsung Galaxy A13 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h06/had/49613711802398/smartfon-samsung-galaxy-a13-128gb-sm-a135fzkkskz-black-104253279-1.png',
  'price': 97955,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a13-4-gb-128-gb-chernyi-104253279/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a03',
  'color': 'черный',
  'description': '- тип экрана: PLS TFT LCD сенсорный, мультитач- диагональ: '
                 '6.5 дюйм- размер оперативной памяти: 2 ГБ- технология nfc: '
                 'нет- цвет: черный- процессор: 8-ядерный Unisoc SC9863A- '
                 'объем встроенной памяти: 32 ГБ- емкость аккумулятора: 5000 '
                 'мАч',
  'memory': 'ГБ/32ГБ',
  'name': 'Samsung Galaxy A03 Core 2 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h7d/hc9/47719147733022/samsung-galaxy-a03-core-2-32gb-cernyj-103153817-1.jpg',
  'price': 48900,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a03-core-2-gb-32-gb-chernyi-103153817/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a23',
  'color': 'черный',
  'description': '- тип экрана: PLS TFT LCD сенсорный, мультитач- диагональ: '
                 '6.6 дюйм- размер оперативной памяти: 6 ГБ- технология nfc: '
                 'да- цвет: черный- процессор: 8-ядерный Snapdragon 680- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Samsung Galaxy A23 6 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hd7/he8/49792685047838/smartfon-samsung-galaxy-a23-sm-a235fzkkskz-128gb-black-104348541-1.jpg',
  'price': 111390,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a23-6-gb-128-gb-chernyi-104348541/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a23',
  'color': 'черный',
  'description': '- тип экрана: PLS TFT LCD сенсорный, мультитач- диагональ: '
                 '6.6 дюйм- размер оперативной памяти: 4 ГБ- технология nfc: '
                 'да- цвет: черный- процессор: 8-ядерный Snapdragon 680- объем '
                 'встроенной памяти: 64 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/64ГБ',
  'name': 'Samsung Galaxy A23 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h25/h55/49797822218270/smartfon-samsung-galaxy-a23-sm-a235fzkuskz-64gb-black-104349419-1.jpg',
  'price': 88980,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a23-4-gb-64-gb-chernyi-104349419/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a53',
  'color': 'черный',
  'description': '- тип экрана: Super AMOLED, сенсорный, мультитач- диагональ: '
                 '6.5 дюйм- размер оперативной памяти: 6 ГБ- технология nfc: '
                 'да- цвет: черный- процессор: 8-ядерный Exynos 1280- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Samsung Galaxy A53 5G 6 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hde/h68/49613532430366/smartfon-samsung-galaxy-a53-5g-128gb-sm-a536ezkdskz-black-104253225-1.png',
  'price': 169850,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a53-5g-6-gb-128-gb-chernyi-104253225/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a33',
  'color': 'черный',
  'description': '- тип экрана: Super AMOLED, сенсорный, Corning Gorilla Glass '
                 '5- диагональ: 6.4 дюйм- размер оперативной памяти: 6 ГБ- '
                 'технология nfc: да- цвет: черный- процессор: 8-ядерный '
                 'Exynos 1280- объем встроенной памяти: 128 ГБ- емкость '
                 'аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Samsung Galaxy A33 5G 6 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h6b/hba/49894747963422/samsung-galaxy-a33-5g-6-gb-128-gb-cernyj-104398547-1.jpg',
  'price': 138700,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a33-5g-6-gb-128-gb-chernyi-104398547/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a13',
  'color': 'голубой',
  'description': '- тип экрана: PLS TFT LCD сенсорный, мультитач- диагональ: '
                 '6.6 дюйм- размер оперативной памяти: 4 ГБ- технология nfc: '
                 'да- цвет: голубой- процессор: 8-ядерный Exynos 850- объем '
                 'встроенной памяти: 64 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/64ГБ',
  'name': 'Samsung Galaxy A13 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hdc/hdb/49613836976158/smartfon-samsung-galaxy-a13-64gb-sm-a135flbvskz-blue-104253442-1.png',
  'price': 79885,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a13-4-gb-64-gb-goluboi-104253442/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a13',
  'color': 'голубой',
  'description': '- тип экрана: PLS TFT LCD сенсорный, мультитач- диагональ: '
                 '6.6 дюйм- размер оперативной памяти: 4 ГБ- технология nfc: '
                 'да- цвет: голубой- процессор: 8-ядерный Exynos 850- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Samsung Galaxy A13 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h8a/h8a/49613817970718/smartfon-samsung-galaxy-a13-128gb-sm-a135flbkskz-blue-104253392-1.png',
  'price': 97345,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a13-4-gb-128-gb-goluboi-104253392/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a13',
  'color': 'белый',
  'description': '- тип экрана: PLS TFT LCD сенсорный, мультитач- диагональ: '
                 '6.6 дюйм- размер оперативной памяти: 4 ГБ- технология nfc: '
                 'да- цвет: белый- процессор: 8-ядерный Exynos 850- объем '
                 'встроенной памяти: 64 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/64ГБ',
  'name': 'Samsung Galaxy A13 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/he8/h71/49613726842910/smartfon-samsung-galaxy-a13-64gb-sm-a135fzwvskz-white-104253316-1.png',
  'price': 79890,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a13-4-gb-64-gb-belyi-104253316/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a53',
  'color': 'черный',
  'description': '- тип экрана: Super AMOLED- диагональ: 6.5 дюйм- размер '
                 'оперативной памяти: 8 ГБ- технология nfc: да- цвет: черный- '
                 'процессор: 8-ядерный Exynos 1280- объем встроенной памяти: '
                 '256 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/256ГБ',
  'name': 'Samsung Galaxy A53 5G 8 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hb4/he2/49613525090334/smartfon-samsung-galaxy-a53-5g-256gb-sm-a536ezkhskz-black-104253200-1.png',
  'price': 196370,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a53-5g-8-gb-256-gb-chernyi-104253200/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a13',
  'color': 'белый',
  'description': '- тип экрана: PLS TFT LCD сенсорный, мультитач- диагональ: '
                 '6.6 дюйм- размер оперативной памяти: 4 ГБ- технология nfc: '
                 'да- цвет: белый- процессор: 8-ядерный Exynos 850- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Samsung Galaxy A13 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h35/h1f/49613741359134/smartfon-samsung-galaxy-a13-128gb-sm-a135fzwkskz-white-104253362-1.png',
  'price': 95095,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a13-4-gb-128-gb-belyi-104253362/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a23',
  'color': 'оранжевый',
  'description': '- тип экрана: PLS TFT LCD сенсорный, мультитач- диагональ: '
                 '6.6 дюйм- размер оперативной памяти: 6 ГБ- технология nfc: '
                 'да- цвет: оранжевый- процессор: 8-ядерный Snapdragon 680- '
                 'объем встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 '
                 'мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Samsung Galaxy A23 6 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h4f/hf7/49792674267166/samsung-galaxy-a23-128gb-peach-104347752-1.jpg',
  'price': 111870,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a23-6-gb-128-gb-oranzhevyi-104347752/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a33',
  'color': 'голубой',
  'description': '- тип экрана: Super AMOLED, сенсорный, Corning Gorilla Glass '
                 '5- диагональ: 6.4 дюйм- размер оперативной памяти: 6 ГБ- '
                 'технология nfc: да- цвет: голубой- процессор: 8-ядерный '
                 'Exynos 1280- объем встроенной памяти: 128 ГБ- емкость '
                 'аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Samsung Galaxy A33 5G 6 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h07/h82/49897401090078/smartfon-samsung-galaxy-a33-5g-128gb-sm-a336blbgskz-blue-104399147-1.png',
  'price': 137990,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a33-5g-6-gb-128-gb-goluboi-104399147/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a23',
  'color': 'белый',
  'description': '- тип экрана: PLS TFT LCD сенсорный, мультитач- диагональ: '
                 '6.6 дюйм- размер оперативной памяти: 6 ГБ- технология nfc: '
                 'да- цвет: белый- процессор: 8-ядерный Snapdragon 680- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Samsung Galaxy A23 6 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h22/hf2/49797805539358/smartfon-samsung-galaxy-a23-sm-a235fzwkskz-128gb-white-104349175-1.jpg',
  'price': 112095,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a23-6-gb-128-gb-belyi-104349175/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a03',
  'color': 'зеленый',
  'description': '- тип экрана: PLS TFT LCD- диагональ: 6.5 дюйм- размер '
                 'оперативной памяти: 2 ГБ- технология nfc: нет- цвет: '
                 'зеленый- процессор: 8-ядерный Unisoc SC9863A- объем '
                 'встроенной памяти: 32 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/32ГБ',
  'name': 'Samsung Galaxy A03 Core 2 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h21/h61/52423990247454/samsung-galaxy-a03-core-2-gb-32-gb-zelenyj-105772575-1.jpg',
  'price': 47580,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a03-core-2-gb-32-gb-zelenyi-105772575/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a03',
  'color': 'медный',
  'description': '- тип экрана: PLS TFT LCD сенсорный, мультитач- диагональ: '
                 '6.5 дюйм- размер оперативной памяти: 2 ГБ- технология nfc: '
                 'нет- цвет: бронзовый- процессор: 8-ядерный Unisoc SC9863A- '
                 'объем встроенной памяти: 32 ГБ- емкость аккумулятора: 5000 '
                 'мАч',
  'memory': 'ГБ/32ГБ',
  'name': 'Samsung Galaxy A03 Core 2 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hde/h01/52423971799070/samsung-galaxy-a03-core-2-gb-32-gb-bronzovyj-105772530-1.jpg',
  'price': 46890,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a03-core-2-gb-32-gb-mednyi-105772530/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a23',
  'color': 'белый',
  'description': '- тип экрана: PLS TFT LCD сенсорный, мультитач- диагональ: '
                 '6.6 дюйм- размер оперативной памяти: 4 ГБ- технология nfc: '
                 'да- цвет: белый- процессор: 8-ядерный Snapdragon 680- объем '
                 'встроенной памяти: 64 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/64ГБ',
  'name': 'Samsung Galaxy A23 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hb2/h45/49797815042078/smartfon-samsung-galaxy-a23-sm-a235fzwuskz-64gb-white-104349332-1.jpg',
  'price': 96413,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a23-4-gb-64-gb-belyi-104349332/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a73',
  'color': 'серый',
  'description': '- тип экрана: Super AMOLED, сенсорный, Corning Gorilla Glass '
                 '5- диагональ: 6.7 дюйм- размер оперативной памяти: 8 ГБ- '
                 'технология nfc: да- цвет: серый- процессор: 8-ядерный '
                 'Snapdragon 778G- объем встроенной памяти: 256 ГБ- емкость '
                 'аккумулятора: 5000 мАч',
  'memory': 'ГБ/256ГБ',
  'name': 'Samsung Galaxy A73 5G 8 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h9a/hd9/50197108916254/samsung-galaxy-a73-5g-8-gb-256-gb-seryi-104545951-1.png',
  'price': 250607,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a73-5g-8-gb-256-gb-seryi-104545951/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a33',
  'color': 'белый',
  'description': '- тип экрана: Super AMOLED- диагональ: 6.4 дюйм- размер '
                 'оперативной памяти: 6 ГБ- технология nfc: да- цвет: белый- '
                 'процессор: 8-ядерный Exynos 1280- объем встроенной памяти: '
                 '128 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Samsung Galaxy A33 5G 6 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h73/hca/49955530145822/samsung-galaxy-a33-5g-6-128gb-belyj-104424593-1.jpg',
  'price': 138760,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a33-5g-6-gb-128-gb-belyi-104424593/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a53',
  'color': 'белый',
  'description': '- тип экрана: Super AMOLED, сенсорный, мультитач- диагональ: '
                 '6.5 дюйм- размер оперативной памяти: 6 ГБ- технология nfc: '
                 'да- цвет: белый- процессор: 8-ядерный Exynos 1280- объем '
                 'встроенной памяти: 128 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Samsung Galaxy A53 5G 6 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h8f/h2f/49670964019230/smartfon-samsung-galaxy-a53-5g-128gb-sm-a536ezwdskz-white-104283613-1.jpg',
  'price': 169980,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a53-5g-6-gb-128-gb-belyi-104283613/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_a03_4',
  'color': 'черный',
  'description': '- тип экрана: PLS TFT LCD- диагональ: 6.5 дюйм- размер '
                 'оперативной памяти: 4 ГБ- технология nfc: нет- цвет: черный- '
                 'процессор: 8-ядерный Unisoc Tiger T606- объем встроенной '
                 'памяти: 64 ГБ- емкость аккумулятора: 5000 мАч',
  'memory': 'ГБ/64ГБ',
  'name': 'Samsung A03 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hf3/h63/48617931014174/samsung-a03-4-gb-64-gb-cernyj-103623441-1.jpg',
  'price': 74850,
  'url': 'https://kaspi.kz/shop/p/samsung-a03-4-gb-64-gb-chernyi-103623441/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a23',
  'color': 'оранжевый',
  'description': '- тип экрана: PLS TFT LCD сенсорный, мультитач- диагональ: '
                 '6.6 дюйм- размер оперативной памяти: 4 ГБ- технология nfc: '
                 'да- цвет: оранжевый- процессор: 8-ядерный Snapdragon 680- '
                 'объем встроенной памяти: 64 ГБ- емкость аккумулятора: 5000 '
                 'мАч',
  'memory': 'ГБ/64ГБ',
  'name': 'Samsung Galaxy A23 4 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/ha3/hf4/49797836308510/smartfon-samsung-galaxy-a23-sm-a235fzouskz-64gb-peach-104349486-1.jpg',
  'price': 88760,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a23-4-gb-64-gb-oranzhevyi-104349486/?c=750000000'},
 {'brand': 'samsung',
  'call_back': 'samsung_galaxy_a73',
  'color': 'серый',
  'description': '- тип экрана: Super AMOLED, сенсорный, Corning Gorilla Glass '
                 '5- диагональ: 6.7 дюйм- размер оперативной памяти: 6 ГБ- '
                 'технология nfc: да- цвет: серый- процессор: 8-ядерный '
                 'Snapdragon 778G- объем встроенной памяти: 128 ГБ- емкость '
                 'аккумулятора: 5000 мАч',
  'memory': 'ГБ/128ГБ',
  'name': 'Samsung Galaxy A73 5G 6 ',
  'photo': 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h94/hec/50197108621342/samsung-galaxy-a73-5g-6-gb-128-gb-seryi-104545794-1.png',
  'price': 207250,
  'url': 'https://kaspi.kz/shop/p/samsung-galaxy-a73-5g-6-gb-128-gb-seryi-104545794/?c=750000000'}]

add_products_db(items=data)




