#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_PARAGRAPH_LENGTH 1000
#define MAX_WORD_LENGTH 50
#define MAX_WORDS 200

typedef struct {
    char word[MAX_WORD_LENGTH];
    int frequency;
} WordFrequency;

void toLowerCase(char* str) {
    for (int i = 0; str[i]; i++) {
        str[i] = tolower(str[i]);
    }
}

int findWordIndex(WordFrequency wordFreq[], int size, const char* word) {
    for (int i = 0; i < size; i++) {
        if (strcmp(wordFreq[i].word, word) == 0) {
            return i;
        }
    }
    return -1;
}

void countWordFrequencies(const char* paragraph, WordFrequency wordFreq[], int* wordCount) {
    char word[MAX_WORD_LENGTH];
    int pos = 0;
    *wordCount = 0;
    for (int i = 0; paragraph[i] != '\0'; i++) {
        if (isalpha(paragraph[i])) {
            word[pos++] = paragraph[i];
        } else if (pos > 0) {
            word[pos] = '\0';
            toLowerCase(word);
            int index = findWordIndex(wordFreq, *wordCount, word);
            if (index != -1) {
                wordFreq[index].frequency++;
            } else {
                strcpy(wordFreq[*wordCount].word, word);
                wordFreq[*wordCount].frequency = 1;
                (*wordCount)++;
            }
            pos = 0;
        }
    }
  
    if (pos > 0) {
        word[pos] = '\0';
        toLowerCase(word);
        int index = findWordIndex(wordFreq, *wordCount, word);
        if (index != -1) {
            wordFreq[index].frequency++;
        } else {
            strcpy(wordFreq[*wordCount].word, word);
            wordFreq[*wordCount].frequency = 1;
            (*wordCount)++;
        }
    }
}

int main() {
    char paragraph[MAX_PARAGRAPH_LENGTH];
    WordFrequency wordFreq[MAX_WORDS];
    int wordCount = 0;

    printf("Enter a paragraph:\n");
    fgets(paragraph, MAX_PARAGRAPH_LENGTH, stdin);

    countWordFrequencies(paragraph, wordFreq, &wordCount);

    printf("\nWord Frequencies:\n");
    for (int i = 0; i < wordCount; i++) {
        printf("%s: %d\n", wordFreq[i].word, wordFreq[i].frequency);
    }

    return 0;
}
