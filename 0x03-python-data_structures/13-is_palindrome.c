#include <stdio.h>
#include "lists.h"

/**
 * reverseList - Reverses the given linked list
 * @head: Pointer to the head of the linked list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverseList(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *curr = head;
	listint_t *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return (prev);
}
/**
 * is_palindrome - palindrome checker
 * @head: pointer on pointer list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	slow = reverseList(slow);
	fast = *head;

	while (slow != NULL)
	{
		if (slow->n != fast->n)
			return (0);
		slow = slow->next;
		fast = fast->next;
	}

	return (1);
}
