# Token Ring - Mutual Exclusion
# CCS-482 Lab Project - Problem 3

import time

# Number of processes
num_processes = 3

def request_printer(pid):
    print(f"Process P{pid} is requesting the printer...")
    time.sleep(0.5)

def print_document(pid):
    print(f"Process P{pid} has the token - PRINTING...")
    time.sleep(1)
    print(f"Process P{pid} finished printing.")

def pass_token(pid, next_pid):
    print(f"Process P{pid} is passing the token to P{next_pid}")
    print()

# Main simulation
print("=== Token Ring Mutual Exclusion Simulation ===")
print(f"Number of Processes: {num_processes}")
print(f"Shared Resource: Printer")
print()

# Token starts at P1 and goes around the ring
for i in range(1, num_processes + 1):
    next_process = (i % num_processes) + 1
    request_printer(i)
    print_document(i)
    pass_token(i, next_process)

print("=== All processes finished. Mutual Exclusion maintained. ===")
