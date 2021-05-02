# To calculate Average order Value, we would calculate the total sales amount divided by the order count

def main():
    with open("2019 Winter Data Science Intern Challenge Data Set - Sheet1.tsv", "r") as fd:

        total_sales = 0
        order_count = 0
        fd.readline()

        for currLine in fd:

            order_id, shop_id, user_id, order_amount, total_items, payment_method, date, time = currLine.split()

            order_amount = int(order_amount)
            total_items = int(total_items)

            order_count += total_items
            total_sales += order_amount

        print("AOV is", total_sales/order_count)

if __name__ == "__main__":
	main()