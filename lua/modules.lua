-- There isn't anything special about modules in lua:
-- Modules are just files.
local M = {}
M.cool_function = function() end
return M

local foo = require('foo')
foo.cool_function()

-- Multiple returns
local return_four_values = function()
    return 1, 2, 3, 4
end

first, second, last = returns_four_values()

print("first: ", first)
print("second: ", second)
print("last: ", last)
    -- the '4' is discarded

local variable_arguments = function( ... )
    local arguments = { ... }
    for i, v in ipairs({ ... }) do print(i, v) end
    return unpack(arguments)
end

print("=============")
print("1:", variable_arguments("hello," "world", "!"))
print("=============")
print("2:", variable_arguments("hello", "world", "!"), "<lost>")
