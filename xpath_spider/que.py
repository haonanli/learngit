#队列可用于实时数据的处理，可将队列放进类中进行定义
from queue import Queue
que_a=Queue()
a=[1,2,3]
for i in a:
    que_a.put(i)
while not que_a.empty():#两种方法都可以
# while True:
    result=que_a.get()
    print(result)
    que_a.task_done()
que_a.join()