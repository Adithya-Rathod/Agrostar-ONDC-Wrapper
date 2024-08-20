def createItem(catalog):
    id = catalog.get("skuCode") 
    rating = catalog.get("rating", {}).get("average")
    descriptor = {
        "name" : catalog.get("productName"),
        "short_desc" : catalog.get("displayMessage"),
        "image" : [i.get("name") for i in catalog.get("productImages")]
    }
    category_id = catalog.get("productGroup")
    price = {
        "currency" : "INR",
        "value" : catalog.get("sellingPrice"),
        "maximum_value" : catalog.get("mrp"),
        
    }
    item = {
        "id" : id,
        "descriptor" : descriptor,
        "rating" : rating,
        "category_id" : category_id,
        "price"  : price,
    }
    return item

def getItems(catalog):
    items = []
    for dic in catalog:
        items.append(createItem(dic))
        for alt in dic.get("alternateProductWithSimilarChemicalComposition", []):
            items.append(createItem(alt))
    return items