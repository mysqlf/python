#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
import time
import numpy as np
from class_summary_statistics import SummaryStatistics
def main(one_dimensional_array):
    #创建对象
    summary_statistics=SummaryStatistics()
    #计算观测数
    number_observation=summary_statistics.calculate_number_observation(one_dimensional_array)
    #计算平均数
    arithmetic_mean=summary_statistics.calculate_arithmetic_mean(one_dimensional_array, number_observation)
    print("Arithmetic Mean:{}".format(arithmetic_mean))
    #计算中值
    median=summary_statistics.calculate_median(one_dimensional_array, number_observation)
    print("Median:{}".format(median))
    #计算标准差
    sample_standard_deviation=summary_statistics.calculate_sample_standard_deviation(one_dimensional_array, number_observation, arithmetic_mean)
    print("Sample Standard Deviation: {} ".format(sample_standard_deviation))
# if __name__ == '__main__':
#     start_time=time.clock()
#     one_dimensional_array=np.arange(100000000, dtype=np.float64)      
#     main(one_dimensional_array)
#     end_time=time.clock()
#     print("Program Runtime: {} seconds".format(round(end_time - start_time, 1)))
from class_summary_statistics_asyncio import SummaryStatisticsAsyncio
def main_asyncio(one_dimensional_array):
    summary_statistics_asyncio=SummaryStatisticsAsyncio()
    summary_statistics_asyncio.main(one_dimensional_array)
if __name__ == '__main__':
    start_time=time.clock()
    one_dimensional_array=np.arange(10000000,dtype=np.float64)
    main_asyncio(one_dimensional_array)
    end_time=time.clock()
    print("Program Runtime: {} seconds".format(round(end_time - start_time, 1)))
