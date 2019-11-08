#include <iostream>
#include <fstream>

using namespace std;

int main(){

    cout << "What files are you testing" << endl;
    string file1;
    string file2;

    cin >> file1;
    cin >> file2;

    ifstream ourAns(file1);
    ifstream corrAns(file2);

    string line1;
    string line2;
    while(getline(ourAns, line1)){
        try
        {
            getline(corrAns, line2);
        }
        catch(const std::exception& e)
        {
            std::cerr << e.what() << '\n';
        }

        if(line1 != line2){
            cout << "Wrong Output: " << line1 << endl;
        } 
        else{
            cout << "Correct" << endl;
        } 
    }

    return 0;
}