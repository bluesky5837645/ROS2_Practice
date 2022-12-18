#include <chrono>

# include "rclcpp/rclcpp.hpp"
# include "std_msgs/msg/string.hpp"
# include "std_msgs/msg/u_int32.hpp"



using std::placeholders::_1;
using namespace std::chrono_literals;


class writernode: public rclcpp::Node
{
    public:
        writernode(std::string name):Node(name){
            RCLCPP_INFO(this->get_logger(),"大家好我是作家%s",name.c_str());
            sub_money = this->create_subscription<std_msgs::msg::UInt32>("money", 10, std::bind(&writernode::topic_callback, this,_1));
            pub_novel = this->create_publisher<std_msgs::msg::String>("novel",10);
            timer = this->create_wall_timer(1ms, std::bind(&writernode::timer_callback, this));
            count = 0;
        }
        
    private:
        int32_t count;
        void timer_callback()
        {
            auto message = std_msgs::msg::String();
            message.data = "作者發布了第" + std::to_string(count++) + "回小說";
            pub_novel->publish(message);

        }
        void topic_callback(const std_msgs::msg::UInt32::SharedPtr msg)
        {
            RCLCPP_INFO(this->get_logger(), "作家已經收到%d元", msg->data);
        }
        rclcpp::TimerBase::SharedPtr timer;
        rclcpp::Subscription<std_msgs::msg::UInt32>::SharedPtr sub_money;
        rclcpp::Publisher<std_msgs::msg::String>::SharedPtr pub_novel;
        

};

int main(int argc, char* argv[]){
    rclcpp::init(argc,argv);
    auto node = std::make_shared<writernode>("chen");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}