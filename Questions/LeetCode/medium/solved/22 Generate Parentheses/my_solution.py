def generateParenthesis(self, n: int) -> List[str]:
    all_paths = []

    def get_all_paranthesis(s, n1, n2):
        if n1 == 0:
            if n2 == 0:
                all_paths.append(s)
            else:
                get_all_paranthesis(s + ")", n1, n2 - 1)
        elif n1 == n2:
            get_all_paranthesis(s + "(", n1 - 1, n2)
        elif n1 < n2:
            get_all_paranthesis(s + "(", n1 - 1, n2)
            get_all_paranthesis(s + ")", n1, n2 - 1)

    get_all_paranthesis("", n, n)
    return all_paths