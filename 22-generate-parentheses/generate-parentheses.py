class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [], []

        def backtrack(n_open, n_close):
            if len(sol) == 2*n:
                ans.append("".join(sol))
                return

            if n_open < n:
                sol.append("(")
                backtrack(n_open+1, n_close)
                sol.pop()

            if n_open > n_close:
                sol.append(")")
                backtrack(n_open, n_close+1)
                sol.pop()

        backtrack(0,0)
        return ans



        