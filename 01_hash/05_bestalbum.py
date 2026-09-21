def solution(genres, plays):

    answer = []
    genres_dic = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        # print(i, g, p)

        if g not in genres_dic:
            genres_dic[g] = []
            genres_dic[g].append((p, i))
        else:
            genres_dic[g].append((p, i))

    genre_total = {}
    for g, songs in genres_dic.items():
        # print(g, songs)
        for num, i in songs:
            # print(num)
            if g not in genre_total:
                genre_total[g] = 0
            genre_total[g] += num

    print(genre_total)

    sorted_genres = sorted(genre_total, key=lambda g: genre_total[g], reverse = True)

    print(sorted_genres)    

    for g in sorted_genres:
        # print(g)
        print(genres_dic)
        a = sorted(genres_dic[g], key=lambda x: x[0], reverse=True)[:2]
        print(a)
        for num, i in a:
            answer.append(i)
    
    return answer


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop", "pop", "classic"]
    plays = [500, 600, 150, 800, 2500, 1600, 2000]
    print(solution(genres, plays))  # Expected output: [4, 1, 3, 0]