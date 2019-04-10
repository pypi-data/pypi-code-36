# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import hapi.services.tiller_pb2 as hapi_dot_services_dot_tiller__pb2


class ReleaseServiceStub(object):
  """ReleaseService is the service that a helm application uses to mutate,
  query, and manage releases.

  		Release: A named installation composed of a chart and
  				 config. At any given time a release has one
  				 chart and one config.

  		Config:  A config is a YAML file that supplies values
  				 to the parametrizable templates of a chart.

  		Chart:   A chart is a helm package that contains
  				 metadata, a default config, zero or more
  				 optionally parameterizable templates, and
  				 zero or more charts (dependencies).
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListReleases = channel.unary_stream(
        '/hapi.services.tiller.ReleaseService/ListReleases',
        request_serializer=hapi_dot_services_dot_tiller__pb2.ListReleasesRequest.SerializeToString,
        response_deserializer=hapi_dot_services_dot_tiller__pb2.ListReleasesResponse.FromString,
        )
    self.GetReleaseStatus = channel.unary_unary(
        '/hapi.services.tiller.ReleaseService/GetReleaseStatus',
        request_serializer=hapi_dot_services_dot_tiller__pb2.GetReleaseStatusRequest.SerializeToString,
        response_deserializer=hapi_dot_services_dot_tiller__pb2.GetReleaseStatusResponse.FromString,
        )
    self.GetReleaseContent = channel.unary_unary(
        '/hapi.services.tiller.ReleaseService/GetReleaseContent',
        request_serializer=hapi_dot_services_dot_tiller__pb2.GetReleaseContentRequest.SerializeToString,
        response_deserializer=hapi_dot_services_dot_tiller__pb2.GetReleaseContentResponse.FromString,
        )
    self.UpdateRelease = channel.unary_unary(
        '/hapi.services.tiller.ReleaseService/UpdateRelease',
        request_serializer=hapi_dot_services_dot_tiller__pb2.UpdateReleaseRequest.SerializeToString,
        response_deserializer=hapi_dot_services_dot_tiller__pb2.UpdateReleaseResponse.FromString,
        )
    self.InstallRelease = channel.unary_unary(
        '/hapi.services.tiller.ReleaseService/InstallRelease',
        request_serializer=hapi_dot_services_dot_tiller__pb2.InstallReleaseRequest.SerializeToString,
        response_deserializer=hapi_dot_services_dot_tiller__pb2.InstallReleaseResponse.FromString,
        )
    self.UninstallRelease = channel.unary_unary(
        '/hapi.services.tiller.ReleaseService/UninstallRelease',
        request_serializer=hapi_dot_services_dot_tiller__pb2.UninstallReleaseRequest.SerializeToString,
        response_deserializer=hapi_dot_services_dot_tiller__pb2.UninstallReleaseResponse.FromString,
        )
    self.GetVersion = channel.unary_unary(
        '/hapi.services.tiller.ReleaseService/GetVersion',
        request_serializer=hapi_dot_services_dot_tiller__pb2.GetVersionRequest.SerializeToString,
        response_deserializer=hapi_dot_services_dot_tiller__pb2.GetVersionResponse.FromString,
        )
    self.RollbackRelease = channel.unary_unary(
        '/hapi.services.tiller.ReleaseService/RollbackRelease',
        request_serializer=hapi_dot_services_dot_tiller__pb2.RollbackReleaseRequest.SerializeToString,
        response_deserializer=hapi_dot_services_dot_tiller__pb2.RollbackReleaseResponse.FromString,
        )
    self.GetHistory = channel.unary_unary(
        '/hapi.services.tiller.ReleaseService/GetHistory',
        request_serializer=hapi_dot_services_dot_tiller__pb2.GetHistoryRequest.SerializeToString,
        response_deserializer=hapi_dot_services_dot_tiller__pb2.GetHistoryResponse.FromString,
        )
    self.RunReleaseTest = channel.unary_stream(
        '/hapi.services.tiller.ReleaseService/RunReleaseTest',
        request_serializer=hapi_dot_services_dot_tiller__pb2.TestReleaseRequest.SerializeToString,
        response_deserializer=hapi_dot_services_dot_tiller__pb2.TestReleaseResponse.FromString,
        )


class ReleaseServiceServicer(object):
  """ReleaseService is the service that a helm application uses to mutate,
  query, and manage releases.

  		Release: A named installation composed of a chart and
  				 config. At any given time a release has one
  				 chart and one config.

  		Config:  A config is a YAML file that supplies values
  				 to the parametrizable templates of a chart.

  		Chart:   A chart is a helm package that contains
  				 metadata, a default config, zero or more
  				 optionally parameterizable templates, and
  				 zero or more charts (dependencies).
  """

  def ListReleases(self, request, context):
    """ListReleases retrieves release history.
    TODO: Allow filtering the set of releases by
    release status. By default, ListAllReleases returns the releases who
    current status is "Active".
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetReleaseStatus(self, request, context):
    """GetReleasesStatus retrieves status information for the specified release.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetReleaseContent(self, request, context):
    """GetReleaseContent retrieves the release content (chart + value) for the specified release.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateRelease(self, request, context):
    """UpdateRelease updates release content.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InstallRelease(self, request, context):
    """InstallRelease requests installation of a chart as a new release.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UninstallRelease(self, request, context):
    """UninstallRelease requests deletion of a named release.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetVersion(self, request, context):
    """GetVersion returns the current version of the server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RollbackRelease(self, request, context):
    """RollbackRelease rolls back a release to a previous version.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetHistory(self, request, context):
    """ReleaseHistory retrieves a releasse's history.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RunReleaseTest(self, request, context):
    """RunReleaseTest executes the tests defined of a named release
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ReleaseServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListReleases': grpc.unary_stream_rpc_method_handler(
          servicer.ListReleases,
          request_deserializer=hapi_dot_services_dot_tiller__pb2.ListReleasesRequest.FromString,
          response_serializer=hapi_dot_services_dot_tiller__pb2.ListReleasesResponse.SerializeToString,
      ),
      'GetReleaseStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetReleaseStatus,
          request_deserializer=hapi_dot_services_dot_tiller__pb2.GetReleaseStatusRequest.FromString,
          response_serializer=hapi_dot_services_dot_tiller__pb2.GetReleaseStatusResponse.SerializeToString,
      ),
      'GetReleaseContent': grpc.unary_unary_rpc_method_handler(
          servicer.GetReleaseContent,
          request_deserializer=hapi_dot_services_dot_tiller__pb2.GetReleaseContentRequest.FromString,
          response_serializer=hapi_dot_services_dot_tiller__pb2.GetReleaseContentResponse.SerializeToString,
      ),
      'UpdateRelease': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateRelease,
          request_deserializer=hapi_dot_services_dot_tiller__pb2.UpdateReleaseRequest.FromString,
          response_serializer=hapi_dot_services_dot_tiller__pb2.UpdateReleaseResponse.SerializeToString,
      ),
      'InstallRelease': grpc.unary_unary_rpc_method_handler(
          servicer.InstallRelease,
          request_deserializer=hapi_dot_services_dot_tiller__pb2.InstallReleaseRequest.FromString,
          response_serializer=hapi_dot_services_dot_tiller__pb2.InstallReleaseResponse.SerializeToString,
      ),
      'UninstallRelease': grpc.unary_unary_rpc_method_handler(
          servicer.UninstallRelease,
          request_deserializer=hapi_dot_services_dot_tiller__pb2.UninstallReleaseRequest.FromString,
          response_serializer=hapi_dot_services_dot_tiller__pb2.UninstallReleaseResponse.SerializeToString,
      ),
      'GetVersion': grpc.unary_unary_rpc_method_handler(
          servicer.GetVersion,
          request_deserializer=hapi_dot_services_dot_tiller__pb2.GetVersionRequest.FromString,
          response_serializer=hapi_dot_services_dot_tiller__pb2.GetVersionResponse.SerializeToString,
      ),
      'RollbackRelease': grpc.unary_unary_rpc_method_handler(
          servicer.RollbackRelease,
          request_deserializer=hapi_dot_services_dot_tiller__pb2.RollbackReleaseRequest.FromString,
          response_serializer=hapi_dot_services_dot_tiller__pb2.RollbackReleaseResponse.SerializeToString,
      ),
      'GetHistory': grpc.unary_unary_rpc_method_handler(
          servicer.GetHistory,
          request_deserializer=hapi_dot_services_dot_tiller__pb2.GetHistoryRequest.FromString,
          response_serializer=hapi_dot_services_dot_tiller__pb2.GetHistoryResponse.SerializeToString,
      ),
      'RunReleaseTest': grpc.unary_stream_rpc_method_handler(
          servicer.RunReleaseTest,
          request_deserializer=hapi_dot_services_dot_tiller__pb2.TestReleaseRequest.FromString,
          response_serializer=hapi_dot_services_dot_tiller__pb2.TestReleaseResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hapi.services.tiller.ReleaseService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
