# Copenheimer
A basic and easy to use version of the Copenheimer bot created by the 5th Column from 2B2T that you can easily and simply execute using python

Simply install the libraries in requirements.txt (btw I'm not sure what python versions are supported, but it should work with all versions following 3.7 at the least) and enter the IP ranges you'd like to search for Minecraft servers on in the ipRanges array.
One thread will be spawned for each range and each thread will spawn an async process for each ip address scanned through, which well then be collected at the end

The default port and default timeout can also be changed inside of the Copenheimer.py file.

(Don't scan too many ip ranges or ip ranges that r too large in one iteration or the program will take up all of your networking buffers and it'll miss a ton of stuff and u won't be able to use the internet while the program's running)
