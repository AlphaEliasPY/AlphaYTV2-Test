class Presets(object):
    HELP_TEXT = """
envíe cualquier imagen para configurar una miniatura personalizada permanente para los videos.

Para eliminar la miniatura personalizada previamente guardada, seleccione en opciones. 
Si no hay miniaturas personalizadas disponibles, el bot colocará las miniaturas predeterminadas de YouTube para los videos, buscará la instalación en línea o pegará el enlace de YouTube para comenzar a descargar

𝐉𝐨𝐢𝐧 <a href='https://t.me/AndroidCave'>𝐔𝐩𝐝𝐚𝐭𝐞𝐬</a> | 𝐑𝐞𝐩𝐨 <a href='https://github.com/AlphaEliasPY/AlphaYT'>𝐋𝐈𝐍𝐊</a>   
    """
    WELCOME_MSG = "Hola ... {} \nPuedo descargar videos de YouTube. \nBuscar en línea: seleccionar y descarga."
    OPTIONS_TXT = "Puedo descargar videos de YouTube. \nBuscar en línea: seleccionar y descargar."
    RESULTS_TXT = "👀 Resultados:"
    NO_RESULTS = "❌ No Hay Resultados:"
    DESCRIPTION = "Duracon: {} || {}"
    NOT_AUTH_TXT = "❌ ❌ No estas autorizado ❌ ❌"
    DEFAULT_TITLE = "Repo de YouTube downloader "
    DEFAULT_THUMB_URL = "https://image.flaticon.com/icons/png/512/25/25231.png"
    DEFAULT_LINK = "https://github.com/AlphaEliasPY/AlphaYT"
    DEFAULT_DESCRIPTION = "Link: aAlphaEliasPY | GitHub"
    DEV_TITLE = "Contacto con el Desarrolador"
    DEV_THUMB_URL = "https://freepikpsd.com/media/2019/10/software-developer-icon-png-2-Transparent-Images.png"
    DEV_LINK = "https://t.me/AlphaElias"
    DEV_DESCRIPTION = "Name: ⚡️𝔼𝕝 𝔹𝕣𝕠𝕞𝕒𝕤⚡️[𝙿𝙼=🚫] | Telegram"
    SHARE_BUTTON_TEXT = "Hola... 👋 \nCheckout: @{username}\nPara buscar y descargar videos de YouTube"
    SAVED_THUMB = "<b>✅ Miniatura guardada correctamente</b>\n<code>Este archivo se utilizará en el próximo archivo de YouTube " \
                  "que descargues hasta que lo borres !</code> "
    WAIT_MESSAGE = "Por Favor Espere.. 4 segundos !"
    THUMB_CAPTION = "<code>Esta imagen es tu miniatura actual, toca </code><b> DEL THUMB </b><code> Si quieres " \
                    "Limpiarlo !</code> "
    NO_THUMB = "No hay miniaturas en su directorio local, cargue una imagen para guardarla !"
    DEL_THUMB_CNF = "Miniatura Borrada Correctamente ✅"
    LINK_ERROR = "ocurrieron algunos errores en el proceso !\nPor favor, inténtelo de nuevo más tarde.."
    #
    #
    #
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    FINISHED_PROGRESS_STR = "◼️"
    UN_FINISHED_PROGRESS_STR = "◻️"
    CHECKING_LINK = "⏳ Espere por favor... ⏳"
    DOWNLOAD_START = "Descargando ... Por favor espere !"
    UPLOAD_START = "Subiendo a Telegram..."
    NOT_DOWNLOADABLE = "URL No Descargable !"
    CANCEL_PROCESS = "<b>Proceso cancelado con éxito</b>  ✅"
    SEND_TEXT = "<b>Procesando...</b>\n<i>Este mensaje desaparecerá automáticamente cuando finalice la transmisión.</i> "
    REPLY_ERROR = "<i>Utilice este comando como respuesta a cualquier mensaje de telegram sin espacios.</i>"
    USERS_LIST = "<b>Total: {}</b>\n\nSuscriptores - {}\nBloqueado / Eliminado - {}"
    WAIT_MSG = "<b>Procesando...</b>\n<i>Esto tomará algún tiempo...</i>"
    PROMPT_THUMB = "<b>¿Quieres configurar esta imagen como miniatura?</b>"
    FORMAT_SELECTION = """
<b>Titulo -</b> {}
<b>Canal -</b> <a href={}>{}</a>
<b>Subido en -</b> {}
<b>Vistas -</b> {}  |  <b>Clasificación:</b> {}

<b>Seleccione el formato deseado:</b>
    """
    SET_CUSTOM_USERNAME_PASSWORD = """Si desea descargar videos premium, proporcione en el siguiente formato:
URL | nuevo nombre de archivo | nombre de usuario | contraseña"""
    CUSTOM_CAPTION_UL_FILE = "\xad \xad\n<code>{}</code>\n\n<b>Creditos- </b><b><a href='https://t.me/AndroidCave'>@AlphaElias</a></b>"
    RCHD_TG_API_LIMIT = "Tamaño de archivo detectado: {}\nPerdón. Pero no puedo subir archivos " \
                        "más de 1,95 GB debido a las limitaciones de la API de Telegram."
    AD_STRING_TO_REPLACE = "Informe este problema en https://yt-dl.org/bug. Asegúrate de estar usando el " \
                           "ultima versión; consulte https://yt-dl.org/update sobre cómo actualizar. Asegúrate de llamar " \
                           "youtube-dl con el indicador --verbose e incluye su salida completa."
