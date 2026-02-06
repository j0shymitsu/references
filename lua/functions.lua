
local function hello(name)
    print("Hello", name)
end

local greet = function(name)
    -- .. is string concat
    print("Greetings, " ..  name .. "!")
end

localhigher_order = function(value)
    return function(another)
        return value + another
    end
end

local add_one = higher_order(1)
print("add_one(2) -> ", add_one(2))

-- Calling
local single_string = function(s)
    return s .. " - Wow!"
end

local x = single_string("hi")
local y = single_string "hi"
print(x, y)

--
local setup = function(opts)
    if opts.default = nil then
        opts.default = 17
    end

    print(opts.default, opts.other)
end

setup { default = 12, other = false }
setup { other = true }

--
local MyTable = {}
function MyTable.something(self, ...) end
function MyTable:something( ... )end
