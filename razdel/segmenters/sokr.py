

def parse_sokrs(lines):
    for line in lines:
        for word in line.split():
            yield word


def parse_pair_sokrs(lines):
    for line in lines:
        yield tuple(line.split())


TAIL_SOKRS = set(parse_sokrs([
    'дес тыс млн млрд',
    'дол долл',
    'коп руб р',
    'проц',  # 95 проц. акций,

    'га',
    'барр',  # 40 долларов за барр.
    'куб',  # 1000 куб. метр.
    'кв км',  # 700 тыс. кв. км.
    'см',  # 30 см

    'час мин сек',  # в 15 час. 13 мин. 53 сек.
    'в вв',  # XII в. XVIII—XIX вв.
    'г гг',  # 1996-1999гг

    'с стр',  # 287 стр.

    'co corp inc',

    'изд ed',  # 1-е изд. Arthur W. Hummel, ed. Eminent Chinese

    'др',  # и другие
    'al',  # North et al.
]))

HEAD_SOKRS = set(parse_sokrs([
    'букв',  # яп. 18禁, букв. «запрещено
    'ст',  # ст.-слав.
    'трад',  # кит. трад
    'лат венг исп кат укр нем англ фр итал греч',
    'евр араб яп слав кит рус русск латв',
    'словацк хорв',

    'mr mrs ms dr vs',
    'св',  # св.Иоанна
    'арх зав зам проф акад',
    'кн',  # кандидат наук
    'корр',  # сообщил корр. ИТАР-ТАСС
    'ред',  # Под ред. Линды Уильямс
    'гр',  # гр. Валевской
    'ср',  # Ср. L. Ross
    'чл корр',  # является чл.-корр. АН СССР
    'им',  # им. Вс. Мейерхольда
    'тов',  # тюремном подвале тов. Берия

    'нач пол',  # нач. XX века

    'chap',
    'п пп ст ч чч гл стр абз пт',  # ст. 129 ч. 2 п. 8 Гл. VI
    'no',  # No. 6

    'просп пр ул ш г гор д стр к корп пер корп обл эт пом ауд оф ком комн каб',
    'домовлад лит',
    'т',  # т. 1 л.д. 85-89
    'рп пос с х',  # х. Ново-Максимовский, с. Кляшево рп.Раздолинск
    'пл',  # площадь
    'bd',  # Bd. 16, Berlin
    'о оз',  # Вблизи оз. Селяха
    'р',  # р. Иордан
    'а',  # а. Адыге-Хабль

    'обр',  # обр. 1936 г.
    'ум',  # ум. 1064
    'ок',  # "родилась ок. 1211", "работают ок. 150 специалистов"
    'откр',  # Откр. 20:40

    'пс ps',
    'upd',
    'см',
    'напр',  # UNIX-семейства, напр. Linux, FreeBSD
    'доп',

    'юр физ',  # юр. адрес

    'тел',
    'сб',  # Сб. «Киноварь»
    'внутр',  # к внутр. миру героев
    'дифф',  # мне по дифф. зачёту «5» поставил
    'гос',  # гос. экзамены
    'отм',  # от отм. 0.000
]))

OTHER_SOKRS = set(parse_sokrs([
    'сокр рис искл прим',

    'яз',
    'устар',  # пометкой "устар."
    'шутл',  # "в стиле шутл.", "bones — шутл. человек"
]))

SOKRS = TAIL_SOKRS | HEAD_SOKRS | OTHER_SOKRS

TAIL_PAIR_SOKRS = set(parse_pair_sokrs([
    'т п',
    'т д',
    'у е',
    'н э',
    'p m',
    'a m',
    'с г',  # от 18 мая с. г.
    'р х',  # 250 года до Р. Х.
    'с г',  # 18 мая с. г.
    'с ш',  # 50°13′ с. ш.
    'з д',  # 12°48′ з. д.
    'л с',
    'ч т', 'т д',  # ч.т.д
]))

HEAD_PAIR_SOKRS = set(parse_pair_sokrs([
    'т е',
    'т к',
    'т н',
    'и о',
    'к н',
    'к п', 'п н',  # к.п.н
    'к т', 'т н',  # к.т.н
    'л д',  # т. 1 л.д. 85-89
]))

OTHER_PAIR_SOKRS = set(parse_pair_sokrs([
    'ед ч',
    'мн ч',
    'повел накл',  # в 1 лице мн. ч. повел. накл.
    'жен р'
    'муж р',
]))

PAIR_SOKRS = TAIL_PAIR_SOKRS | HEAD_PAIR_SOKRS | OTHER_PAIR_SOKRS

INITIALS = {
    'дж',
    'ed',
    'вс',  # Вс. Мейерхольда
}
