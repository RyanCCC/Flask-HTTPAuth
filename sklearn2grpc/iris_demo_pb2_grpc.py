# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import iris_demo_pb2 as iris__demo__pb2


class IrisPredictorStub(object):
    """定义服务
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.predict_iris_species = channel.unary_unary(
                '/iris.IrisPredictor/predict_iris_species',
                request_serializer=iris__demo__pb2.IrisPredictRequest.SerializeToString,
                response_deserializer=iris__demo__pb2.IrisPredictResponse.FromString,
                )


class IrisPredictorServicer(object):
    """定义服务
    """

    def predict_iris_species(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IrisPredictorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'predict_iris_species': grpc.unary_unary_rpc_method_handler(
                    servicer.predict_iris_species,
                    request_deserializer=iris__demo__pb2.IrisPredictRequest.FromString,
                    response_serializer=iris__demo__pb2.IrisPredictResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'iris.IrisPredictor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IrisPredictor(object):
    """定义服务
    """

    @staticmethod
    def predict_iris_species(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iris.IrisPredictor/predict_iris_species',
            iris__demo__pb2.IrisPredictRequest.SerializeToString,
            iris__demo__pb2.IrisPredictResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
