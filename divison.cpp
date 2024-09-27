#include <iostream>

int main(){
   return 0; 
}

std::pair<int, int> division(int a, int b) {
    auto abs = [](int x) {
        if(x >= 0){
            return x;
        } else {
            return x * -1;
        }
    };
    std::pair<int, int> result;
    result.first = -1;
    result.second = -1;
   if(b == 0){
       return result;
   }
   if(a == 0){
    result.first = 0;
    result.second = 0;
   } else{
        result.first = abs(a);
        result.second = 0;
        
    }
}