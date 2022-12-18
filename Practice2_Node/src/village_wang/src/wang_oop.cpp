#include "rclcpp/rclcpp.hpp"

class writernode: public rclcpp::Node
{
    public:
        writernode(std::string name):Node(name)
        {
            RCLCPP_INFO(this->get_logger(),"大家好,大家好,我是%s",name.c_str());
        }

    private:
};

int main(int argc, char* argv[]){
    rclcpp::init(argc, argv);
    auto node = std::make_shared<writernode>("wang");
    rclcpp::spin(node);
    rclcpp::shutdown();
}

