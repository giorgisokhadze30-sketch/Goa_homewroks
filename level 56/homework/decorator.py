import time 

input("Click enter to start")
start_time = time.time()

input("Click enter to stop")
end_time = time.time()

passed_time = round(end_time - start_time, 2)

print(f"passed {passed_time} seconds")