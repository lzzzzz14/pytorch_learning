# My first week studying

1. First Day, we learn about how to create a tensor
2. Second Day, we learn cat and stack

### cat
* 将张量按照dim维度进行拼接

### stack
* 将张量在**新创建的dim维度**上进行拼接

### chunk
* 将张量按照维度dim进行平均切分，若不能整除，则最后一份张量小于其他张量

### split
* 将张量按照维度dim进行平均切分，也可以指定每一个分量的切分长度

### index_select
* 在维度dim上，按照index索引取出数据拼接为张量返回1
