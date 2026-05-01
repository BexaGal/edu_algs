#include <iostream>
#include <algorithm>
#include <string>
#include <random>

using namespace std;

const string alphabet[26] = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                           "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                           "u", "v", "w", "x", "y", "z"};

int main(){
    random_device rd;                                       // Creating random number generator
    mt19937 gen(rd());
    // Лимит от 1 до 50
    uniform_int_distribution<> dis(0, 26);
    string line = "";
    for(int i = 0; i < 10; i++){
        line.append(alphabet[dis(gen)]);
    }
    cout << line << endl;
    sort(line.begin(), line.end());

    cout << line << endl;

    return 0;
}
