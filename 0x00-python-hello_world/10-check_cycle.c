#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle -  cycle checker
 * @list: pointer on list
 * Description: checks if a singly linked list has a cycle in it
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *one;
	listint_t *two;

	if (list == NULL || list->next == NULL)
	{
		return (-1);
	}
	one = list;
	two = list->next;
	while (two != NULL && two->next != NULL)
	{
		if (one == two)
		{
			return (1);
		}
		one = one->next;
		two = two->next->next;
	}
	return (0);
}
