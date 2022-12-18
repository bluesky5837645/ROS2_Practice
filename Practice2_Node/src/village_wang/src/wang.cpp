#include "rclcpp/rclcpp.hpp"

int main(int argc, char * argv[]){
    rclcpp::init(argc,argv);
    auto node = std::make_shared<rclcpp::Node>("wang");
    RCLCPP_INFO(node->get_logger(),"大家好,我是wang");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}