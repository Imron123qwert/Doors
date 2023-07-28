from googletrans import Translator

# norwegian : "no"
# turkish : "tr"
# chinese (simplified) : "zh-cn"
# indonesian : "id"

tran = Translator()

async def translate_user_text(text, to_lang):
    text = tran.translate(text=text, dest=to_lang)
    return text.text
