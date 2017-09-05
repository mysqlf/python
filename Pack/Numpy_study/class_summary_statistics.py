#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
import sys
import traceback
import time
from math import sqrt
class SummaryStatistics(object):
    """
    使用标准过程计算观测数、算术平均值、中值和样本标准差 
    """
    def __init__(self):
        pass
    def calculate_number_observation(self,one_dimensional_array):
        """
        计算观测数 
        :参数 one_dimensional_array: numpy一维数组 
        :返回值 观测数 
        """
        number_observation=0
        try:
            number_observation=one_dimensional_array.size
        except Exception:
            self.print_exception_message()
        return number_observation
    def calculate_arithmetic_mean(self,one_dimensional_array,number_observation):
        """
        计算算术平均值 
        :参数 one_dimensional_array: numpy一维数组 
        :参数 number_observation: 观测数 
        :返回值 算术平均值 
        """
        arithmetic_mean=0.0
        try:
            sum_result=0.0
            for  i in range(number_observation):
                sum_result+=one_dimensional_array[i]
                arithmetic_mean=sum_result/number_observation
        except Exception:
            self.print_exception_message()
        return arithmetic_mean
    def calculate_median(self,one_dimensional_array,number_observation):
        """
        计算中值 

        :参数 one_dimensional_array: numpy一维数组 
        :参数 number_observation: 观测数 
        :返回值 中值 

        """
        median=0.0
        try:
            one_dimensional_array.sort()
            half_position=number_observation//2
            if not number_observation%2:
                median=(one_dimensional_array[half_position-1]+one_dimensional_array[half_position])/2.0
            else:
                median=one_dimensional_array[half_position]     
        except Exception:
            self.print_exception_message()
        return median
    def calculate_sample_standard_deviation(self,one_dimensional_array,number_observation,arithmetic_mean):
        """
        计算样本标准差 
        :参数 one_dimensional_array: numpy一维数组 
        :参数 number_observation: 观测数 
        :参数 arithmetic_mean: 算术平均值 
        :返回值 样本标准差值 
        """
        sample_standard_deviation = 0.0
        try:
            sum_result=0.0
            for i in range(number_observation):
                sum_result+=pow((one_dimensional_array[i]-arithmetic_mean),2)
            sample_variance=sum_result/(number_observation-1)
            sample_standard_deviction=sqrt(sample_variance)
        except Exception :
            self.print_exception_message()
        return sample_standard_deviction

    def print_exception_message(self,message_orientation='horizonal'):
        try:
            exc_type,exc_value,exc_tp=sys.exc_info()
            file_name,line_number,procedure_name,line_code=traceback.extract_tb(exc_tb)[-1]
            time_stamp="[Time Stamp]:"+str(time.strftime("%Y-%m-%d %I:%M:%S %p"))
            file_name="[File Name]:"+str(file_name)
            procedure_name="[Procedure Name]:"+str(procedure_name)
            error_message="[Error message]:"+str(exc_value)
            error_type="[Error Type]:"+str(exc_type)
            line_number="[Line number]"+str(line_number)
            line_code="[Line Code]"+str(line_code)
            if(message_orientation=='horizonal'):
                print( "An error occurred:{};{};{};{};{};{};{}".format(time_stamp, file_name, procedure_name, error_message, error_type, line_number, line_code))
            elif (message_orientation == "vertical"):
                print( "An error occurred:\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(time_stamp, file_name, procedure_name, error_message, error_type, line_number, line_code))
            else:
                pass
        except Exception:
            pass
        else:
            pass

