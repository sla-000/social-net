for q in range(0, 70):
    for q2 in range(0, 70):
        print("\t\t{")
        print('\t\t\t"nick": "Nick-{}-{}",'.format(q, q2))
        print('\t\t\t"name": "Name-{}-{}",'.format(q, q2))
        print('\t\t\t"surname": "Surname-{}-{}",'.format(q, q2))
        print('\t\t\t"position": "Position-{}-{}",'.format(q, q2))
        print('\t\t\t"photo": "https://www.fillmurray.com/{}/{}"'.format(q + 200, q2 + 200))
        print("\t\t},")

        # {
        #     "nick": "Nick1",
        #     "name": "Name1",
        #     "surname": "Surname1",
        #     "position": "Position1",
        #     "photo": "https://www.fillmurray.com/200/300"
        # },