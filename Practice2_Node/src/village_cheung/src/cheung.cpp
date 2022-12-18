#include "rclcpp/rclcpp.hpp"

int main(int argc, char* argv[]){
    rclcpp::init(argc,argv);
    rclcpp::Node::SharedPtr node = std::make_shared<rclcpp::Node>("cheung");
    RCLCPP_INFO(node->get_logger(),"大家好,我是%s","cheung");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}