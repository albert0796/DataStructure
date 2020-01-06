一、	Hash Table流程圖
1.	建立Hash Table並決定其長度
 
2.	新增資料進入Hash Table
新增非數值型態資料「dog」進入Hash Table中。  
計算該資料須存放的位置: 以MD5編碼並將編碼結果轉成十進位，並將該數值除以Hash Table的長度求餘數。  
「dog」以MD5編碼並將編碼結果轉成十進位後為909720205502626453 5080901219663267845，除以Hash Table的長度求餘數為0。  
將「dog」存放至Hash Table的index=0的位置。  
   
新增非數值型態資料「pig」進入Hash Table中。  
「pig」 以MD5編碼並將編碼結果轉成十進位後為909720205502626 4535080901219663267845，除以Hash Table的長度求餘數為2。  
將「pig」存放至Hash Table的index=2的位置。  
   
新增非數值型態資料「cat」進入Hash Table中。  
「cat」 以MD5編碼並將編碼結果轉成十進位後為2771022202490735 55409885156483852860632，除以Hash Table的長度求餘數為2。  
將「cat」存放至Hash Table的index=2的位置。  
在index=2的位置發生Collision，利用Chaining的方法，使用Linked list將分在Hash Table中同一個index的資料串起來，將「cat」接在「pig」後面。  
   
3.	刪除Hash Table中資料
在Hash Table中刪除新增非數值型態資料「cat」。  
計算該資料須存放的位置: 以MD5編碼並將編碼結果轉成十進位，並將該數值除以Hash Table的長度求餘數。  
「cat」 以MD5編碼並將編碼結果轉成十進位後為2771022202490735 55409885156483852860632，除以Hash Table的長度求餘數為2。  
訪尋位於Hash Table 中index=2位置的Linkedlist，並刪除含有「cat」的node。  
  
4.	查找Hash Table中的資料
在Hash Table中查找非數值型態資料「cat」。  
計算該資料須存放的位置: 以MD5編碼並將編碼結果轉成十進位，並將該數值除以Hash Table的長度求餘數。  
「cat」 以MD5編碼並將編碼結果轉成十進位後為2771022202490735 55409885156483852860632，除以Hash Table的長度求餘數為2。  
訪尋位於Hash Table 中index=2位置的Linkedlist，並查找含有「cat」的node。如找到符合條件的node則返回 "cat" is in the hash table.。
