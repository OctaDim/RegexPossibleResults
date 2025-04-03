# -*-coding=utf-8-*-


from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r"xxx", "0"),
    # (r"(незачем)|((мне)? ?(это)? ?не (интер\w*|нужн\w*|над|хоч\w*|зачем))", "0.0"),
    (r"нет|не|не (нужн\w*|над\w*|трэба)|пропус\w*|отказ\w*|отбой|(незачем)|((мне)? ?(это)? ?не (интер\w*|нужн\w*|над|хоч\w*|зачем))", "0.0")
]


test_phrases = [
    "незачем",
    "не надо",
    "не нужно",
    "не зачем",
    "мне не зачем",
    "мне это не нужно",
    "этот счетчик не нужно"
]


test_phrases_additional = [
    "надо",
    "нужно",
    "зачем",
    "мне зачем",
]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
