#include <stdio.h>
#include <stdlib.h>

int fib(int n);

int main(int argc, char** argv)
{
  int nth = atoi(argv[1]);
  int ret;

  for (int i = 1; i <= nth; i++)
  {
    ret = fib(i);
    printf("%d\n", ret);
  }

  return 0;
}

int fib(int n)
{
  if ((n == 1) || (n == 2))
  {
    return 1;
  }
  else
  {
    return fib(n - 1) + fib(n - 2);
  }
}
