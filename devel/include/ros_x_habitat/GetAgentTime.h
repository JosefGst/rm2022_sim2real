// Generated by gencpp from file ros_x_habitat/GetAgentTime.msg
// DO NOT EDIT!


#ifndef ROS_X_HABITAT_MESSAGE_GETAGENTTIME_H
#define ROS_X_HABITAT_MESSAGE_GETAGENTTIME_H

#include <ros/service_traits.h>


#include <ros_x_habitat/GetAgentTimeRequest.h>
#include <ros_x_habitat/GetAgentTimeResponse.h>


namespace ros_x_habitat
{

struct GetAgentTime
{

typedef GetAgentTimeRequest Request;
typedef GetAgentTimeResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GetAgentTime
} // namespace ros_x_habitat


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::ros_x_habitat::GetAgentTime > {
  static const char* value()
  {
    return "823e9883d7a51ebd6a56062eea85e4b1";
  }

  static const char* value(const ::ros_x_habitat::GetAgentTime&) { return value(); }
};

template<>
struct DataType< ::ros_x_habitat::GetAgentTime > {
  static const char* value()
  {
    return "ros_x_habitat/GetAgentTime";
  }

  static const char* value(const ::ros_x_habitat::GetAgentTime&) { return value(); }
};


// service_traits::MD5Sum< ::ros_x_habitat::GetAgentTimeRequest> should match
// service_traits::MD5Sum< ::ros_x_habitat::GetAgentTime >
template<>
struct MD5Sum< ::ros_x_habitat::GetAgentTimeRequest>
{
  static const char* value()
  {
    return MD5Sum< ::ros_x_habitat::GetAgentTime >::value();
  }
  static const char* value(const ::ros_x_habitat::GetAgentTimeRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::ros_x_habitat::GetAgentTimeRequest> should match
// service_traits::DataType< ::ros_x_habitat::GetAgentTime >
template<>
struct DataType< ::ros_x_habitat::GetAgentTimeRequest>
{
  static const char* value()
  {
    return DataType< ::ros_x_habitat::GetAgentTime >::value();
  }
  static const char* value(const ::ros_x_habitat::GetAgentTimeRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::ros_x_habitat::GetAgentTimeResponse> should match
// service_traits::MD5Sum< ::ros_x_habitat::GetAgentTime >
template<>
struct MD5Sum< ::ros_x_habitat::GetAgentTimeResponse>
{
  static const char* value()
  {
    return MD5Sum< ::ros_x_habitat::GetAgentTime >::value();
  }
  static const char* value(const ::ros_x_habitat::GetAgentTimeResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::ros_x_habitat::GetAgentTimeResponse> should match
// service_traits::DataType< ::ros_x_habitat::GetAgentTime >
template<>
struct DataType< ::ros_x_habitat::GetAgentTimeResponse>
{
  static const char* value()
  {
    return DataType< ::ros_x_habitat::GetAgentTime >::value();
  }
  static const char* value(const ::ros_x_habitat::GetAgentTimeResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ROS_X_HABITAT_MESSAGE_GETAGENTTIME_H