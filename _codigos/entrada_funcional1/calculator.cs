IDictionary<string, Func<int, int, int>> calculadoraFuncional = new Dictionary<string, Func<int, int, int>>();
calculadoraFuncional["add"] = (a, b) => a + b;
calculadoraFuncional["sub"] = (a, b) => a - b;
calculadoraFuncional["mul"] = (a, b) => a * b;
calculadoraFuncional["div"] = (a, b) => a / b;

// sum example
int result = calculadoraFuncional["sum"](3, 4);
