#include<iostream> #include<unistd.h>
#include<sys/wait.h> #include<stdlib.h>

using namespace std;

int main()

int pid ;
pid=fork();
 if (pid<0){

cout<< FORK FAILED": exit(1);
}
else if(pid==0){

cout<<"I AM CHILD PROCESS" <<endl; cout<<"MY PID IS <<getpid()<<endl; exit(1);
}
else{
cout<<"I AM PARENT PROCESS"<<endl;

cout<<"MY ACTUAL PID IS: <<getpld()<<endl; wait(NULL );
exit(1);
}
return 0;
}
