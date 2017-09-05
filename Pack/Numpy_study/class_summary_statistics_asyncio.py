#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf

import sys
import time
import traceback
import asyncio
from math import sqrt

class SummaryStatisticsAsyncio(object):
    """
    使用asyncion库计算观测数、算术平均值、中值和样本标准差 
    """
    def __init__(self):
        pass
    
    async def calculate_number_observation(self, one_dimensional_array):    
        """
        计算观测数 
        :参数 one_dimensional_array: numpy一维数组 
        :返回值 空
        """
        try:
            print('start calculate_number_observation() procedure')   
            await asyncio.sleep(0)
            number_observation = one_dimensional_array.size
            print("Number of Observation: {} ".format(number_observation))    
            print("观测数：  {} ".format(number_observation))    
            await self.calcuate_arithmetic_mean(one_dimensional_array, number_observation)
            print("finished calculate_number_observation() procedure")   
        except Exception:
            self.print_exception_message()
            
    async def calcuate_arithmetic_mean(self, one_dimensional_array, number_observation):    
        """
        计算算术平均值 
        :参数 one_dimensional_array: numpy一维数组 
        :参数 number_observation: 观测数 
        :返回值 空
        """
        try:
            print('start calcuate_arithmetic_mean() procedure')   
            await self.calculate_median(one_dimensional_array, number_observation)
            sum_result = 0.0
            await asyncio.sleep(0)
            for i in range(number_observation):       
                sum_result += one_dimensional_array[i]    
            arithmetic_mean = sum_result / number_observation
            print("Arithmetic Mean: {} ".format(arithmetic_mean))    
            await self.calculate_sample_standard_deviation(one_dimensional_array, number_observation, arithmetic_mean)
            print("finished calcuate_arithmetic_mean() procedure")   
        except Exception:
            self.print_exception_message()
            
    async def calculate_median(self, one_dimensional_array, number_observation):      
        """
        计算中值 
        :参数 one_dimensional_array: numpy一维数组 
        :参数 number_observation: 观测数 
        :返回值 空
        """
        try:
            print('starting calculate_median()')   
            await asyncio.sleep(0)
            one_dimensional_array.sort()    
            half_position = number_observation // 2
            if not number_observation % 2:
                median = (one_dimensional_array[half_position - 1] + one_dimensional_array[half_position]) / 2.0
            else:
                median = one_dimensional_array[half_position]        
            print("Median: {} ".format(median))
            print("finished calculate_median() procedure")   
        except Exception:
            self.print_exception_message()

    async def calculate_sample_standard_deviation(self, one_dimensional_array, number_observation, arithmetic_mean):    
        """
        计算样本标准差 
        :参数 one_dimensional_array: numpy一维数组 
        :参数 number_observation:  观测数 
        :参数 arithmetic_mean: 算术平均值 
        :返回值 空
        """
        try:
            print('start calculate_sample_standard_deviation() procedure')   
            await asyncio.sleep(0)
            sum_result = 0.0
            for i in range(number_observation):                   
                sum_result += pow((one_dimensional_array[i] - arithmetic_mean), 2)           
            sample_variance = sum_result / (number_observation - 1)            
            sample_standard_deviation = sqrt(sample_variance)        
            print("Sample Standard Deviation: {} ".format(sample_standard_deviation))
            print("finished calculate_sample_standard_deviation() procedure")   
        except Exception:
            self.print_exception_message()
            
    def print_exception_message(self, message_orientation = "horizontal"):
        """
        打印完整异常消息 
        :参数 message_orientation: 水平或垂直 
        :返回值 空
        """
        try:
            exc_type, exc_value, exc_tb = sys.exc_info()            
            file_name, line_number, procedure_name, line_code = traceback.extract_tb(exc_tb)[-1]       
            time_stamp = " [Time Stamp]: " + str(time.strftime("%Y-%m-%d %I:%M:%S %p")) 
            file_name = " [File Name]: " + str(file_name)
            procedure_name = " [Procedure Name]: " + str(procedure_name)
            error_message = " [Error Message]: " + str(exc_value)        
            error_type = " [Error Type]: " + str(exc_type)                    
            line_number = " [Line Number]: " + str(line_number)                
            line_code = " [Line Code]: " + str(line_code) 
            if (message_orientation == "horizontal"):
                print( "An error occurred:{};{};{};{};{};{};{}".format(time_stamp, file_name, procedure_name, error_message, error_type, line_number, line_code))
            elif (message_orientation == "vertical"):
                print( "An error occurred:\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(time_stamp, file_name, procedure_name, error_message, error_type, line_number, line_code))
            else:
                pass                    
        except Exception:
            pass
    
    def main(self, one_dimensional_array):    
        """
        启动事件循环异步进程 
        :参数 one_dimensional_array: numpy一维数组 
        """
        try:
            ioloop = asyncio.get_event_loop()
            tasks = [ioloop.create_task(self.calculate_number_observation(one_dimensional_array))]
            wait_tasks = asyncio.wait(tasks)
            ioloop.run_until_complete(wait_tasks)
            ioloop.close()
        except Exception:
            pass
