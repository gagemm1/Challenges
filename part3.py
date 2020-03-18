'''
Write an alternative implementation of the following method.
/// <summary>
/// Gets a sub-item summary for a given item number.
/// </summary>
/// <param name="itemNumber">The item number of the item to get the sub-item summary of.</param>
public SubItemSummary[] GetSubItemSummary(string itemNumber)
{
    IEnumerable<Item> subItems = GetSubItems(itemNumber);

    List<SubItemSummary> subItemSummary = new List<SubItemSummary>();

    foreach (Item item in subItems)
    {
        IEnumerable<SubItemSummary> tempSummaries = TransformSubItems(item, item.GetSubItems());

        subItemSummary.AddRange(tempSummaries);
    }

    return subItemSummary.ToArray();
}
'''

#since I'm doing this all in python, I'll try and recreate it in python as an alternative implementation
#(as far as I can understand what that function above is doing)
#it seems it's a function that is a 2d array that for each element in the array this function adds another something/anything to the end
#then returns the list


def appendSomething(arr):
	#initialize var for the loop
	i = 0
	#start appending something to the list
	while i < len(arr):
		arr[i].append(something)
		i += 1
	#print(arr)
	return arr

#below used in actual implementation of the method
#arr = [[0,1],[2,3],[4,5]]
#something = 'hi'
#appendSomething(arr)