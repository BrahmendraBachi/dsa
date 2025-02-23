def repeatedCharacter(s: str) -> str:
    let_counts = set([])
    for i in s:
        if i in let_counts:
            return i
        let_counts.add(i)
