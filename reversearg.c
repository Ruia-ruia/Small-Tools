#include <stdio.h>
 
size_t c_strlen(char* str);
 
int main(int argc, char** argv)
{
    char* str_ptr = argv[1];
    int str_size = c_strlen(str_ptr);
 
    for(int i = 0; i < str_size; i++)
    {
        printf("%c", str_ptr[str_size - (1 + i)]);
    }
    return 0;
}
 
size_t c_strlen(char* str)
{
    int count = 0;
    char curr = 's';
    while (curr != '\0')
    {  
        curr = str[count];
        count++;
    }
   
    return count;
}
