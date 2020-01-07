## 232. Implement Queue using Stacks
  
## 700. Search in a Binary Search Tree
從樹根開始向下搜尋，當欲搜尋的數值小於根節點時就往根節點左方走
訪；大於根節點時 就往根節點右方走訪。直到找到欲搜尋的數值為止。
如已走訪到最後的葉節點但仍未找到數值，則代表欲搜尋的數值並未在
二原搜尋樹中。  

## 705. Design Hash Set
1. 建立 Hash Table 並決定其長度。
2. 新增數值型態資料進入 Hash Table 中，決定資料再Hash Table中index的位置，key = index。若發生 Collision 的情況，很可能有多個 Key被分在Hash Table 中同一個 index ，此時就可以利用 Chaining 的方法， 使用 Linked list 把被分在 Hash Table 中同一個 index 的 Key 值串起來。  
Add : 先利用 Hash Function 取得 Table 的 index ，接著再利用 addAtTail每個資料依序串起來。  
Contains: 先利用 Hash Function 取得 Table 的 index ，接著再利用 Search 找到欲查找的資料。  
Remove: 先利用 Hash Function 取得 Table的 index ，接著再 利用 Delete 刪除欲刪除的資料。  

## 707. Design Linked List
Linked list(鏈結串列)是一種常見的資料結構，其使用node(節點)來記錄、表示、儲存資料(data)，並利用每個node中的pointer指向下一個node，藉此將多個node串連起來，形成Linked list，並以NULL來代表Linked list的終點。  
Linked List 是由「節點」(Node)組成的有序串列集合，節點又稱串列節點(List Node)。每一個節點至少包含一個「資料欄」(Data Field)和「鏈結欄」(Linked Field)。  
鏈結串列加入或刪除一個節點非常方便，不需要大幅搬動資料，只要改變鏈結的指標即可。
## 912. Sort an Array
利用Heap Sort進行排序。  
Heap Sort的原理是先將數列排成堆積樹的形態，將位於樹根節點的數值與位於最後一個子節點的數值對調，再將對掉到最後一個子節點的數值剔除，作為新數列的第一順位，完成一次的Heap Sort排列。接著，因為原本堆積樹型態的數列已經剔除了位於最後一個節點的數值並且原本位於樹根的數值也被移往最後一個節點的位置，因此原本堆積樹的型態已被破壞掉，此時將位於數根的數值向下依序與其較小的子節點比較，當該數值大於子節點時，兩數值則互換，互換後原位於數根的數值再繼續與更下層較小的子節點比較，直到比到最後一個節點為止，全部比較完後再將位於樹根節點的數值與位於最後一個子節點的數值對調，並將對調到最後一個子節點的數值剔除，排進新數列的第二順位。以此類堆，直到堆積樹型態的數列的數值完全被剔除，都被排到新數列中。而此時的新數列將會是一個經大小排序過的數列。  
以Min Heap Tree為例，堆積樹的型態分成根節點、父節點、子節點三個元素。根節點為該數列的最小值並且位於數量的首端，而每個父節點底下連接最多兩個，最少一個子節點，並且父節點的數值必須小於子節點的數值。
