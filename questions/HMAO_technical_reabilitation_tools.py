# -*-coding=utf-8-*-


from utilities.regexp_check_with_query import check_regexp_with_queries

common_regular_exp = r"(как|что|какое|какой)? ?(можно|нужно|мне|необ\w*|обяз\w*)? ?(\w*делать|нужно|порядок)? ?(для|чтобы)? ?(оформ\w*|\w*делать|получ\w*|заказ\w*|\w*готов\w*)"
QUESTIONS = [
    (common_regular_exp+r"? ?(тср|тэ сэ эр|тэ се эр|те се эр)? ?(техн\w*)? ?сред\w* реаб\w* ?(для)? ?(инвал\w*)?", "210"),

]


test_phrases = [
    "как оформить тср технические средства реабилитации",
    "оформить тср технические средства реабилитации",
    "тср технические средства реабилитации",
    "технические средства реабилитации",
    "средства реабилитации",
    "средства реабилитации для инвалида",

]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
