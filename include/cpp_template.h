#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define CPP_TEMPLATE_EXPORT __declspec(dllexport)
#else
  #define CPP_TEMPLATE_EXPORT
#endif

CPP_TEMPLATE_EXPORT void cpp_template();
CPP_TEMPLATE_EXPORT void cpp_template_print_vector(const std::vector<std::string> &strings);
