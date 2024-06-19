<h4>Hello World</h4>

Como disse o professor Gustavo Guanabara existe uma maldição no mundo da programação, se você não começa escrevendo um programa que diz Olá Mundo(Hello world), você nunca aprende a linguagem que esta tentando aprender, então vamos quebrar logo essa maldição escrevendo o nosso primeiro programa.

```print("Hello, World")```

Viu só? Não foi dificil, agora vou explicar o que cada função faz. A função print em Python é uma das funções mais fundamentais e amplamente utilizadas. Ela é responsável por enviar dados de saída para o console, ou até mesmo passar argumentos para o interpretador python como ```print(1+1)```. Nesse caso em especifico o interpretador python, vai ler a instrução que você passou para ele, vai processar essa instrução e vai te retornar a resposta referente a operação matematica que você passou como argumento.

Agora vou mostrar todo o código por traz desse simples comando, você não vai precisar saber disso agora porquê diferente de algumas linguagens, a linguagem python não foi escrita em python, mas em sua grande maioria foi escrita em C, e o código por tras do print do python escrito em Cython é:

```
// Importar headers necessários
#include <Python.h>

// Função print
static PyObject *
builtin_print(PyObject *self, PyObject *args, PyObject *kwds) {
    // Variáveis usadas para armazenar argumentos e palavra-chave
    PyObject *sep = NULL, *end = NULL, *file = NULL, *flush = NULL;
    static char *kwlist[] = {"sep", "end", "file", "flush", NULL};

    // Parsear argumentos e palavras-chave
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OOOO:print",
                                     kwlist, &sep, &end, &file, &flush)) {
        return NULL;
    }

    // Definir separador padrão se não especificado
    if (sep == NULL) {
        sep = PyUnicode_FromString(" ");
    }

    // Definir final padrão se não especificado
    if (end == NULL) {
        end = PyUnicode_FromString("\n");
    }

    // Definir arquivo padrão se não especificado
    if (file == NULL || file == Py_None) {
        file = PySys_GetObject("stdout");  // Obter stdout
        if (file == NULL) {
            PyErr_SetString(PyExc_RuntimeError, "lost sys.stdout");
            return NULL;
        }
    }

    // Verificar se o objeto file é um arquivo
    if (!PyFile_Check(file)) {
        PyErr_SetString(PyExc_TypeError, "file must be a file-like object");
        return NULL;
    }

    // Iterar sobre os argumentos e imprimir cada um
    for (Py_ssize_t i = 0; i < PyTuple_Size(args); i++) {
        if (i > 0 && sep != NULL) {
            if (PyFile_WriteObject(sep, file, Py_PRINT_RAW) != 0) {
                return NULL;
            }
        }
        if (PyFile_WriteObject(PyTuple_GetItem(args, i), file, Py_PRINT_RAW) != 0) {
            return NULL;
        }
    }

    // Escrever o final da linha
    if (PyFile_WriteObject(end, file, Py_PRINT_RAW) != 0) {
        return NULL;
    }

    // Realizar flush se solicitado
    if (flush == Py_True) {
        PyObject *result = PyObject_CallMethodNoArgs(file, PyUnicode_FromString("flush"));
        if (result == NULL) {
            return NULL;
        }
        Py_DECREF(result);
    }

    Py_RETURN_NONE;
}

// Definir a função no módulo
static PyMethodDef builtin_methods[] = {
    {"print", (PyCFunction)builtin_print, METH_VARARGS | METH_KEYWORDS, "Prints to a stream"},
    {NULL, NULL, 0, NULL}  // Sentinela
};

// Inicializar o módulo
static struct PyModuleDef builtinsmodule = {
    PyModuleDef_HEAD_INIT,
    "builtins",  // Nome do módulo
    NULL,        // Documentação do módulo
    -1,          // Tamanho do estado do módulo
    builtin_methods
};

// Inicializar o módulo
PyMODINIT_FUNC
PyInit_builtins(void) {
    return PyModule_Create(&builtinsmodule);
}
```

Como eu disse você não vai precisar saber de tudo isso agora mas acho legal mostrar isso para vocês terem uma dimensão do quão grande é a linguagem python!
