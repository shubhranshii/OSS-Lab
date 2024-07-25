#include <stdio.h>
#include <string.h>

#define MAX_SIZE 100

int main() {
    char str[MAX_SIZE];
    int length, i;
    
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
   
    if (str[strlen(str) - 1] == '\n') {
        str[strlen(str) - 1] = '\0';
    }
    
    length = strlen(str);

    for (i = 0; i < length / 2; i++) {
        char temp = str[i];
        str[i] = str[length - i - 1];
        str[length - i - 1] = temp;
    }
    
    printf("Reversed string: %s\n", str);
    
    return 0;
}
