import grpc
import route_guide_pb2
import route_guide_pb2_grpc

GRPC_SERVER_ADDRESS = 'python-container-1:50051'

def run():
    channel = grpc.insecure_channel(GRPC_SERVER_ADDRESS)
    stub = route_guide_pb2_grpc.RouteGuideStub(channel)
    
    point = route_guide_pb2.Point(latitude=409146138, longitude=-746188906)
    feature = stub.GetFeature(point)
    
    print("Feature name {}".format(feature.name))
    print("Feature location {}".format(feature.location))

if __name__ == '__main__':
    run()