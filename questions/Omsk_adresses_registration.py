from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r'присвоение адресов|аннулирование адресов|адресов объектам адресации|присв\w* адрес\w* (дом\w*|зу)', '66'),

]


test_phrases = [
    "присвоение адреса зу",
    "присвоение адреса дому",
]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
