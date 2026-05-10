# Token Ring - Mutual Exclusion
# CCS-482 Lab Project - Problem 3

import time

# Number of processes
num_processes = 3 

# List representing if each process wants to print
# True = wants to print, False = just passes the token
wants_to_print = [True, False, True]

def request_printer(pid):
    print(f"Process P{pid} is requesting the printer...") 
    time.sleep(0.5)

def print_document(pid):
    print(f"Process P{pid} has the token - PRINTING...") 
    time.sleep(1)
    print(f"Process P{pid} finished printing.") 

def pass_token(pid, next_pid):
    print(f"Process P{pid} is passing the token to P{next_pid}")
    print("-" * 30)

# Main simulation
print("=== Token Ring Mutual Exclusion Simulation ===")
print(f"Number of Processes: {num_processes}")
print(f"Shared Resource: Printer")
print()

# Token Ring Logic
for i in range(1, num_processes + 1):
    # Check if the current process wants to access the printer
    if wants_to_print[i-1]:
        request_printer(i)
        print_document(i)
    else:
        print(f"Process P{i} does not need the printer, passing token...")

    # Calculate next process in the ring
    next_process = (i % num_processes) + 1
    pass_token(i, next_process)

print("=== All processes finished. Mutual Exclusion maintained. ===")
