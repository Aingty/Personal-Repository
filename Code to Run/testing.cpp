#include <iostream>
#include <cstdlib>
#include <time.h>
#include <unistd.h>
using namespace std;

int main()
{
    string name;
    cout << "Please input your name: ";
    cin >> name;
    cout << "\nLani it's time to stop!!";
    sleep(5);
    return 0;
}