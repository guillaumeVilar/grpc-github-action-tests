import grpc
import route_guide_pb2
import route_guide_pb2_grpc

GRPC_SERVER_ADDRESS = 'python-container-1:50051'

def run():
    channel = grpc.insecure_channel(GRPC_SERVER_ADDRESS)
    stub = route_guide_pb2_grpc.RouteGuideStub(channel)
    
    
    ########### GetFeature rpc call ############
    point = route_guide_pb2.Point(latitude=409146138, longitude=-746188906)
    feature = stub.GetFeature(point)
    print("Feature name {}".format(feature.name))
    print("Feature location {}".format(feature.location))

    ########### ListFeatures rpc call ############
    rectangle = route_guide_pb2.Rectangle(
        lo=route_guide_pb2.Point(latitude=400000000, longitude=-750000000),
        hi=route_guide_pb2.Point(latitude=420000000, longitude=-730000000))
    print("Looking for features between 40, -75 and 42, -73")

    features = stub.ListFeatures(rectangle)

    for feature in features:
        print("Feature called %s at %s" % (feature.name, feature.location))



if __name__ == '__main__':
    run()