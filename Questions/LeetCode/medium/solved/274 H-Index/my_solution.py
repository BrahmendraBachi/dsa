def hIndex(citations):
    n = len(citations)
    if n == 1:
        return 1 if citations[0] > 0 else 0
    citations.sort()

    for i in range(n):
        cite = citations[i]
        n_papers = n - i
        if n_papers <= cite:
            return n_papers
    return 0
