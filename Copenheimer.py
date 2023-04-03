from mcstatus import JavaServer
import threading
import asyncio

defaultPort = 25565
defaultTimeout = 1
waitForTimeout = 100
ipIters = [
               [
                    #Enter the IP ranges here like this: [[127, 0, 0, 1], [127, 0, 0, 1]],
		            #A thread will scan each
               ],
               [ # Since computer network buffers are limited, there are different ipIters which are looped over synchronously in order, thus this is the same as the previous one, it just runs afterwards
               ]
          ]
outputFileName = "output.txt"

def GetAddr(ip):
    return f"{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}:{defaultPort}"

class SearchThread(threading.Thread):
    def __init__(self, ipRange):
        threading.Thread.__init__(self)
        self.ipRange = ipRange
    def run(self):
        asyncio.run(self.async_run())
    async def async_run(self):
        tasks = []
        while self.ipRange[0] != self.ipRange[1]:
            server = JavaServer.lookup(GetAddr(self.ipRange[0]))
            server.timeout = defaultTimeout
            tasks.append([self.ipRange[0].copy(), asyncio.create_task(server.async_status())])

            self.ipRange[0][3] += 1
            for i in reversed(range(len(self.ipRange[0]))):
                if self.ipRange[0][i] > 255:
                    self.ipRange[0][i] = 0
                    self.ipRange[0][i - 1] += 1
                else:
                    break

        for task in tasks:
            try:
                await asyncio.wait_for(task[1], timeout=waitForTimeout)
                task[1].result()
                outputFile = open(outputFileName, 'a')
                outputFile.write(GetAddr(task[0]) + '\n')
                outputFile.close()
            except:
                pass
        print("Thread finished!")

def main():
    print("Program started!")
    for i in range(len(ipIters)):
        print(f"Iteration #{i} started!")
        searchThreads = []
        for ipRange in ipIters[i]:
            searchThreads.append(SearchThread(ipRange))
            searchThreads[len(searchThreads) - 1].start()
        for thread in searchThreads:
            thread.join()

if __name__ == "__main__":
    main()
