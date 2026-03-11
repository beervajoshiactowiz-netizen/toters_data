from parsel import Selector
import json
from pprint import pprint
def parser(raw_data: dict):

    selector = Selector(json.dumps(raw_data), type='json')
    result = []
    for item in selector.jmespath('data'):
        item_data={}
        item_data['id'] = item.jmespath('id').get()
        item_data['name'] = item.jmespath('title').get()
        item_data['original_price'] = item.jmespath('original_price').get()
        item_data['original_price_usd'] = item.jmespath('original_price_usd').get()
        item_data['category_id'] = item.jmespath('category_id').get()
        item_data['store_id'] = item.jmespath('store_id').get()
        item_data['store_item_id'] = item.jmespath('store_item_id').get()
        item_data['imgs'] = [item.jmespath('imgs').get()]
        item_data['final_price'] = item.jmespath('final_price').get()
        item_data['final_price_usd'] = item.jmespath('final_price_usd').get()
        item_data['local_currency'] = item.jmespath('local_currency').get()
        item_data['measurement_value'] = item.jmespath('measurement_value').get()
        item_data['measurement_unit'] = item.jmespath('measurement_unit').get()
        item_data['stock_level'] = item.jmespath('stock_level').get()
        item_data['is_available'] = item.jmespath('is_available').get()
        item_data['unavailable_until'] = item.jmespath('unavailable_until').get()
        item_data['reward_id'] = item.jmespath('reward.id').get()
        item_data['reward_points'] = item.jmespath('reward.points_cost').get()
        item_data['reward_tier'] = item.jmespath('reward.min_loyalty_tier.title').get()
        item_data['offers'] = item.jmespath('reward.offers').get()
        item_data["Diet"]=[]
        for i in item.jmespath('nutrition_facts.nutrition_info.diet_info.diets'):
            item_data["Diet"].append({
                'key': i.jmespath('key').get(),
                'name': i.jmespath('name').get(),
                'image': i.jmespath('image').get(),
                'selected': i.jmespath('selected').get(),
            })
        item_data["substance_free_diet"]=[]
        for i in item.jmespath('nutrition_facts.nutrition_info.diet_info.substance_free_diets'):
            item_data["substance_free_diet"].append({
                'key': i.jmespath('key').get(),
                'name': i.jmespath('name').get(),
                'image': i.jmespath('image').get(),
                'selected': i.jmespath('selected').get(),
            })
        item_data["allergies"]=[]
        for i in item.jmespath('nutrition_facts.nutrition_info.diet_info.allergies'):
            item_data["allergies"].append({
                'key': i.jmespath('key').get(),
                'name': i.jmespath('name').get(),
                'image': i.jmespath('image').get(),
                'selected': i.jmespath('selected').get(),
            })








        result.append(item_data)

    pprint(result)
    return result



