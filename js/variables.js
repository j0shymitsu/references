// Use `let` for variables that will be reassigned
let count = 0;
count = 5;

// Use `const` for variables that won't be reassigned
const PI = 3.14159;

// Avoid using `var` (old syntax, has scoping issues)
var oldVariable = "Avoid this";

// Use descriptive names
let userName = "Josh";
let isLoggedIn = true;

// Use camelCase for variable names
let totalAmount = 100;

// Avoid single-letter names (except in loops)
for (let i = 0; i < 10; i++) {
    console.log(i);
}

// Always initialize variables when declaring
let age = 25;

// Use `const` by default, and only use `let` if reassignment is needed
const maxUsers = 100;
let currentUsers = 50;

// Avoid global variables (use block scope)
{
    let scopedVariable = "This is block-scoped";
    console.log(scopedVariable);
}

// Use meaningful and consistent naming conventions
const TAX_RATE = 0.07; // Use UPPER_CASE for constants

// Avoid magic numbers (use named constants)
const MAX_RETRIES = 3;
for (let attempt = 0; attempt < MAX_RETRIES; attempt++) {
    console.log(`Attempt ${attempt + 1}`);
}

// Template Literals for Strings
const firstName = "Josh";
const greeting = `Hello, ${firstName}!`;
console.log(greeting);

// Declare variables before using them
let message = "This is safe!";
console.log(message);

// Enforce stricter parsing and error handling
"use strict";
let safeVariable = "Strict mode is enabled!";
console.log(safeVariable);


/* SCOPE */
// Block scope with `let` and `const`
{
    let blockScopedLet = "I am block-scoped with let";
    const blockScopedConst = "I am block-scoped with const";
    console.log(blockScopedLet); // Accessible here
    console.log(blockScopedConst); // Accessible here
}
// console.log(blockScopedLet); // Error: blockScopedLet is not defined
// console.log(blockScopedConst); // Error: blockScopedConst is not defined

// Function scope with `var`
function testVarScope() {
    if (true) {
        var functionScopedVar = "I am function-scoped with var";
    }
    console.log(functionScopedVar); // Accessible here
}
testVarScope();
// console.log(functionScopedVar); // Error: functionScopedVar is not defined

// Avoid global variables
{
    let localScopedVariable = "I am block-scoped and not global";
    console.log(localScopedVariable); // Accessible here
}
// console.log(localScopedVariable); // Error: localScopedVariable is not defined
