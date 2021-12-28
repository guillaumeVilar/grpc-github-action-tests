import grpc
import execute_script_pb2
import execute_script_pb2_grpc
import time
from concurrent import futures
import logging
import subprocess


# ExecuterServicer provides an implementation of the methods of the Executer service.
class ExecuterServicer(execute_script_pb2_grpc.ExecuterServicer):
    def ExecuteScript(self, request, context):
        logging.info("Request {}".format(request))
        logging.info("Request.state {}".format(request.script))
        if (request.script == execute_script_pb2.ScriptChoice.SCRIPT0):
            logging.info("Executing Script0")
            
            # This function will redirect stderr to stdin. This could be useful in the case if the order where stdin and stderr arrives matter. 
            # popen = subprocess.Popen(["/opt/python/execute_script/script0.sh"], stdout = subprocess.PIPE, stderr=subprocess.STDOUT)           
            
            # This function will read stderr at the end of the process.  
            popen = subprocess.Popen(["/opt/python/execute_script/script0.sh"], stdout = subprocess.PIPE, stderr=subprocess.PIPE)            
            
            # Poll process for new output until finished
            while True: 
                stdout_nextline = popen.stdout.readline()
                
                if popen.poll() is not None: 
                    logging.info("Exiting script")
                    # Getting stderr at the end of the script
                    output, stderr = popen.communicate()
                    logging.info("stderr_nextline: {}".format(stderr))
                    yield execute_script_pb2.ScriptResult(stderr = stderr)
                    break

                logging.info("stdout_nextline: {}".format(stdout_nextline))    
                yield execute_script_pb2.ScriptResult(stdout = stdout_nextline)
            
        elif (request.script == execute_script_pb2.ScriptChoice.SCRIPT1):
            logging.info("Executing Script1")
        elif (request.script == execute_script_pb2.ScriptChoice.SCRIPT2):
            logging.info("Executing Script2")    
        
        # Simulate the execution of the script
        # for i in range(5):
        #     yield execute_script_pb2.ScriptResult(result = str(request.script) + ' - ' + str(i) + '...')
        #     time.sleep(1)
    
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  execute_script_pb2_grpc.add_ExecuterServicer_to_server(ExecuterServicer(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()
  
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()