# My first week studying

1. First Day, we learn about how to create a tensor
2. Second Day, we learn cat and stack

## cat
* 将张量按照dim维度进行拼接

## stack
* 将张量在**新创建的dim维度**上进行拼接

## chunk
* 将张量按照维度dim进行平均切分，若不能整除，则最后一份张量小于其他张量

## split
* 将张量按照维度dim进行平均切分，也可以指定每一个分量的切分长度

## index_select
* 在维度dim上，按照index索引取出数据拼接为张量返回1

## mask_select
* 按照mask中的True进行索引拼接得到一维张量返回
* 最后返回的是一维张量
###
** le is mean less than or euqal
** lt is mean less
** ge is mean greater than or equal 
** gt greater le lt 

## reshape
* 变换张量形状。当张量在内存中是连续时，返回的张量和原来的张量共享数据内存，改变一个变量时，另一个变量也会被改变
