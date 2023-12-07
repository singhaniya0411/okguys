#include <pthread.h>
#include <iostream>
#include <vector>

// Define the structure for thread data
struct thread_data {
    int id;
    int num;
};

// Define the shared total
int total = 0;

// Define the mutex
pthread_mutex_t mutex;

// This function will be executed by each thread
void* add_to_total(void* threadarg) {
    // Lock the mutex before changing the total
    pthread_mutex_lock(&mutex);

    // Cast the argument to a thread_data pointer
    struct thread_data* data;
    data = (struct thread_data*) threadarg;

    // Add the number to the total
    total += data->num;

    // Unlock the mutex
    pthread_mutex_unlock(&mutex);

    pthread_exit(NULL);
}

int main() {
    // Initialize the mutex
    pthread_mutex_init(&mutex, NULL);

    // The numbers to add
    std::vector<int> numbers = {1, 2, 3, 4, 5};

    // Create a vector of threads and thread data
    std::vector<pthread_t> threads(numbers.size());
    std::vector<thread_data> thread_data_array(numbers.size());

    // Create the threads
    for(int i = 0; i < numbers.size(); i++) {
        thread_data_array[i].id = i;
        thread_data_array[i].num = numbers[i];
        pthread_create(&threads[i], NULL, add_to_total, (void*)&thread_data_array[i]);
    }

    // Wait for all threads to complete
    for(int i = 0; i < numbers.size(); i++) {
        pthread_join(threads[i], NULL);
    }
   // Print the total
    std::cout << "Total: " << total << std::endl;

    // Destroy the mutex
    pthread_mutex_destroy(&mutex);

    return 0;
}
