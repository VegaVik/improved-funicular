from turtle import right
from google_images_search import GoogleImagesSearch
import config

gis = GoogleImagesSearch(config.DEV_API_KEY, config.PROGECT_CX)

_search_params = {
    # Строка запроса
    'q': 'Rebbeca CyberPunk',
    # Кол-во запрошенных картинок
    'num': 15,
    'fileType': 'png|jpg',
    # Поиск по провам на картинку
    # 'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
    # 'safe': 'active|high|medium|off|safeUndefined', ##
    # 'imgType': 'clipart|face|lineart|stock|photo|animated|imgTypeUndefined', ##
    # 'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge|imgSizeUndefined', ##
    # 'imgDominantColor': 'black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow|imgDominantColorUndefined', ##
    # 'imgColorType': 'color|gray|mono|trans|imgColorTypeUndefined' ##
}

# Только поиск 
# gis.search(search_params=_search_params)

# Поиск и загрузка
gis.search(search_params=_search_params, path_to_dir='D:\Python\TelegramBot\images')

# Поиск, загрузка, изменение размера
# gis.search(search_params=_search_params, path_to_dir='/path/', width=500, height=500)