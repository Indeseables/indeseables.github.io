operations = [(\a b -> a + b), (\a b -> a - b), (\a b -> a * b), (\a b -> a / b)]

--testing
operationsNames = ["add", "sub", "mul", "div"]
testOperations a b = [(operations !! i) a b | i <- [0..3]]
--
hazOperaciones a b = zip (testOperations a b) operationsNames
