/* Comment  1 - C-style/multi-line */
// Comment 2 - C++ style/single-line

/** Although not part of the c standard, this is style is often used to indicate
 * documentation blocks **/

// A C-style comment may appear within a C++ style comment:
// y = f(x);  /* Invoke algorithm */

// A C++ style comment may appear within a C-style comment. This is a mechanism
// for excluding a small block of source code:
/* 
  y = f(x);   // Invoke algorithms
  z = g(x);
*/

// EXAMPLE
#include <stdio.h>
/*
C-style comments can contain
multiple lines.
*/

/* Or just one line. */

// C++-style comments can comment one line.

// Or they can
// be strung together.

int main(void)
{
  // Thebelow code won't be run
  // puts("Hello");
  
  // The below code will be run
  puts("World");

  // A note regarding backslash + newline.
  // Despite belonging to translation phase 2 (vs phase 3 for comments),
  // '\' still determines which portion of the source code is considered
  // as 'comments':
  // This comment will be promoted to the next line \
  puts("Won't be run"); // may issue warning "multi-line comment"
  puts("Hello, again");
}