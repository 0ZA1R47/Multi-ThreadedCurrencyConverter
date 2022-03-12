# Multi-ThreadedCurrencyConverter
This repo contains a multi-threaded GUI-based currency converter in Python. The GUI is based on Tkinter. 
 

# Multi-threaded Currency Converter
#### An Application of Multithreading using Python3 and Tkinter 
## Pre-Requisites
- Python 3.0 and above
- Python Tkinter Module
- Python threading Module
- Pycharm IDE (Recommended)

## User Interface

#### Figure. 1
![1](https://user-images.githubusercontent.com/75529175/158011891-3bc28fee-d568-42a8-88ed-3acfe2ed73e9.png)


#### Figure. 2
![2](https://user-images.githubusercontent.com/75529175/158011894-fa1bcbdc-5451-4d23-b422-c49ab6e0b115.png)


#### Figure. 3
![3](https://user-images.githubusercontent.com/75529175/158011895-3de3e9b4-66d8-40cc-91c5-30d5f2037a7a.png)


## Multithreading Implementation

## Code Snippet
          

#### Performing two tasks via Multi-Threading  
> ```python3
> def threading():  
>    if variable1.get() == "Both":  # if user chooses 'both' then thread 1 will be executed  
>  t1 = Thread(target=ok2())  # thread t1 will call function ok2()  
>  t1.start()  # Currency will be converted into both PKR & Pound,  
>  t1.join()  
>   
>      else:  
>         t2 = Thread(target=ok1())  # thread t2 will call function ok1()
>  t2.start()  
>         t2.join()
>  t2 = Thread(target=ok1()) # thread t2 will call function ok1() t2.start()  
>  t2.join()
> 
>  t2 = Thread(target=ok1()) # thread t2 will call function ok1() t2.start()  
>  t2.join()
>  ```


Here I have used two threads to perform the conversion tasks. These two threads declared as "t1" and "t2".

**Thread "t1"** is executed when the user chooses the "both" option (figure.3) , i.e. to convert USD into both PKR and Pound simultaneously. "ok2()" function is targeted by t1 to perform the specified task.

If the user chooses to convert a single currency at a time, then the **"t2" thread** is executed. "ok1()" function is targeted by t2 to perform the specified task. (figure.1 & 2)

ok1() function is defined to convert single currency at a time. Whereas, ok2() is defined to convert both currencies simultaneously. The result of both the converted amounts is stored in a list. 

