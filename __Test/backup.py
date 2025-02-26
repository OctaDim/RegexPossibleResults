import re


QUESTIONS = [
    (r"адреса? мфц", "0.0"),
    (r'адреса? мфц|режимы? работы мфц|адреса? офис(ов|а) мфц|режимы? работы офис(ов|а)', '1', (
        (r'област', '1.2', (
            (r'азовск', '1.2.1'),
            (r'большереченск', '1.2.2'),
            (r'большеуковск', '1.2.3'),
            (r'горьковск', '1.2.4'),
            (r'знаменск', '1.2.5'),
            (r'исилькульск', '1.2.6'),
            (r'калачинск', '1.2.7'),
            (r'колосовск', '1.2.8'),
            (r'кормиловск', '1.2.9'),
            (r'крутинск', '1.2.10'),
            (r'любинск', '1.2.11'),
            (r'марьяновск', '1.2.12'),
            (r'москаленск', '1.2.13'),
            (r'муромцевск', '1.2.14'),
            (r'называевск', '1.2.15'),
            (r'нижнеомск', '1.2.16'),
            (r'нововаршавск', '1.2.17'),
            (r'одесск', '1.2.18'),
            (r'оконешниковск', '1.2.19'),
            (r'омск', '1.2.20'),
            (r'павлоградск', '1.2.21'),
            (r'полтавск', '1.2.22'),
            (r'русско[- ]полянск', '1.2.23'),
            (r'саргатск', '1.2.24'),
            (r'седельниковск', '1.2.25'),
            (r'таврическ', '1.2.26'),
            (r'тарск', '1.2.27'),
            (r'тевризск', '1.2.28'),
            (r'тюкалинск', '1.2.29'),
            (r'усть[- ]ишимск', '1.2.30'),
            (r'черлакск', '1.2.31'),
            (r'шербакульск', '1.2.32'),
        )),
        (r'город|омск\b', '1.1', (
            (r'центр', '1.1.1'),
            (r'киров', '1.1.2'),
            (r'октябрь', '1.1.3'),
            (r'ленин', '1.1.4'),
            (r'совет', '1.1.5'),
        )),
    )),
    # (r"(измен\w*|друг\w*|в связи с изменен\w*) (фамили\w*|им\w*|отчеств\w*|данн\w*) (пасп[оа]рт|в пасп[оа]рте) ?(как|как можно|как мне)? ?(заменить|сделать|получить|заказать|оформить)? ?(новый)?", "0.0"),
    # (r"(измен\w*|друг\w*|в связи с изменен\w*) (фамили\w*|им\w*|отчеств\w*|данн\w*) ?(как|ка1к можно|как мне)? ?(заменить|сделать|получить|заказать|оформить)? ?(новый)? ?(пасп[оа]рт|в пасп[оа]рте)", "0.0"),
    # (r"(фамили\w*|им\w*|отчеств\w*|данн\w*) (измен\w*|друг\w*|в связи с изменен\w*) (пасп[оа]рт|в пасп[оа]рте) ?(как|как можно|как мне)? ?(заменить|сделать|получить|заказать|оформить)? ?(новый)?", "0.0"),
    # (r"(фамили\w*|им\w*|отчеств\w*|данн\w*) (измен\w*|друг\w*|в связи с изменен\w*) ?(как|как можно|как мне)? ?(заменить|сделать|получить|заказать|оформить)? ?(новый)? ?(пасп[оа]рт|в пасп[оа]рте)", "0.0"),
    # (r"(как|как можно)? ?(заменить|сделать|получить|заказать|оформить)? ?(новый)? ?(пасп[оа]рт|в пасп[оа]рте) (измен\w*|друг\w*|в связи с изменен\w*) (фамили\w*|им\w*|отчеств\w*|данн\w*)", "0.0"),
]

test_phrases = [
    # "test",
    "азовск",
    # "водительское удостоверение",
    # "конец срока"
    # "изменил имя паспорт",
    # "фамилию изменил в паспорте",
    # "как заменить паспорт изменилось отчество",
    # "изменилась фамилия паспорт",
    # "изменились данные паспорт новый",
]

# subq = ()
# subsubq = ()

for test_phrase in test_phrases:
    for q in QUESTIONS:
        subquestions = None
        subsubquestions = None

        if re.search(q[0], test_phrase, flags=re.U):
            print(f"Test Phrase: {test_phrase}\n"
                  f"Regular Expression: {q}\n"
                  f"Result: Base Question - OK ✅ \n"
                  f"len(q): {len(q)}\n"
                  f"Action: Playback q[1]\n\n")
            continue
        else:
            print(f"Test Phrase: {test_phrase}\n"
                  f"Regular Expression: {q}\n"
                  f"len(q): {len(q)}\n"
                  f"Result: NOT FOUND IN QUESTION!!! 🚫\n\n")

        if len(q) == 3:
            subquestions = q[2]
            # print(f"Regular Sub Expression: {subquestions}")

        if subquestions:
            for subq in subquestions:  # Sub questions in q[2]
                if re.search(subq[0], test_phrase, flags=re.U):
                    print(f"Test Phrase: {test_phrase}\n"
                          f"Regular Sub Expression: {subq}\n"
                          f"Result: Sub Question - OK ✅✅ \n"
                          f"len(subq): {len(subq)}\n"
                          f"Action: Play sub_q[1] \n\n")
                    continue
                else:
                    print(f"Test Phrase: {test_phrase}\n"
                          f"Regular Sub Expression: {subq}\n"
                          f"len(subq): {len(subq)}\n"
                          f"Result: NOT FOUND IN SUB QUESTION!!! 🚫🚫\n\n")

                if len(subq) == 3:
                    subsubquestions = subq[2]
                    # print(f"Regular Sub Sub Expression: {subsubquestions}")

                if subsubquestions:
                    for subsubq in subsubquestions:  # Sub sub questions in q[2]
                        if re.search(subsubq[0], test_phrase, flags=re.U):
                            found_flag = True
                            print(f"Test Phrase: {test_phrase}\n"
                                  f"Regular Expression: {q}\n"
                                  f"Result: Sub Sub Question - OK ✅✅✅ \n"
                                  f"len(subsubq): {len(subsubq)}\n"
                                  f"Action: Play sub_sub_q[1] \n\n")
                            continue
                        else:
                            print(f"Test Phrase: {test_phrase}\n"
                                  f"Regular Sub Sub Expression: {subq}\n"
                                  f"len(subsubq): {len(subsubq)}\n"
                                  f"Result: NOT FOUND IN SUB SUB QUESTION!!! 🚫🚫🚫\n\n")
