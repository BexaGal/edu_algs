#include <iostream>
#include <random>

using namespace std;

void reversearray(int* arr, int size) {
    for (int i = 0; i < size / 2; i++) {
        swap(arr[i], arr[size - i - 1]);
    }
}
int partition(int* arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quicksort(int* arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quicksort(arr, low, pi - 1);
        quicksort(arr, pi + 1, high);
    }
}

int main(){
    random_device rd;
    mt19937 gen(rd());
    // Лимит от 0 до 1000
    uniform_int_distribution<> dis(50, 101);

    int size = 10;

    int* array = new int[size];

    for (int i = 0; i < size; i++) {
        array[i] = dis(gen);
    }

    quicksort(array, 0, size - 1);

    for(int i = 0; i < size; i++){
        cout << array[i] << " ";
    }
    cout << "\n";

    delete[] array;
    return 0;
}