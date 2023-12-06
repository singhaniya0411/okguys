#include<iostream>
#include<algorithm>

using namespace std;

// Structure to represent a process
struct Process {
    int processID;
    int arrivalTime;
    int burstTime;
    int priority;
    int turnaroundTime;
    int waitingTime;
};

// Function to perform Priority scheduling
void priorityScheduling(Process processes[], int n) {
    // Sort processes based on arrival time
    sort(processes, processes + n, [](const Process& a, const Process& b) {
        return a.arrivalTime < b.arrivalTime;
    });

    int currentTime = 0; // Current time
    float totalTurnaroundTime = 0.0, totalWaitingTime = 0.0;

    cout << "Process Execution Order:\n";

    for (int i = 0; i < n; ++i) {
        // Find process with the highest priority among arrived processes
        int highestPriorityIndex = i;
        for (int j = i + 1; j < n && processes[j].arrivalTime <= currentTime; ++j) {
            if (processes[j].priority < processes[highestPriorityIndex].priority) {
                highestPriorityIndex = j;
            }
        }

        // Swap processes
        swap(processes[i], processes[highestPriorityIndex]);

        // Execute the process
        cout << "Executing Process " << processes[i].processID << " from time "
             << currentTime << " to " << currentTime + processes[i].burstTime << endl;

        // Update turnaround and waiting times
        processes[i].turnaroundTime = currentTime + processes[i].burstTime - processes[i].arrivalTime;
        processes[i].waitingTime = processes[i].turnaroundTime - processes[i].burstTime;

        // Update total turnaround and waiting times
        totalTurnaroundTime += processes[i].turnaroundTime;
        totalWaitingTime += processes[i].waitingTime;

        // Update current time
        currentTime += processes[i].burstTime;
    }

    // Calculate averages
    float avgTurnaroundTime = totalTurnaroundTime / n;
    float avgWaitingTime = totalWaitingTime / n;

    cout << "\nAverage Turnaround Time: " << avgTurnaroundTime << endl;
    cout << "Average Waiting Time: " << avgWaitingTime << endl;
}

int main() {
    int n;

    // Input the number of processes
    cout << "Enter the number of processes: ";
    cin >> n;

    // Input arrival time, burst time, and priority for each process
    Process processes[n];
    for (int i = 0; i < n; ++i) {
        cout << "Enter arrival time for Process " << i + 1 << ": ";
        cin >> processes[i].arrivalTime;
        cout << "Enter burst time for Process " << i + 1 << ": ";
        cin >> processes[i].burstTime;
        cout << "Enter priority for Process " << i + 1 << ": ";
        cin >> processes[i].priority;
        processes[i].processID = i + 1;
    }

    // Perform Priority scheduling
    priorityScheduling(processes, n);

    return 0;
}

