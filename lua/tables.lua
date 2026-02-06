-- Tables are the only data structure in Lua
local list = { "first", 2, false, function() print("Fourth") end }
print("1-indexed: ", list[1])
print("Fourth is 4...", list[4]())

-- Tables as maps
local t = {
    literal_key = "a string"
    ["an expression"] = "also works",
    [function() end] = true
}

print("literal_key : ", t.literal_key)
print("an expression: ", t["an expression"])
print("function() end: ", t[function() end])    -- This will print nothing


