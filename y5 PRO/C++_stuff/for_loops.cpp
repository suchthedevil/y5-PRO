#include <iostream>
#include <string>
//using namespace std;     this is considered a bad practice because it adds ambiguity

int main() {
    /*
    string myString = "I can count to 10";
    for (int i=1; i <= 10; i++) {
        cout << i << endl;
    }
    cout << myString << endl;
    return 0;
*/
/*
    int Pica;
    Pica = 250;
    for (int i = 10; i >= 1; i--) {
        if (i == 7) {
            cout << Pica-i << endl;
        } else {
            cout << i << endl;
        }
    }

    string word;
    cout << "Enter the word to spell";
    cin >> word;

    for (int i=0; i < word.length(); i++) {
        cout << word.at(i) << " ";
    }
*/
   std::string word = "Jozef Macka dobre kacka";
   if(word.find("macka") != std::string::npos) {
    std::cout << "It's there" << std::endl;
   } else {
    std::cout << "I'm afraid I did not find what you've been looking for mate" << std::endl;
    std::cout << "Real sorry" << std::endl;
   }
    return 0;
}
