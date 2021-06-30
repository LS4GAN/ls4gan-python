#!/usr/bin/env bats

@test "An example test with BATS" {
    run python -c 'import sys; print(sys.version)' 
    echo "$output"
    [ "$status" -eq 0 ]    
    [ -n "$(echo "$output" | head -1 | grep '^3')" ]
}
