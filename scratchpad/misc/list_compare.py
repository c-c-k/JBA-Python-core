with open('/dev/shm/tmp1', 'r') as f:
    target = [8, 19, 12, 7, 6, 5]
    data = [
        [
            int(x)
            for x
            in line
        ]
        for line
        in (
            line.strip().split(',')
            for line
            in f
        )
    ]


    def count(_line: list[int]) -> int:
        _count = 0
        for i in target:
            for j in _line:
                _count += 1
                if i == j:
                    break
        return _count


    data.sort(key=count)
    counts = [(count(entry), entry) for entry in data]

    print(*counts, sep='\n')
