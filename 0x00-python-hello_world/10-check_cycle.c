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
	listint_t *cycle_t;
	listint_t *tmp;

	if (list == NULL)
		return (-1);
	cycle_t = list;
	while (cycle_t)
	{
		tmp = cycle_t;
		while (tmp)
		{
			if (tmp->next != cycle_t)
				tmp = tmp->next;
			else
				return (1);
		}
		cycle_t = cycle_t->next;
	}
	return (0);
}
