# Автономная миссия дронов в симуляторе Gazebo  

## Описание проекта  
Данный проект представляет собой реализацию квалификационного задания по программированию автономной миссии дронов в симуляторе **Gazebo**.  
Миссия включает два уровня сложности:  
1. **Автономный взлёт по траектории и детектирование красного шара.**  
2. **Касание красного шара и последующая посадка.**  

Проект демонстрирует навыки:  
- командной разработки,  
- устойчивого автономного полёта,  
- алгоритмической синхронизации роя дронов.  

## Структура мира  
Мир симуляции включает:  
- Поле из **Aruco-меток** (7×7 меток, №0–48);  
- Размер метки: **33 см**, шаг между центрами: **1 м**;  
- Разноцветные шары;  
- Целевой шар расположен в центре поля (метка **№24**).  

## Реализованный функционал  
- Автономный взлёт дронов;  
- Полёт к целевому шару и его детектирование;  
- Касание шара и возврат для посадки;  
- Полный автономный цикл от взлёта до посадки без ручного вмешательства.  

## Видео демонстрации  
https://disk.yandex.ru/i/NEHaGeruQ6pI1Q
