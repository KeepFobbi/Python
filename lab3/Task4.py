def arreck(move):
    if len(move) != 5:
        return 'ERROR'
    arr = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    try:
        src, dst = move.split('-')
        if all([int(src[1]) % 9, int(dst[1]) % 9]):
            try:
                result = '{0}{1}'.format(abs(arr[src[0]] - arr[dst[0]]), abs(int(src[1]) - int(dst[1])))
                if result in ('12', '21'):
                    return 'YES'
                return 'NO'
            except KeyError:
                return 'ERROR'
        return 'ERROR'
    except ValueError:
        return 'ERROR'

with open('INPUT4.txt', 'r') as fin:
    with open('OUTPUT4.txt', 'w') as fout:
        fout.write(arreck(fin.readline()[:-1]))
