from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
import time

user = " "
password = " "
cont = 0
cont2 = 0
cont3 = 1
while 1:
    if password != "123" or user != "user1":
        if cont >= 1:
            print("The user or password are incorrect, try again \n")
        elif cont == 4:
            print("Too many failed attempts, try again in 10 minutes")
            cont += 1
            time.sleep(600)
        elif cont == 7:
            print("You have no attempts left, so your account has been blocked")
            break
        print("User: ")
        user = input()
        print("Password: ")
        password = input()
        cont += 1
    else:
        print("\n---------------------------------------")
        print("Login success")
        print("---------------------------------------")
        id_category = [[product[0], product[3]] for product in lifestore_products]
        categorized_products = {}
        for product in id_category:
            product_id = product[0]
            category = product[1]
            if category not in categorized_products.keys():
                categorized_products[category] = []
            categorized_products[category].append(product_id)
        id_Sale = [[product[1], product[2]] for product in lifestore_sales]
        categorized_score = {}
        for sale in id_Sale:
            product_id = sale[0]
            review = sale[1]
            if product_id not in categorized_score.keys():
                categorized_score[product_id] = []
            categorized_score[product_id].append(review)
        sales_x_cat = {}
        for category in categorized_products.keys():
            products = categorized_products[category]
            reviews_cat = []
            profits = 0
            sales = 0
            for product_id in products:
                if product_id not in categorized_score.keys():
                    continue
                reviews = categorized_score[product_id]
                price = lifestore_products[product_id - 1][2]
                total = len(reviews)
                profits += total * price
                sales += total
                reviews_cat += reviews
            average = sum(reviews_cat) / len(reviews_cat)
            sales_x_cat[category] = {'average_review': average,
                                     'total_profits': profits,
                                     'total_sales': sales}
        print('\n Ventas por categoría \n')
        print("---------------------------------------")
        print("---------------------------------------")
        print('\n', sales_x_cat, '\n')
        print("---------------------------------------")
        print("---------------------------------------")
        sales_x_id = {}
        profits_id = 0
        sales_id = 0
        av_rev = []
        for product_id in categorized_score.keys():
            reviews_id = categorized_score[product_id]
            price_id = lifestore_products[product_id - 1][2]
            total_id = len(reviews_id)
            profits_id += total_id * price_id
            sales_id += total_id
            av_rev += reviews_id
            average = sum(av_rev) / len(av_rev)
            sales_x_id[product_id] = {'average_review': average,
                                      'total_profits': profits_id,
                                      'total_sales': sales_id}
        print('\n Ventas por producto \n')
        print("---------------------------------------")
        print("---------------------------------------")
        print('\n', sales_x_id, '\n')
        print("---------------------------------------")
        print("---------------------------------------")
        searches = {}
        for product_id in lifestore_searches:
            if product_id[1] not in searches.keys():
                searches[product_id[1]] = []
                if product_id[1] - cont3 in searches.keys():
                    searches[product_id[1] - cont3].append(cont2)
                    cont3 = 1
                else:
                    if product_id[1] > 1:
                        while product_id[1] - cont3 not in searches.keys():
                            cont3 += 1
                        searches[product_id[1] - cont3].append(cont2)
                        cont3 = 1
                cont2 = 0
            cont2 += 1
        searches[product_id[1]].append(cont2)
        search_list = list(searches.items())
        ord_searches = sorted(search_list, key=lambda x: x[1])
        most_searched = ord_searches[-10:]
        least_searched = ord_searches[0:10]
        print("\n Los productos más buscados fueron: \n")
        for i in range(9, -1, -1):
            print(most_searched[i])
        print("\n---------------------------------------")
        print("---------------------------------------")
        print("\n Los productos menos buscados fueron: \n")
        for i in range(0, 10):
            print(least_searched[i])
        id_sales = {}
        for product_id in sales_x_id.keys():
            if product_id not in id_sales.keys():
                id_sales[product_id] = []
            id_sales[product_id].append(sales_x_id[product_id].get('total_sales'))
        sales_list = list(id_sales.items())
        ord_sales = sorted(sales_list, key=lambda x: x[1])
        most_sales = ord_sales[-5:]
        least_sales = ord_sales[0:5]
        print("\n---------------------------------------")
        print("---------------------------------------")
        print("\n Los productos más vendidos fueron: \n")
        for i in range(4, -1, -1):
            print(most_sales[i])
        print("\n---------------------------------------")
        print("---------------------------------------")
        print("\n Los productos menos vendidos fueron: \n")
        for i in range(0, 5):
            print(least_sales[i])
        id_reviews = {}
        for product_id in sales_x_id.keys():
            if product_id not in id_reviews.keys():
                id_reviews[product_id] = []
            id_reviews[product_id].append(sales_x_id[product_id].get('average_review'))
        print("\n---------------------------------------")
        print("---------------------------------------")
        reviews_list = list(id_reviews.items())
        ord_reviews = sorted(reviews_list, key=lambda x: x[1])
        most_reviews = ord_reviews[-5:]
        least_reviews = ord_reviews[0:5]
        print("\n Los productos con mejor reseña fueron: \n")
        for i in range(4, -1, -1):
            print(most_reviews[i])
        print("\n---------------------------------------")
        print("---------------------------------------")
        print("\n Los productos con peor reseña fueron: \n")
        for i in range(0, 5):
            print(least_reviews[i])
        sales_date = [[product_id[3].split('/'), product_id[-1]] for product_id in lifestore_sales]
        sales_date_valid = [product_id[0] for product_id in sales_date if product_id[-1] == 0]
        sales_month = [int(product_id[1]) for product_id in sales_date_valid]
        month_sales_ord = sorted(sales_month)
        jan = 0
        feb = 0
        mar = 0
        apr = 0
        may = 0
        jun = 0
        jul = 0
        aug = 0
        sep = 0
        obr = 0
        nov = 0
        dec = 0
        for month in month_sales_ord:
            if month == 1:
                jan += 1
            elif month == 2:
                feb += 1
            elif month == 3:
                mar += 1
            elif month == 4:
                apr += 1
            elif month == 5:
                may += 1
            elif month == 6:
                jun += 1
            elif month == 7:
                jul += 1
            elif month == 8:
                aug += 1
            elif month == 9:
                sep += 1
            elif month == 10:
                obr += 1
            elif month == 11:
                nov += 1
            elif month == 12:
                dec += 1
        print("\n---------------------------------------")
        print("---------------------------------------")
        print("\n Las ventas por mes fueron: \n")
        print(jan, 'en enero')
        print(feb, 'en febrero')
        print(mar, 'en marzo')
        print(apr, 'en abril')
        print(may, 'en mayo')
        print(jun, 'en junio')
        print(jul, 'en julio')
        print(aug, 'en agosto')
        print(sep, 'en septiembre')
        print(obr, 'en octubre')
        print(nov, 'en noviembre')
        print(dec, 'en diciembre')
        total_profits = {}
        for product_id in sales_x_id.keys():
            total_profits[product_id] = sales_x_id[product_id].get('total_profits')
        year_profits = sum(list(total_profits.values()))
        months_with_sales = 0
        months_sales=[jan,feb,mar,apr,may,jun,jul,aug,sep,obr,nov,dec]
        for month in months_sales:
            if month >0:
                months_with_sales += 1
        prom = year_profits/months_with_sales
        print("\n---------------------------------------")
        print("---------------------------------------")
        print("\n Se vendieron un total de: \n")
        print(len(month_sales_ord), " productos en el año")
        print("$", year_profits, " en ganancias anuales")
        print("Con un promedio de: $", prom, " mensuales")

        break
