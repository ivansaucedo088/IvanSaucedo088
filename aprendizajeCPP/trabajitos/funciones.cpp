#include <iostream>
using namespace std;

//**** la funciones van afuera del main ****//

//declaramos la funcion 
int suma(int a, int b) { // nombre y parametros de la funcion
    // acciones de la funcion
    return a + b;
}

int main() {

    int resultado = suma(3, 4); // llamamos la funcion
    cout << "la sumas es: " << resultado << endl;

}