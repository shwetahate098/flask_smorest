from flask import Flask, request

app=Flask(__name__)

stores = [
    {"name": "Shweta",
      "items": 
     [
         {"name": "my item",
           "price": 15.99}
    ]   
     }
     ]



@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.post("/store/<string:name>/item")
def create_item(name): #shweta
    request_data = request.get_json()
    for store in stores: 
        ##{"name": "Shweta",  "items"  [         {"name": "my item",           "price": 15.99}    ]    }
        if store["name"] == name: #shweta
            ##   {"name": "Abhishek",           "price": 15.99}    ]   
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item
    return {"message": "Store not found"}, 404

@app.post("/store")
def create_store():
    request_data = request.get_json()
        ##request_data = {"name": "Shweta",  "items"  :[         {"name": "my item",           "price": 15.99}    ]    }
    new_store = {"name": request_data["name"], "items": request_data["items"]}
    stores.append(new_store)
    return new_store, 201

##particular store name
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404

#item base pe
@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        ##{"name": "Shweta",  "items"  [         {"name": "my item",           "price": 15.99}    ]    }

        if store["name"] == name:
        ##{"name": "Shweta",  "items"  [         {"name": "my item",           "price": 15.99}    ]    }

            return {"items": store["items"],
                    "name":store["name"]
            }
    return {"message": "Store not found"}, 404

@app.route('/')
def bubble():
    return 'hi'

if __name__=='__main__':
    app.run(debug=True)