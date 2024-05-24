import os
def child_process():
    print(f"This is the child process with PID: {os.getpid()}")
def parent_process():
    print(f"This is the parent process with PID: {os.getpid()}")
def main():
    pid = os.fork()
    if pid > 0:
        # parent process
        parent_process()
        os.wait() #wait for the child process to complete
        print("Child process fnished execution")
    elif pid == 0:
        # Child Process
        child_process()
    else:
        print("Fork failed")
if __name__ == "__main__":
    main()
