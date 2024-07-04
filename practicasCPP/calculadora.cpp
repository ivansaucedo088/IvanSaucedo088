// funciones basicas de una calculadora
// con menu



#include <iostream>
using namespace std;

// funciones 

int suma(int a, int b) {
    return a + b;
}

int resta(int a, int b) {
    return a - b;
}

int multiplicacion(int a, int b) {
    return a * b;
}

int divicion(int a, int b) {
    return a / b;
}

int numeros(int a, int b) {
    cout << "dame el primer numero" << endl;
    cin >> a;
    cout << "dame el segundo numero" << endl;
    cin >> b;
}

int main() {

 
    
    // pedimos los numeros
    // y generamos el bucle

    while (true) { 
        int opcion;
        //esto seria nuestro menu principal
        cout << "selecciona una opcion # numeros #" << endl;
        cout << "suma (1)"<< endl;
        cout << "resta (2)" << endl;
        cout << "multiplicacion (3)" << endl;
        cout << "divicion (4)" << endl;
        cin >> opcion; // recuerda que el cin va con flecha invertida
        
        // aqui serian las condiciones 
        
        if (opcion == 1) {
        int numeros(int a, int b);
        }

    }

}