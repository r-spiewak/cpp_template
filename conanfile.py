from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.system import package_manager


class cpp_templateRecipe(ConanFile):
    name = "cpp_template"
    version = "0.0"
    package_type = "library"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of cpp_template package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

#    def requirements(self):
#        self.requires("base64/0.4.0")

    def build_requirements(self):
        self.tool_requires("cmake/[>=3.22.6]")
        self.requires("catch2/3.6.0")

    def system_requirements(self):
        # This is a bad idea, since packages have different names on
        # different systems...
        #for package in ["clang-format"]:
        #    for manager in [
        #        package_manager.Apt(self),
        #        package_manager.Yum(self),
        #        package_manager.Dnf(self),
        #        package_manager.Apk(self),
        #        package_manager.Brew(self),
        #        package_manager.PacMan(self),
        #        package_manager.Chocolatey(self),
        #        package_manager.Zypper(self),
        #        package_manager.Pkg(self),
        #        package_manager.PkgUtil(self),
        #    ]:
        #        manager.install([package])
        packages = [
            "clang-format=1:14.0-55~exp2",
            "clang-tidy=1:14.0-55~exp2",
        ]
        package_manager.Apt(self).install(packages,recommends=True)

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)
    
    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["cpp_template"]

