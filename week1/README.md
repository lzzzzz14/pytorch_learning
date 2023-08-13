# My first week studying

1. First Day, we learn about how to create a tensor
2. Second Day, we learn cat and stack

## cat

- 将张量按照dim维度进行拼接

## stack

- 将张量在**新创建的dim维度**上进行拼接

## chunk

- 将张量按照维度dim进行平均切分，若不能整除，则最后一份张量小于其他张量

## split

- 将张量按照维度dim进行平均切分，也可以指定每一个分量的切分长度

## index_select

- 在维度dim上，按照index索引取出数据拼接为张量返回1

## mask_select

- 按照mask中的True进行索引拼接得到一维张量返回
- 最后返回的是一维张量

### 小tips，tensor.le/lt/ge/gt, 会得到True or False，需要指定一个数来进行比较

1. le is mean less than or euqal
2. lt is mean less
3. ge is mean greater than or equal
4. gt greater le lt

## reshape

- 变换张量形状。当张量在内存中是连续时，返回的张量和原来的张量共享数据内存，改变一个变量时，另一个变量也会被改变

## transpose

- 交换张量的两个维度。参数为，dim0:要交换的第一个维度，dim1:要交换的第二个维度

### torch.t()

- 2维张量转置，对于2维矩阵而言，等驾驭torch.transpose(input, 0, 1)

## squeeze

- 压缩长度为1的维度
- dim: 若为None，则移除所有长度为1的维度；若指定维度，则当且仅当该维度长度为1时可以移除

### torch.unsqueeze()

- 根据dim扩展维度，长度为1

## torch.add()

- 逐元素计算input + alpha\*other

## torch.addcdiv()

- 计算公式为：out ${i}=\operatorname{input}{i}+$ value $\times \frac{\text { tensor } 1{i}}{\text { tensor } 2{i}}$

## torch.addcmul()

- 计算公式为：out ${i}=$ input ${i}+$ value $\times$ tensor $1{i} \times$ tensor $2{i}$
