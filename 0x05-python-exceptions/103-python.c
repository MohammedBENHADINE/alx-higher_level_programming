#include <Python.h>
#include <stdio.h>

/**
 *print_python_list - print info about list
 *@p: PyObject pointer
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[*] Python list info\n [ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *) p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *itemType = Py_TYPE(item)->tp_name;

		printf("Element %zd: %s\n", i, itemType);
	}
}

/**
 *print_python_bytes - print info about bytes
 *@p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	const char *byteData = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", byteData);

	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < size && i < 10; ++i)
	{
		unsigned char byte = byteData[i];

		printf("%02X ", byte);
	}

	printf("\n");
}

/**
 *print_python_float - print info about float
 *@p: PyObject pointer
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[.] float object info\n [ERROR] Invalid Float Object\n");
		return;
	}

	double value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}
