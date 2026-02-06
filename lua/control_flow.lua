local favourite_accounts = { "acc_a", "acc_b", "acc_c" }

-- Iterators/for
for index = 1, #favourite_accounts do
    print(index, favourite_accounts[index])
end

for index, value in ipairs(favourite_accounts) do
    print(index, value)
end

-- If
local function action(loves_coffee)
    if loves_coffee then
        print("Check out my coffee shop!")
    else
        print("Still check out my coffee shop!")
    end
end

    -- Falsey: nil, false
action()    -- Same as: action(nil)
action(false)
    -- Everything else is truthy
action(true)
action(0)
action({})

