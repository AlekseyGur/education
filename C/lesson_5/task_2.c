/*
Условия.
Запросить у пользователя любое целое число. Написать программу, которая проверит, входит ли введённое число в диапазон (например, ль 0 до 100, квлючительно) и выведет на экран сообщение о результате проверки.
*/

#include <stdio.h>

int main() {
    int num;
    printf("Введите число для проверки\n");
    scanf("%d", &num);
    if(0 < num && num <= 100){
        printf("Число входит в диапазон (0, 100]\n");
    } else {
        printf("Число НЕ входит в диапазон (0, 100]\n");
    }
}
