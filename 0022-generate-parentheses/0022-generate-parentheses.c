void backtrack(char **result, int *returnSize, char *current, int open, int close, int n, int pos) {
    if (pos == 2 * n) {
        current[pos] = '\0';
        result[*returnSize] = (char *)malloc((2 * n + 1) * sizeof(char));
        strcpy(result[*returnSize], current);
        (*returnSize)++;
        return;
    }

    if (open < n) {
        current[pos] = '(';
        backtrack(result, returnSize, current, open + 1, close, n, pos + 1);
    }

    if (close < open) {
        current[pos] = ')';
        backtrack(result, returnSize, current, open, close + 1, n, pos + 1);
    }
}

char** generateParenthesis(int n, int* returnSize) {
    int maxSize = 1 << (2 * n);
    char **result = (char **)malloc(maxSize * sizeof(char *));
    char *current = (char *)malloc((2 * n + 1) * sizeof(char));

    *returnSize = 0;

    backtrack(result, returnSize, current, 0, 0, n, 0);

    free(current);

    return result;
}