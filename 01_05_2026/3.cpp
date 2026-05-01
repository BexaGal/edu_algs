#include <iostream>
#include <random>

using namespace std;

void selectionSort(int* arr, int n){
    for(int i = 0; i < n-1; i++){
        int minidx = i;
        for(int j = i + 1; j < n; j++){
            if(arr[j] < arr[minidx]){
                minidx = j;
            }
        }
        swap(arr[i], arr[minidx]);
    }
}

int main(){
    random_device rd;                                       // Creating random number generator
    mt19937 gen(rd());
    // Лимит от 1 до 50
    uniform_int_distribution<> dis(2, 104);

    int size = 10;

    int* array = new int[size];

    for(int i = 0; i < size; i++){
        array[i] = dis(gen);
    }

    selectionSort(array, size);

    for(int i = 0; i < size; i++){
        cout << array[i] << " ";
    }
    cout << "\n";

    delete[] array;
    return 0;
}