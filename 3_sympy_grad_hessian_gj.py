#include<iostream>

using namespace std;

const int MAX_BLOCKS = 10;

// Structure to represent a memory block
struct MemoryBlock {
    int blockID;
    int size;
    bool allocated;
};

// Function to allocate memory using First Fit algorithm
void firstFit(MemoryBlock blocks[], int numBlocks, int processID, int processSize) {
    for (int i = 0; i < numBlocks; ++i) {
        if (!blocks[i].allocated && blocks[i].size >= processSize) {
            blocks[i].allocated = true;
            cout << "Process " << processID << " allocated to Block " << blocks[i].blockID << endl;
            return;
        }
    }
    cout << "Unable to allocate Process " << processID << " using First Fit.\n";
}

// Function to allocate memory using Best Fit algorithm
void bestFit(MemoryBlock blocks[], int numBlocks, int processID, int processSize) {
    int bestFitIndex = -1;

    for (int i = 0; i < numBlocks; ++i) {
        if (!blocks[i].allocated && blocks[i].size >= processSize) {
            if (bestFitIndex == -1 || blocks[i].size < blocks[bestFitIndex].size) {
                bestFitIndex = i;
            }
        }
    }

    if (bestFitIndex != -1) {
        blocks[bestFitIndex].allocated = true;
        cout << "Process " << processID << " allocated to Block " << blocks[bestFitIndex].blockID << endl;
    } else {
        cout << "Unable to allocate Process " << processID << " using Best Fit.\n";
    }
}

// Function to allocate memory using Worst Fit algorithm
void worstFit(MemoryBlock blocks[], int numBlocks, int processID, int processSize) {
    int worstFitIndex = -1;

    for (int i = 0; i < numBlocks; ++i) {
        if (!blocks[i].allocated && blocks[i].size >= processSize) {
            if (worstFitIndex == -1 || blocks[i].size > blocks[worstFitIndex].size) {
                worstFitIndex = i;
            }
        }
    }

    if (worstFitIndex != -1) {
        blocks[worstFitIndex].allocated = true;
        cout << "Process " << processID << " allocated to Block " << blocks[worstFitIndex].blockID << endl;
    } else {
        cout << "Unable to allocate Process " << processID << " using Worst Fit.\n";
    }
}

int main() {
    int numBlocks;
    cout << "Enter the number of memory blocks: ";
    cin >> numBlocks;

    MemoryBlock blocks[MAX_BLOCKS];
    for (int i = 0; i < numBlocks; ++i) {
        blocks[i].blockID = i + 1;
        cout << "Enter size of Block " << blocks[i].blockID << ": ";
        cin >> blocks[i].size;
        blocks[i].allocated = false;
    }

    int choice;
    do {
        cout << "\nMemory Allocation Algorithms:\n";
        cout << "1. First Fit\n";
        cout << "2. Best Fit\n";
        cout << "3. Worst Fit\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                int processID, processSize;
                cout << "Enter Process ID: ";
                cin >> processID;
                cout << "Enter Process Size: ";
                cin >> processSize;
                firstFit(blocks, numBlocks, processID, processSize);
                break;

            case 2:
                cout << "Enter Process ID: ";
                cin >> processID;
                cout << "Enter Process Size: ";
                cin >> processSize;
                bestFit(blocks, numBlocks, processID, processSize);
                break;

            case 3:
                cout << "Enter Process ID: ";
                cin >> processID;
                cout << "Enter Process Size: ";
                cin >> processSize;
                worstFit(blocks, numBlocks, processID, processSize);
                break;

            case 4:
                cout << "Exiting the program.\n";
                break;

            default:
                cout << "Invalid choice. Please enter a valid option.\n";
        }
    } while (choice != 4);

    return 0;
}

