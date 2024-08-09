def sales_data(filename):
  total_items_sold = 0
  total_discounts = 0
  total_taxes = 0
  total_sales = 0

  with open(filename, 'r') as file:
      for line in file:
          sale = eval(line)

          item = sale['item']
          quantity = sale['quantity']
          price_per_unit = sale['price_per_unit']
          discount = sale['discount']
          tax_rate = sale['tax_rate']

          gross_amount = quantity * price_per_unit
          discount_amount = gross_amount * discount
          net_amount = gross_amount - discount_amount
          tax_amount = net_amount * tax_rate
          final_amount = net_amount + tax_amount

          print(f"Item: {item}")
          print(f"Quantity sold: {quantity}")
          # .2f is used to hold two values after decimal
          print(f"Gross amount : ${gross_amount:.2f}")
          print(f"Discount amount: ${discount_amount:.2f}")
          print(f"Net amount: ${net_amount:.2f}")
          print(f"Tax amount: ${tax_amount:.2f}")
          print(f"Final amount: ${final_amount:.2f}")
          print("-" * 50)

          total_items_sold += quantity
          total_discounts += discount_amount
          total_taxes += tax_amount
          total_sales += final_amount

  print("Summary Report")
  print("=" * 30)
  print(f"Total number of items sold: {total_items_sold}")
  print(f"Total discounts: ${total_discounts:.2f}")
  print(f"Total taxes collected: ${total_taxes:.2f}")
  print(f"Total sales amount: ${total_sales:.2f}")

sales_data('sample.txt')
