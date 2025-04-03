from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r"присв\w* адрес\w* ?(дом\w*|объек\w*|зу|земельн\*|участк\w*)?", "66"),
    # (r"присвоение адреса дому|(присв\w*|аннулир\w*|анулир\w*|) адреc\w* ?(объек\w*|дом\w*|зу)?", "66"),
    # (r"(присв\w*|аннулир\w*|анулир\w*|) адреc\w* ?(объек\w*|дом\w*|зу)? ?(адресации)?", "66"),

]


test_phrases = [
    "присвоение адреса дому",
    "Присвоение адреса ЗУ",
    "Присвоение адреса",
    "Присвоение адреса земельному участку",

]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
