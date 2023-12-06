#include<iostream>

using namespace std;

// Structure to represent a process
struct Process {
    int processID;
    int arrivalTime;
    int burstTime;
    int completionTime;
    int turnaroundTime;
    int waitingTime;
};

// Function to perform SJF scheduling and calculate average turnaround and waiting time
void sjfScheduling(Process processes[], int n) {
    // Sort processes based on arrival time
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            if (processes[j].arrivalTime > processes[j + 1].arrivalTime) {
                // Swap processes
                Process temp = processes[j];
                processes[j] = processes[j + 1];
                processes[j + 1] = temp;
            }
        }
    }

    int currentTime = 0; // Current time
    float totalTurnaroundTime = 0;
    float totalWaitingTime = 0;

    for (int i = 0; i < n; ++i) {
        // Find process with the shortest burst time among arrived processes
        int shortestJobIndex = i;
        for (int j = i + 1; j < n && processes[j].arrivalTime <= currentTime; ++j) {
            if (processes[j].burstTime < processes[shortestJobIndex].burstTime) {
                shortestJobIndex = j;
            }
        }

        // Swap processes
        Process temp = processes[i];
        processes[i] = processes[shortestJobIndex];
        processes[shortestJobIndex] = temp;

        // Execute the process
        processes[i].completionTime = currentTime + processes[i].burstTime;
        processes[i].turnaroundTime = processes[i].completionTime - processes[i].arrivalTime;
        processes[i].waitingTime = processes[i].turnaroundTime - processes[i].burstTime;

        // Update current time
        currentTime = processes[i].completionTime;

        // Accumulate turnaround and waiting times
        totalTurnaroundTime += processes[i].turnaroundTime;
        totalWaitingTime += processes[i].waitingTime;
    }

    // Calculate average turnaround and waiting times
    float avgTurnaroundTime = totalTurnaroundTime / n;
    float avgWaitingTime = totalWaitingTime / n;

    cout << "\nAverage Turnaround Time: " << avgTurnaroundTime << " units\n";
    cout << "Average Waiting Time: " << avgWaitingTime << " units\n";
}

int main() {
    int n;

    // Input the number of processes
    cout << "Enter the number of processes: ";
    cin >> n;

    // Input arrival time and burst time for each process
    Process processes[n];
    for (int i = 0; i < n; ++i) {
        cout << "Enter arrival time for Process " << i + 1 << ": ";
        cin >> processes[i].arrivalTime;
        cout << "Enter burst time for Process " << i + 1 << ": ";
        cin >> processes[i].burstTime;
        processes[i].processID = i + 1;
    }

    // Perform SJF scheduling and calculate average turnaround and waiting times
    sjfScheduling(processes, n);

    return 0;
}

