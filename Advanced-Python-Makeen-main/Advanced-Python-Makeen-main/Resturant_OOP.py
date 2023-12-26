class Resturant():
    def __init__(self,menu_items, book_table,customer_order):
        self.menu_items=menu_items
        self.book_table=book_table
        self.customer_order=customer_order
        
    def menu_items():
        menu_items=[]
        
        while True:
            order=input("Select Your Order: ")
            
            if order =="done":
                break
    
            menu_items.append(order)
        print(menu_items)
        
     def book_table():
         self.book_table=[[0]*3 for i in range(3)]
         for i in range(3):
             for j in range(3):
                 if book_table[i][j]==0:
                     print('the table is available')
                 elif book_table[i][j]>0:
                    print('the table is not available')
             
        
        
  
        

Resturant.menu_items()
  
    