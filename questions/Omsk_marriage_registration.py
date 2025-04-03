from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r"(заключ\w*|зарег\w*|оформ\w*|регистр\w*) брак\w*|государственная регистрация брака", '58'),
    (r'расторжение брака|по взаимному согласию супругов|не имеющих общих детей|не достигших совершеннолетия|государственная регистрация расторжения брака', '59'),
]

test_phrases = [

]

test_phrases_additional = [
    "Заключение брака",
    "Зарегистрировать брак",
    "Оформить брак",
    "Регистрация брака",
]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
