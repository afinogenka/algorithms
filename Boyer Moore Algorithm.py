import timeit


def boyer_alg(txt, pat):
    # create shift table
    s = set()
    dictionary = {}

    for i in range(len(pat)-2, -1, -1):
        if pat[i] not in s:
            dictionary[pat[i]] = len(pat) - i - 1
            s.add(pat[i])
    if pat[len(pat)-1] not in s:
        dictionary[pat[len(pat)-1]] = len(pat)

    dictionary['*'] = len(pat)

    # print('dictionary', dictionary)

    # find sub sring in string

    if len(txt) >= len(pat):
        i = len(pat) - 1

        while i < len(txt):
            k = 0
            j = 0
            for j in range(len(pat) - 1, -1, -1):
                if txt[i-k] != pat[j]:
                    if j == len(pat) - 1:
                        shift = dictionary[txt[i]] if dictionary.get(txt[i], False) else \
                            dictionary['*']
                    else:
                        shift = dictionary[pat[j]]

                    i += shift
                    break
                k += 1

            if j == 0:
                print(f'Pattern is found at index {i-k+1}')

                break
        else:
            print('Pattern is NOT found ')
    else:
        print('Pattern is NOT found ')


def main():
    text = input('Enter text: ')
    pattern = input('Enter pattern to find: ')
    case = input('Sensitivity to Upper case Y/N?').upper()

    if case != "Y":
        text = text.lower()
        pattern = pattern.lower()

    boyer_alg(text, pattern)
    t1 = timeit.timeit(lambda: boyer_alg(text, pattern), number=1)
    t2 = timeit.timeit(lambda: text.find(pattern), number=1)
    print(f'Search with boyer alg took {t1} seconds')
    print(f'Build in search took {t2} seconds')


if __name__ == '__main__':
    main()
