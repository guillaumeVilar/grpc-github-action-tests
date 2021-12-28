import grpc
import execute_script_pb2
import execute_script_pb2_grpc
import logging

GRPC_SERVER_ADDRESS = 'python-container-1:50051'

def run():
    channel = grpc.insecure_channel(GRPC_SERVER_ADDRESS)
    stub = execute_script_pb2_grpc.ExecuterStub(channel)
    
    # Execution of script0
    script0 = execute_script_pb2.ScriptChoice(script = execute_script_pb2.ScriptChoice.SCRIPT0)
    resultStream = stub.ExecuteScript(script0)

    for result in resultStream:
        logging.info("Result {}".format(result.stdout))



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run()