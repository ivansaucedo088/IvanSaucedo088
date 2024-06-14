#include <iostream>
using namespace std;
int main() {

    //se pueden declarar las de dos variables en una linea 
    int a = 10, b = 5;

    // operadores arimeticos
    // por cada accion diferente usamos flechas
    cout << "suma " << a + b << endl;
    cout << "resta " << a - b << endl;
    cout << "multiplicacion " << a * b << endl;
    cout << "division " << a / b << endl;

    //opadores racionales

    cout << a << " es mayor que " << b << (a < b) << endl;

    // operador logico
    cout << "a es mayor que b Y b es menor que 10: " << ((a > b) && (b < 10)) << endl;
}