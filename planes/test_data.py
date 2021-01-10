URL = 'https://api.scryfall.com/cards/search?q=t:plane%20or%20t:phenomenon'

PLANES_RESPONSE = '''
{
  "object": "list",
  "total_cards": 78,
  "has_more": false,
  "data": [
    {
      "object": "card",
      "id": "ed4f4210-9871-4cec-9b46-100c80f93cd4",
      "oracle_id": "15b979de-c8ee-4664-9ca7-6c4eb3346967",
      "multiverse_ids": [
        423590
      ],
      "tcgplayer_id": 125570,
      "cardmarket_id": 294404,
      "name": "Academy at Tolaria West",
      "lang": "en",
      "released_at": "2018-12-25",
      "uri": "https://api.scryfall.com/cards/ed4f4210-9871-4cec-9b46-100c80f93cd4",
      "scryfall_uri": "https://scryfall.com/card/opca/9/academy-at-tolaria-west?utm_source=api",
      "layout": "planar",
      "highres_image": true,
      "image_uris": {
        "small": "https://c1.scryfall.com/file/scryfall-cards/small/front/e/d/ed4f4210-9871-4cec-9b46-100c80f93cd4.jpg?1547432274",
        "normal": "https://c1.scryfall.com/file/scryfall-cards/normal/front/e/d/ed4f4210-9871-4cec-9b46-100c80f93cd4.jpg?1547432274",
        "large": "https://c1.scryfall.com/file/scryfall-cards/large/front/e/d/ed4f4210-9871-4cec-9b46-100c80f93cd4.jpg?1547432274",
        "png": "https://c1.scryfall.com/file/scryfall-cards/png/front/e/d/ed4f4210-9871-4cec-9b46-100c80f93cd4.png?1547432274",
        "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/front/e/d/ed4f4210-9871-4cec-9b46-100c80f93cd4.jpg?1547432274",
        "border_crop": "https://c1.scryfall.com/file/scryfall-cards/border_crop/front/e/d/ed4f4210-9871-4cec-9b46-100c80f93cd4.jpg?1547432274"
      },
      "mana_cost": "",
      "cmc": 0.0,
      "type_line": "Plane — Dominaria",
      "oracle_text": "At the beginning of your end step, if you have no cards in hand, draw seven cards.\\nWhenever you roll {CHAOS}, discard your hand.",
      "colors": [

      ],
      "color_identity": [

      ],
      "keywords": [

      ],
      "legalities": {
        "standard": "not_legal",
        "future": "not_legal",
        "historic": "not_legal",
        "gladiator": "not_legal",
        "pioneer": "not_legal",
        "modern": "not_legal",
        "legacy": "not_legal",
        "pauper": "not_legal",
        "vintage": "not_legal",
        "penny": "not_legal",
        "commander": "not_legal",
        "brawl": "not_legal",
        "duel": "not_legal",
        "oldschool": "not_legal",
        "premodern": "not_legal"
      },
      "games": [
        "paper"
      ],
      "reserved": false,
      "foil": false,
      "nonfoil": true,
      "oversized": true,
      "promo": false,
      "reprint": true,
      "variation": false,
      "set": "opca",
      "set_name": "Planechase Anthology Planes",
      "set_type": "planechase",
      "set_uri": "https://api.scryfall.com/sets/ada3345c-d416-49bc-92e0-73363ddee5c8",
      "set_search_uri": "https://api.scryfall.com/cards/search?order=set&q=e%3Aopca&unique=prints",
      "scryfall_set_uri": "https://scryfall.com/sets/opca?utm_source=api",
      "rulings_uri": "https://api.scryfall.com/cards/ed4f4210-9871-4cec-9b46-100c80f93cd4/rulings",
      "prints_search_uri": "https://api.scryfall.com/cards/search?order=released&q=oracleid%3A15b979de-c8ee-4664-9ca7-6c4eb3346967&unique=prints",
      "collector_number": "9",
      "digital": false,
      "rarity": "common",
      "card_back_id": "7840c131-f96b-4700-9347-2215c43156e6",
      "artist": "James Paick",
      "artist_ids": [
        "1a7be0a2-d8ac-45c7-b0a0-eb0886f47b5f"
      ],
      "illustration_id": "8d617a18-0f09-4471-8ac6-f0928f1f9912",
      "border_color": "black",
      "frame": "2015",
      "full_art": false,
      "textless": false,
      "booster": false,
      "story_spotlight": false,
      "prices": {
        "usd": "1.54",
        "usd_foil": null,
        "eur": null,
        "eur_foil": null,
        "tix": null
      },
      "related_uris": {
        "gatherer": "https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=423590",
        "tcgplayer_decks": "https://decks.tcgplayer.com/magic/deck/search?contains=Academy+at+Tolaria+West&page=1&utm_campaign=affiliate&utm_medium=api&utm_source=scryfall",
        "edhrec": "https://edhrec.com/route/?cc=Academy+at+Tolaria+West",
        "mtgtop8": "https://mtgtop8.com/search?MD_check=1&SB_check=1&cards=Academy+at+Tolaria+West"
      },
      "purchase_uris": {
        "tcgplayer": "https://shop.tcgplayer.com/product/productsearch?id=125570&utm_campaign=affiliate&utm_medium=api&utm_source=scryfall",
        "cardmarket": "https://www.cardmarket.com/en/Magic/Products/Search?referrer=scryfall&searchString=Academy+at+Tolaria+West&utm_campaign=card_prices&utm_medium=text&utm_source=scryfall",
        "cardhoarder": "https://www.cardhoarder.com/cards?affiliate_id=scryfall&data%5Bsearch%5D=Academy+at+Tolaria+West&ref=card-profile&utm_campaign=affiliate&utm_medium=card&utm_source=scryfall"
      }
    },
    {
      "object": "card",
      "id": "6caf8b21-1807-442c-a461-c89c7591df70",
      "oracle_id": "38f84e55-049c-441e-b4e2-1e207ab5dbe5",
      "multiverse_ids": [
        423592
      ],
      "tcgplayer_id": 125571,
      "cardmarket_id": 294406,
      "name": "Agyrem",
      "lang": "en",
      "released_at": "2018-12-25",
      "uri": "https://api.scryfall.com/cards/6caf8b21-1807-442c-a461-c89c7591df70",
      "scryfall_uri": "https://scryfall.com/card/opca/11/agyrem?utm_source=api",
      "layout": "planar",
      "highres_image": true,
      "image_uris": {
        "small": "https://c1.scryfall.com/file/scryfall-cards/small/front/6/c/6caf8b21-1807-442c-a461-c89c7591df70.jpg?1547432309",
        "normal": "https://c1.scryfall.com/file/scryfall-cards/normal/front/6/c/6caf8b21-1807-442c-a461-c89c7591df70.jpg?1547432309",
        "large": "https://c1.scryfall.com/file/scryfall-cards/large/front/6/c/6caf8b21-1807-442c-a461-c89c7591df70.jpg?1547432309",
        "png": "https://c1.scryfall.com/file/scryfall-cards/png/front/6/c/6caf8b21-1807-442c-a461-c89c7591df70.png?1547432309",
        "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/front/6/c/6caf8b21-1807-442c-a461-c89c7591df70.jpg?1547432309",
        "border_crop": "https://c1.scryfall.com/file/scryfall-cards/border_crop/front/6/c/6caf8b21-1807-442c-a461-c89c7591df70.jpg?1547432309"
      },
      "mana_cost": "",
      "cmc": 0.0,
      "type_line": "Plane — Ravnica",
      "oracle_text": "Whenever a white creature dies, return it to the battlefield under its owner's control at the beginning of the next end step.\\nWhenever a nonwhite creature dies, return it to its owner's hand at the beginning of the next end step.\\nWhenever you roll {CHAOS}, creatures can't attack you until a player planeswalks.",
      "colors": [

      ],
      "color_identity": [

      ],
      "keywords": [

      ],
      "legalities": {
        "standard": "not_legal",
        "future": "not_legal",
        "historic": "not_legal",
        "gladiator": "not_legal",
        "pioneer": "not_legal",
        "modern": "not_legal",
        "legacy": "not_legal",
        "pauper": "not_legal",
        "vintage": "not_legal",
        "penny": "not_legal",
        "commander": "not_legal",
        "brawl": "not_legal",
        "duel": "not_legal",
        "oldschool": "not_legal",
        "premodern": "not_legal"
      },
      "games": [
        "paper"
      ],
      "reserved": false,
      "foil": false,
      "nonfoil": true,
      "oversized": true,
      "promo": false,
      "reprint": true,
      "variation": false,
      "set": "opca",
      "set_name": "Planechase Anthology Planes",
      "set_type": "planechase",
      "set_uri": "https://api.scryfall.com/sets/ada3345c-d416-49bc-92e0-73363ddee5c8",
      "set_search_uri": "https://api.scryfall.com/cards/search?order=set&q=e%3Aopca&unique=prints",
      "scryfall_set_uri": "https://scryfall.com/sets/opca?utm_source=api",
      "rulings_uri": "https://api.scryfall.com/cards/6caf8b21-1807-442c-a461-c89c7591df70/rulings",
      "prints_search_uri": "https://api.scryfall.com/cards/search?order=released&q=oracleid%3A38f84e55-049c-441e-b4e2-1e207ab5dbe5&unique=prints",
      "collector_number": "11",
      "digital": false,
      "rarity": "common",
      "card_back_id": "7840c131-f96b-4700-9347-2215c43156e6",
      "artist": "Todd Lockwood",
      "artist_ids": [
        "d0b9f3cc-13fb-42b6-bc43-b034728e5c7b"
      ],
      "illustration_id": "995f5b3f-7988-4eb5-9335-284f5c3a1e10",
      "border_color": "black",
      "frame": "2015",
      "full_art": false,
      "textless": false,
      "booster": false,
      "story_spotlight": false,
      "prices": {
        "usd": "1.97",
        "usd_foil": null,
        "eur": "0.25",
        "eur_foil": null,
        "tix": null
      },
      "related_uris": {
        "gatherer": "https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=423592",
        "tcgplayer_decks": "https://decks.tcgplayer.com/magic/deck/search?contains=Agyrem&page=1&utm_campaign=affiliate&utm_medium=api&utm_source=scryfall",
        "edhrec": "https://edhrec.com/route/?cc=Agyrem",
        "mtgtop8": "https://mtgtop8.com/search?MD_check=1&SB_check=1&cards=Agyrem"
      },
      "purchase_uris": {
        "tcgplayer": "https://shop.tcgplayer.com/product/productsearch?id=125571&utm_campaign=affiliate&utm_medium=api&utm_source=scryfall",
        "cardmarket": "https://www.cardmarket.com/en/Magic/Products/Search?referrer=scryfall&searchString=Agyrem&utm_campaign=card_prices&utm_medium=text&utm_source=scryfall",
        "cardhoarder": "https://www.cardhoarder.com/cards?affiliate_id=scryfall&data%5Bsearch%5D=Agyrem&ref=card-profile&utm_campaign=affiliate&utm_medium=card&utm_source=scryfall"
      }
    },
    {
      "object": "card",
      "id": "a1c7f2eb-0654-46f9-ae3d-11efcac837b8",
      "oracle_id": "25650a32-4014-4065-ad01-7357c3ad3995",
      "multiverse_ids": [
        423593
      ],
      "tcgplayer_id": 125572,
      "cardmarket_id": 294407,
      "name": "Akoum",
      "lang": "en",
      "released_at": "2018-12-25",
      "uri": "https://api.scryfall.com/cards/a1c7f2eb-0654-46f9-ae3d-11efcac837b8",
      "scryfall_uri": "https://scryfall.com/card/opca/12/akoum?utm_source=api",
      "layout": "planar",
      "highres_image": true,
      "image_uris": {
        "small": "https://c1.scryfall.com/file/scryfall-cards/small/front/a/1/a1c7f2eb-0654-46f9-ae3d-11efcac837b8.jpg?1547432330",
        "normal": "https://c1.scryfall.com/file/scryfall-cards/normal/front/a/1/a1c7f2eb-0654-46f9-ae3d-11efcac837b8.jpg?1547432330",
        "large": "https://c1.scryfall.com/file/scryfall-cards/large/front/a/1/a1c7f2eb-0654-46f9-ae3d-11efcac837b8.jpg?1547432330",
        "png": "https://c1.scryfall.com/file/scryfall-cards/png/front/a/1/a1c7f2eb-0654-46f9-ae3d-11efcac837b8.png?1547432330",
        "art_crop": "https://c1.scryfall.com/file/scryfall-cards/art_crop/front/a/1/a1c7f2eb-0654-46f9-ae3d-11efcac837b8.jpg?1547432330",
        "border_crop": "https://c1.scryfall.com/file/scryfall-cards/border_crop/front/a/1/a1c7f2eb-0654-46f9-ae3d-11efcac837b8.jpg?1547432330"
      },
      "mana_cost": "",
      "cmc": 0.0,
      "type_line": "Plane — Zendikar",
      "oracle_text": "Players may cast enchantment spells as though they had flash.\\nWhenever you roll {CHAOS}, destroy target creature that isn't enchanted.",
      "colors": [

      ],
      "color_identity": [

      ],
      "keywords": [

      ],
      "legalities": {
        "standard": "not_legal",
        "future": "not_legal",
        "historic": "not_legal",
        "gladiator": "not_legal",
        "pioneer": "not_legal",
        "modern": "not_legal",
        "legacy": "not_legal",
        "pauper": "not_legal",
        "vintage": "not_legal",
        "penny": "not_legal",
        "commander": "not_legal",
        "brawl": "not_legal",
        "duel": "not_legal",
        "oldschool": "not_legal",
        "premodern": "not_legal"
      },
      "games": [
        "paper"
      ],
      "reserved": false,
      "foil": false,
      "nonfoil": true,
      "oversized": true,
      "promo": false,
      "reprint": true,
      "variation": false,
      "set": "opca",
      "set_name": "Planechase Anthology Planes",
      "set_type": "planechase",
      "set_uri": "https://api.scryfall.com/sets/ada3345c-d416-49bc-92e0-73363ddee5c8",
      "set_search_uri": "https://api.scryfall.com/cards/search?order=set&q=e%3Aopca&unique=prints",
      "scryfall_set_uri": "https://scryfall.com/sets/opca?utm_source=api",
      "rulings_uri": "https://api.scryfall.com/cards/a1c7f2eb-0654-46f9-ae3d-11efcac837b8/rulings",
      "prints_search_uri": "https://api.scryfall.com/cards/search?order=released&q=oracleid%3A25650a32-4014-4065-ad01-7357c3ad3995&unique=prints",
      "collector_number": "12",
      "digital": false,
      "rarity": "common",
      "card_back_id": "7840c131-f96b-4700-9347-2215c43156e6",
      "artist": "Rob Alexander",
      "artist_ids": [
        "35906871-6c78-4ab2-9ed1-e6792c8efb74"
      ],
      "illustration_id": "0d0681f8-ecba-4289-ac18-2292b9dc9c0b",
      "border_color": "black",
      "frame": "2015",
      "full_art": false,
      "textless": false,
      "booster": false,
      "story_spotlight": false,
      "prices": {
        "usd": "0.83",
        "usd_foil": null,
        "eur": "0.24",
        "eur_foil": null,
        "tix": null
      },
      "related_uris": {
        "gatherer": "https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=423593",
        "tcgplayer_decks": "https://decks.tcgplayer.com/magic/deck/search?contains=Akoum&page=1&utm_campaign=affiliate&utm_medium=api&utm_source=scryfall",
        "edhrec": "https://edhrec.com/route/?cc=Akoum",
        "mtgtop8": "https://mtgtop8.com/search?MD_check=1&SB_check=1&cards=Akoum"
      },
      "purchase_uris": {
        "tcgplayer": "https://shop.tcgplayer.com/product/productsearch?id=125572&utm_campaign=affiliate&utm_medium=api&utm_source=scryfall",
        "cardmarket": "https://www.cardmarket.com/en/Magic/Products/Search?referrer=scryfall&searchString=Akoum&utm_campaign=card_prices&utm_medium=text&utm_source=scryfall",
        "cardhoarder": "https://www.cardhoarder.com/cards?affiliate_id=scryfall&data%5Bsearch%5D=Akoum&ref=card-profile&utm_campaign=affiliate&utm_medium=card&utm_source=scryfall"
      }
    }
  ]
}
'''