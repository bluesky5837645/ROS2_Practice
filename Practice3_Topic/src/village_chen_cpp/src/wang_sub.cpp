# include <chrono>
# include "rclcpp/rclcpp.hpp"
# include "std_msgs/msg/string.hpp"
# include "std_msgs/msg/u_int32.hpp"

using std::placeholders::_1;
using namespace std::chrono_literals;


class subnode:public rclcpp::Node
{
    public:
        subnode(std::string name):Node(name){
            RCLCPP_INFO(this->get_logger(),"大家好,我是%s", name.c_str());
            sub_novel = this->create_subscription<std_msgs::msg::String>("novel",10,std::bind(&subnode::sub_callback,this,_1));
            money_pub = this->create_publisher<std_msgs::msg::UInt32>("money",10);
            timer = this->create_wall_timer(500ms,std::bind(&subnode::timer_callback,this));
        }

    private:

        void sub_callback(const std_msgs::msg::String::SharedPtr msg){
            RCLCPP_INFO(this->get_logger(),"我收到%s", msg->data.c_str());
        }
        void timer_callback(){
            auto msg = std_msgs::msg::UInt32();
            msg.data = 33;
            money_pub->publish(msg);
        }
        rclcpp::TimerBase::SharedPtr timer;
        rclcpp::Subscription<std_msgs::msg::String>::SharedPtr sub_novel;
        rclcpp::Publisher<std_msgs::msg::UInt32>::SharedPtr money_pub;
};


int main(int argc, char* argv[])
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<subnode>("wang");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}