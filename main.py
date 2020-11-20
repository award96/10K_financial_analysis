from horizontalProfile import HorizontalProfile
import time


constantPath = "testingMethods.csv"

start_time = time.time()
x = HorizontalProfile("SP10k_data.csv", 2015, 2019, inputPath=constantPath)
# x.write_to_output()
x.create_horiz_analysis(2019, 2015)
print(f"###############\n{time.time() - start_time} seconds to finish")
# 6.4131879806518555 seconds
