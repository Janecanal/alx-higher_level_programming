#include "lists.h"

/**
 * check_cycle - search infinite loop on linkedlists
 * @list: linkedlist head
 * Return: 1 if cycle found, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *forward = list;
	listint_t *back = list;

	if (!list || !list->next)
		return (0);

	back = back->next;
	forward = forward->next->next;

	for (; forward && back && forward->next;)
	{
		if (back == forward)
			return (1);
		back = back->next;
		forward = forward->next->next;
	}
	return (0);
}
