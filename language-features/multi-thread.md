# multi-thread（多线程）


### 导入
```python
import threading
```


### threading.current_thread()
返回当前主线程。
```python
threading.current_thread()
```

### thread_instance.getName() 
获得线程的名字。


### thread_instance.getName() 
获得线程id。


### thread_instance.isAlive() 
判断线程是否存活。


### threading.Thread()
创建一个线程。
```python
thread = threading.Thread()
# 创建一个名称为 thread 的线程
thread = threading.Thread(name='thread')
# 创建线程执行：func_op。args指定 func_op 的参数
thread = threading.Thread(target=func_op, args)
```

### thread_instance.start()
开始执行。
```python
thread.start()
```


### threading.Lock()
```python
lock_instance = threading.Lock()
# 获得锁
lock_instance.acquire() 
# 释放锁
lock_instance.release()
```


### 抢夺全局变量
全局变量，被当前进程中所有存活线程共享。也就会出现抢夺全局变量的问题。
编写多线程程序，只要有读取和修改全局变量的情况，如果不采取措施，就一定不是线程安全的。
锁机制：某段代码只能单线程执行时，加上锁，其他线程等待，直到被释放后，其他线程再争锁，竞争到锁的线程执行代码，再释放锁，重复此过程，直到所有线程都走过一遍竞争到锁和释放锁的过程。











