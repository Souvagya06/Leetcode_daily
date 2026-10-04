
bool checkValidString(char* s) {
    int minOpen = 0;
    int maxOpen = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') {
            minOpen++;
            maxOpen++;
        }
        else if (s[i] == ')') {
            minOpen--;
            maxOpen--;
        }
        else {  // '*'
            minOpen--;  // Treat * as ')'
            maxOpen++;  // Treat * as '('
        }

        if (maxOpen < 0) {
            return false;
        }

        if (minOpen < 0) {
            minOpen = 0;
        }
    }

    return minOpen == 0;
}
