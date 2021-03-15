#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {

    string word;
    int strLen = 0;
    int count = 0;

    getline (cin, word);

    strLen = word.length();

    for (int i = 0; i < strLen+1; i++) {
        if (islower(word[i])) {
            count++;
        }
    }

    cout << count << endl;
}