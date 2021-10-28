# Игра Реверси
В игре используется квадратная доска размером 8 × 8 клеток (все клетки могут быть одного цвета) и 64 специальные фишки, окрашенные с разных сторон в контрастные цвета, например, в белый и чёрный. Клетки доски нумеруются от верхнего левого угла: вертикали — латинскими буквами, горизонтали — цифрами (по сути дела, можно использовать шахматную доску). Один из игроков играет белыми, другой — чёрными. Делая ход, игрок ставит фишку на клетку доски «своим» цветом вверх.

В начале игры в центр доски выставляются 4 фишки: чёрные на d5 и e4, белые на d4 и e5.

Первый ход делают чёрные. Далее игроки ходят по очереди.

Делая ход, игрок должен поставить свою фишку на одну из клеток доски таким образом, чтобы между этой поставленной фишкой и одной из имеющихся уже на доске фишек его цвета находился непрерывный ряд фишек соперника, горизонтальный, вертикальный или диагональный (другими словами, чтобы непрерывный ряд фишек соперника оказался «закрыт» фишками игрока с двух сторон). Все фишки соперника, входящие в «закрытый» на этом ходу ряд, переворачиваются на другую сторону (меняют цвет) и переходят к ходившему игроку.

Если в результате одного хода «закрывается» одновременно более одного ряда фишек противника, то переворачиваются все фишки, оказавшиеся на всех «закрытых» рядах.

Игрок вправе выбирать любой из возможных для него ходов. Если игрок имеет возможные ходы, он не может отказаться от хода. Если игрок не имеет допустимых ходов, то ход передаётся сопернику.

Игра прекращается, когда на доску выставлены все фишки или когда ни один из игроков не может сделать хода. По окончании игры проводится подсчёт фишек каждого цвета, и игрок, чьих фишек на доске выставлено больше, объявляется победителем. В случае равенства количества фишек засчитывается ничья.

ТЗ:
  
При входе в программу должно будет открываться окно с игрой. Игра начнется после нажатия на кнопку «Новая игра» и выбора во всплывающем окне режима игры. Если хотите сыграть вдвоем за одним компьютером друг против друга, то нужно нажать на виджет кнопки «Играть вдвоём» в этом окне. Если нужно сыграть с компьютером, то нажмите на кнопку «Играть с компьютером». Если игра уже была начата, то это кнопка остановит игру и после этого появится, то же окно, как и при запуске игры с первого раза. Кнопка с новой игрой будет находиться слева.

Кнопка с настройками будет находиться справа. В ней можно будет очистить кэш программы(Удалить базу данных). Также в ней будет информация о программе и Имя фамилия создателя. В настройках можно будет выбрать как вас будут звать во время игры. Длина имени ограничивается 16 символами

В середине будет показан счёт. В случае игры вдвоём игроки будут называться Игрок1 и Игрок2. Если играть с компьютером, то вместо Игрок1 будет просто Игрок, а вместо Игрок2 Компьютер. Считать программа будет количество фигур того цвета, которое соответствует каждому из игроков.

При игре можно будет откатывать ходы назад, для этого будет специальная кнопка cо знаком «←» над игровым полем. Если вы решили передумать, то можете вернуть откатанные ходы обратно, если перед этим не совершали никаких действий. Для этого будет кнопка со знаком «→»

Кнопка сдаться При игре с компьютером приведет к автоматическому поражению игрока, а при игре вдвоём — проиграет человек, чей сейчас ход.

В игровом поле будет 64 кнопки, изначально они расположены квадратно 8 на 8. Все они окрашены в зелёный цвет. При начале игры на кнопках на 4 строке и 4 столбце, а также на 5 строке и 5 столбце появится изображение белой фигуры. На 4 строке 5 столбце и 5 строке 4 столбце появится изображение черного круга. Изначально они окрашены в зелёный цвет, а при наведении они будут окрашиваться в желтый с появлением кортики круга, если можно по правилам сделать ход.

В игры можно будет посмотреть результаты последних игр. Для жатого будет кнопка «Результаты игр» при нажатии на которую будет осуществляться запрос к базе данных и показываться в отдельном окне: дата начала/окончания мачта, время игры, первый игрок, второй игрок(или компьютер), а также их счет и имя победителя.
