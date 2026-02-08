#undef Py_DEBUG
#include <pybind11/pybind11.h>

#include <iostream>

int main(int argc, char* argv[]) {
  // Try to import our path library
  pybind11::object path_constants = pybind11::module_::import("paths");
  auto program_path = path_constants.attr("PROGRAM_BINARY_PATH");
  //   std::cout << program_path() << '\n';
  return 0;
}
