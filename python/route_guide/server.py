import grpc
import route_guide_pb2
import route_guide_pb2_grpc
import time
from concurrent import futures

# RouteGuideServicer provides an implementation of the methods of the RouteGuide service.
class RouteGuideServicer(route_guide_pb2_grpc.RouteGuideServicer):
    def GetFeature(self, request, context):
        return route_guide_pb2.Feature(name=str(time.time()), location=request)
    
    def ListFeatures(self, request, context):
      for i in range(5):
        yield route_guide_pb2.Feature(name=str(i), location=request.lo)
        # yield route_guide_pb2.Feature(name=str(i), location=request.hi)
        time.sleep(1)        

    
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  route_guide_pb2_grpc.add_RouteGuideServicer_to_server(RouteGuideServicer(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()
  
if __name__ == '__main__':
    serve()