#include "cpp_template.h"
#include <vector>
#include <string>

int main() {
    cpp_template();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    cpp_template_print_vector(vec);
}
