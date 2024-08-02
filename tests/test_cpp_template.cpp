#define CATCH_CONFIG_MAIN
#include <catch2/catch_test_macros.hpp>

#include "cpp_template.h"

TEST_CASE( "Example tests", "[example]" ) {
    //REQUIRE( cpp_template() );
    REQUIRE( 3 == 2 + 1 );
}
