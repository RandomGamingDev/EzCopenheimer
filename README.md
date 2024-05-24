# EzCopenheimer
A basic and easier to use version of the Copenheimer bot created by the 5th Column from 2B2T that you can easily and simply execute using python made for educational purposes. Especially since you don't have to deal with anything like build systems, compilation, and the exact same thing on repeat for dependencies.




# Usage
I've created a video on it which you can check out here: https://youtu.be/oOV52vOx6W0

This version of Copenheimer also doesn't require massscan, zmap, or nmap which are prerequisites for many of the other Copenheimer clones!

# Installation
1. Install [Python](https://python.org/). Make sure you install Python 3 and **not** Python 2. Make sure you check `add Python to PATH`.
2. Verify the installation with `python --version`. If this doesent work, try `python3 --version`
3. Install the libraries in requirements.txt: `python - pip install -r /path/to/requirments.txt`. Replace `/path/to/requirments.txt` with the actual path to `requirments.txt`. If you used `python3` in step 2, replace `python` with `python3`.
4. Run `copenheimer.py. Double-clicking the file should work, but if not, use `python /path/to/copenheimer.py`. As in the previous step, if you used `python3` in step 2, replace `python` with `python3`.
 
(btw I'm not sure what python versions are supported, but it should work with all versions following 3.7 at the least) and enter the IP ranges you'd like to search for Minecraft servers on in the ipRanges array.
One thread will be spawned for each range and each thread will spawn an async process for each ip address scanned through, which well then be collected at the end

The default port and default timeout can also be changed inside of the Copenheimer.py file.

Remember to use multiple arrays inside of the main ipIters list as so not to use more network buffers than what you have.
Also, enter multiple ipRanges into each `ipIter` aka each smaller list inside of `ipIters` as 1 thread will be allocated to each `ipRange`.
In this way you can easily choosing how many resources are allocated to the bot, from how many network buffers to how many threads.
```py
ipIters = [
               [
                    #Enter the IP ranges here like this: [[127, 0, 0, 1], [127, 0, 0, 1]],
		                #A thread will scan each
               ],
               [ # Since computer network buffers are limited, there are different ipIters which are looped over synchronously in order, thus this is the same as the previous one, it just runs afterwards
               ]
          ]
```

(Don't scan too many ip ranges or ip ranges that r too large in one iteration or the program will take up all of your networking buffers and it'll miss a ton of stuff and u won't be able to use the internet while the program's running)
