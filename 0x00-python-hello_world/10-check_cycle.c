#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <inttypes.h>
/**
 * lookup_add - check if address already passed by
 * @list: pointer to Pointers list
 * @add: add to check
 * Return: 1 if exists, 0 if not
 */

int lookup_add(listint_t *list, int add)
{
	listint_t *temp = list;

	while (temp != NULL)
	{
		if (temp->n == add)
		{
			return (1);
		}
		else
		{
			temp = temp->next;
		}
	}
	return (0);
}
/**
 * check_cycle -  cycle checker
 * @list: pointer on list
 * Description: checks if a singly linked list has a cycle in it
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *cycle_t;
	listint_t *headPointers = NULL;

	if (list == NULL)
		return (-1);
	add_nodeint(&headPointers, (int)(intptr_t)list);
	cycle_t = list->next;
	while (cycle_t)
	{
		if (lookup_add(headPointers, (int)(intptr_t)cycle_t))
		{
			return (1);
		}
		else
		{
			add_nodeint(&headPointers, (int)(intptr_t)cycle_t);
		}
		cycle_t = cycle_t->next;
	}
	return (0);
}
