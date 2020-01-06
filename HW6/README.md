[Dijkstra與Kruskal流程圖、程式碼學習歷程與Dijkstra與Kruskal原理說明](https://github.com/albert0796/DSA/blob/master/HW6/Dijkstra%E8%88%87Kruskal%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E7%A8%8B%E5%BC%8F%E7%A2%BC%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87Dijkstra%E8%88%87Kruskal%E5%8E%9F%E7%90%86%E8%AA%AA%E6%98%8E.pdf)
  
Dijkstra與Kruskal原理說明  
  
Shortest Path  
想要知道從高雄到台南，如果開車的話，通常會利用查詢的交通網路來取得: 最短路徑或者走哪一條路最符合經濟效益。諾以圖形網路來思考，就是任意兩個頂點之間的最短路徑或最少花費。
  
Dijkstra Algorithm  
該方法用於計算由某個頂點到其他頂點的最短路徑。  
D[k] = A[F, k], (k = 1, N)  
S = {F}, V = {1, 2, ……, N}  
	A[F, k] 為頂點F到k的距離。  
	D為一個N維陣列用來存放某一頂點到所有頂點的最短距離。  
	F表示起始頂點，V是網路中所有頂點的集合。  
	S也是頂點的集合。   
1.	從V – S集合中找到一個頂點x，使得D(x)為最小值，並把x放入S集合中。  
2.	依D[k] = min(D[k], D[x] + A[x, k])來調整陣列D得值。  
該方法具有下列幾項特性:  
1.	如果u是目前所找到最短路徑之下一個節點，則u必屬於V-S集合中最小花費成本的邊。 
2.	若u被選中，將u加入S集合中，則產生目前由起始點到u的最短路徑。
  
Minimum Spanning Tree (MST)  
Spanning Tree 需滿足三個條件:   
1. 連結所有Graph中的vertex (點)的樹。
2. 沒有cycle，代表一個vertex只能有一個root。
3.若Graph有V個vertex，Spanning Tree只有|V|−1條edge。
如圖一，考慮一個connected、weighted的undirected graph，相同的vertex會有不同的Spanning Tree，如圖二、三皆為其Spanning Tree的寫法。
   
由於Graph具有weight，因此，不同的Spanning Tree，可能有不同的weight總和，而其中，具有最小weight總和的樹，稱為Minimum Spanning Tree (MST)。MST有很多實際應用。將網路頂點看做城市，邊看做連線城市的通訊網，邊的權重看做連線城市的通訊線路的成本，根據最小生成樹建立的通訊網就是這些城市之間成本最低的通訊網。其中如果有相同權值的邊線時，MST並非唯一；如邊線的權值均不同，則MST唯一。
  
Kruskal Algorithm  
Kruskal Algorithm為建立MST的其中一種方法。該演算法將各邊線依權值大小由小到大排列，從權值最低的邊線開始架構MST，依序拿最小成本的邊來搭建MST，如果加入的邊線會造成迴路則捨棄不用，直到加入了|V|−1條邊線為止。
  
  
