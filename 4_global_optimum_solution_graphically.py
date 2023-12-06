#include<iostream>
#include<algorithm>
#include<climits>

using namespace std;

// Structure to represent a process
struct Process {
    int processID;
    int arrivalTime;
    int burstTime;
    int remainingTime;
    int startTime;
    int turnaroundTime;
    int waitingTime;
};

// Function to perform SRTF scheduling
void srtfScheduling(Process processes[], int n) {
    int currentTime = 0; // Current time
    int completedProcesses = 0;
    float totalTurnaroundTime = 0.0, totalWaitingTime = 0.0;

    cout << "Process Execution Order:\n";

    while (completedProcesses < n) {
        int shortestRemainingTimeIndex = -1;
        int shortestRemainingTime = INT_MAX;

        for (int i = 0; i < n; ++i) {
            if (processes[i].arrivalTime <= currentTime && processes[i].remainingTime < shortestRemainingTime && processes[i].remainingTime > 0) {
                shortestRemainingTime = processes[i].remainingTime;
                shortestRemainingTimeIndex = i;
            }
        }

        if (shortestRemainingTimeIndex == -1) {
            currentTime++;
        } else {
            Process& currentProcess = processes[shortestRemainingTimeIndex];

            if (currentProcess.remainingTime == currentProcess.burstTime) {
                currentProcess.startTime = currentTime;
            }

            currentProcess.remainingTime--;
            currentTime++;

            if (currentProcess.remainingTime == 0) {
                // Process is completed
                completedProcesses++;

                // Calculate turnaround and waiting times
                currentProcess.turnaroundTime = currentTime - currentProcess.arrivalTime;
                currentProcess.waitingTime = currentProcess.turnaroundTime - currentProcess.burstTime;

                // Update total turnaround and waiting times
                totalTurnaroundTime += currentProcess.turnaroundTime;
                totalWaitingTime += currentProcess.waitingTime;

                cout << "Executing Process " << currentProcess.processID << " from time "
                     << currentProcess.startTime << " to " << currentTime << endl;
            }
        }
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

    // Input arrival time and burst time for each process
    Process processes[n];
    for (int i = 0; i < n; ++i) {
        cout << "Enter arrival time for Process " << i + 1 << ": ";
        cin >> processes[i].arrivalTime;
        cout << "Enter burst time for Process " << i + 1 << ": ";
        cin >> processes[i].burstTime;
        processes[i].processID = i + 1;
        processes[i].remainingTime = processes[i].burstTime;
    }

    // Perform SRTF scheduling
    srtfScheduling(processes, n);

    return 0;
}

