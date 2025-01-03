# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:56:08 2024

@author: murphy.465

Resources:
National Zoo - Meet the Animals
https://nationalzoo.si.edu/animals/list
"""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

results=pd.DataFrame(columns=['animal','description'])

animals=["abyssinian-ground-hornbill","addax","african-clawed-frog","african-pancake-tortoise","african-plated-lizard","aldabra-tortoise","allens-swamp-monkey","alligator-lizard","alligator-snapping-turtle","alpaca","american-alligator","american-avocet","american-bison","american-flamingo","american-oystercatcher","american-robin","american-wigeon","american-yellow-warbler","andean-bear","aquatic-caecilian","arapaima","asian-elephant","asian-small-clawed-otter","asian-water-dragon","australian-snake-necked-turtle","bald-eagle","baltimore-oriole","band-tailed-pigeon","banded-leporinus","banded-mongoose","banded-rock-rattlesnake","barred-owl","barred-parakeet","barred-tiger-salamander","beaver","bennets-wallaby","binturong","black-howler-monkey","black-pacu","black-and-white-ruffled-lemur","black-and-white-warbler","black-bellied-whistling-duck","black-capped-chickadee","black-crowned-night-heron","black-footed-ferret","black-necked-stilt","black-tailed-prairie-dog","black-throated-blue-warbler","black-throated-green-warbler","blue-crane","blue-grosbeak","blue-ground-dove","blue-billed-curassow","blue-winged-teal","boa-constrictor","bobcat","brazilian-rainbow-boa","brown-pelican","brush-tailed-bettong","bufflehead","burmese-rock-python","burrowing-owl","caiman-lizard","california-sea-lion","canvasback","caracal-lynx","carolina-wren","cedar-waxwing","chameloen-forest-dragon","channel-catfish","cheetah","chicken","chilean-rose-tarantula","chinese-alligator","chinese-crocodile-lizard","chinese-three-striped-box-turtle","clapper-rail","clouded-leopard","collard-brown-lemur","common-peafowl","common-raven","common-yellowthroat","corals-and-sea-anemones-anthozoa","corn-snake","coronated-tree-frog","cotton-top-tamarin","cow","crocodile-monitor","cuban-crocodile","dama-gazelle","damaraland-mole-rat","degu","dunlin","dwarf-mongoose","eastern-box-turtle","eastern-diamondback-rattlesnake","eastern-indigo-snake","eastern-newt","eastern-red-backed-salamander","eastern-screech-owl","elds-deer","electric-eel","emerald-tree-monitor","emperor-newt","emperor-tamarin","emu","eyelash-palm-pitviper","false-water-cobra","fennec-fox","fiji-banded-iguana","fishing-cat","flagtail-characin","fly-river-turtle","fowlers-toad","freshwater-stingray","gaboon-viper","geoffreys-marmoset","gharial","giant-anteater","giant-leaf-tailed-gecko","giant-panda","gila-monster","goat","goeldis-monkey","golden-lion-tamarin","golden-mantella-frog","golden-headed-lion-tamarin","goliath-bird-eating-tarantula","grand-cayman-blue-iguana","grasshopper-sparrow","gray-catbird","gray-seal","gray-tree-frog","gray-wolf","greater-madagascar-hedgehog-tenrec","greater-rhea","green-anaconda","green-aracari","green-crested-basilisk","green-mantella","green-salamander","green-tree-python","green-winged-macaw","green-winged-teal","grevys-zebra","guam-kingfisher","guam-rail","guinea-pig","harbor-seal","hartmanns-mountain-zebra","hawk-headed-parrot","hellbender","homes-hinge-back-tortoise","hooded-crane","hooded-merganswer","horshoe-crab","impressed-tortoise","indigo-bunting","iranian-fat-tailed-gecko","japanese-giant-salamander","japanese-koi","king-cobra","king-vulture","komodo-dragon","kori-bustard","kunekune-pig","la-plata-three-banded-armadillo","lance-head-rattlesnake","land-hermit-crab","larger-malay-mouse-deer","lemur-leaf-frog","lesser-kudu","lesser-madagascar-hedgehog-tenrec","lion","loggerhead-shrike","long-tailed-chinchilla","long-tailed-salamander","madagascar-giant-day-gecko","magnolia-warbler","malagasy-giant-jumping-rat","maned-wolf","mangrove-snake","matamata-turtle","meerkat","mellers-chameloen","miniature-donkey","mummichog","naked-mole-rat","new-caledonian-gecko","north-american-porcupine","north-american-river-otter","north-island-brown-kiwi","northern-copperhead","northern-luzon-giant-cloud-rat","northern-mockingbird","northern-pine-snake","northern-pintail","northern-red-salamander","northern-shoveler","northern-snakehead-fish","northern-tree-shrew","norway-rat","orangutan","orchard-oriole","oriental-fire-bellied-toad","ossabaw-island-hog","ostrich","ovenbird","painted-river-terrapin","pale-headed-saki-monkey","pallas-cat","palm-warbler","panamanian-golden-frog","patagonian-mara","perdido-key-beach-mouse","persian-onager","philippine-crocodile","pink-toed-tarantula","plain-chachalaca","poison-frogs","prehensile-tailed-porcupine","prevosts-squirrel","przewalskis-horse","puff-adder","pumpkinseed","pygmy-slow-loris","radiated-tortoise","red-knot","red-panda","red-river-hog","red-ruffed-lemur","red-siskin","red-wolf","red-bellied-piranha","red-crested-cardinal","red-crowned-crane","red-eyed-vireo","red-footed-tortoise","red-fronted-lemur","red-rumped-agouti","red-winged-blackbird","redhead","rhinoceros-snake","ring-tailed-lemur","rock-cavy","rock-hyrax","rose-breasted-grosbeak","roseate-spoonbill","rosss-goose",
"ruby-throated-hummingbird","ruddy-duck","ruddy-quail-dove","ruddy-turnstone","rufous-collared-sparrow","rufous-crowned-sparrow","ruppells-griffon-vulture","sand-cat","sanderling","sandhill-crane","scarlet-ibis","scarlet-tanager","schmidts-red-tailed-monkey","scimitar-horned-oryx","screaming-hairy-armadillo","semipalmated-plover","semipalmated-sandpiper","short-billed-dowitcher","short-eared-elephant-shrew","siamang","silver-arowana","sinaloan-milksnake","sitatunga","sloth-bear","smallwoods-anole","smooth-sided-toad","song-sparrow","southern-cassowary","southern-lesser-galago","southern-swamp-sparrow","southern-tamandua","spider-tortoise","spiny-tailed-monitor","spotted-pond-turtle","striped-hermit-crab","striped-skunk","suckermouth-catfish","sunbittern","swainsons-thrush","tanagers","taylors-cantil","tennessee-warbler","tentacled-snake","tiger","timber-rattlesnake","timor-python","titi-monkey","tokay-gecko","tomato-frog","tomistoma","turkey","twig-catfish","two-toed-sloth","vietamese-mossy-frog","virginia-opossum","von-der-dekens-hornbill","western-lowland-gorilla","whites-tree-frog","white-cheeked-gibbon","white-eyed-vireo","white-naped-crane","white-nosed-coati","white-throated-sparrow","whooping-crane","wood-duck","wood-thrush","yellow-breasted-chat","yellow-rumped-warbler","yellow-spotted-amazon-river-turtle"]


##### Start by looking at one website first
url='https://nationalzoo.si.edu/animals/abyssinian-ground-hornbill'
xml_data = requests.get(url).content
soup = bs(xml_data, 'lxml')
animal_name=soup.find_all("h2", attrs={"class":"block-title border-animals"})

### YUK - Just use the animal name from the list, but clean up ####
animal='abyssinian-ground-hornbill'
animal=animal.replace('-', ' ').strip().title()
print(animal)
paragraphs=soup.find_all("p")
# print(paragraphs)
all_paragraphs=[]
for each_p in paragraphs:
    paragraph=each_p.text
    all_paragraphs.append(paragraph)
    # print(paragraph)
# print(all_paragraphs)
all_paragraphs=', '.join(all_paragraphs)
# print(all_paragraphs)
lookup="About the Smithsonian Conservation Biology Institute, (.*) Giant pandas"
description=re.findall(lookup, all_paragraphs)
description=description[0]
description=description.replace('.,','.')
print(description)

entry={
        'animal':animal,
        'description':description}
df_entry=pd.DataFrame(entry, index=[0])
results=pd.concat([df_entry, results], axis=0)


####Now put everything together
# for animal in animals:
#     lookup=animal
#     animal=animal.replace('-', ' ').strip().title()
#     print(animal)
#     url='https://nationalzoo.si.edu/animals/'+lookup
#     xml_data = requests.get(url).content
#     soup = bs(xml_data, 'lxml')
#     paragraphs=soup.find_all("p")
#     # print(paragraphs)
#     all_paragraphs=[]
#     try:
#         for each_p in paragraphs:
#             paragraph=each_p.text
#             all_paragraphs.append(paragraph)
#             # print(paragraph)
#         # print(all_paragraphs)
#         all_paragraphs=', '.join(all_paragraphs)
#         # print(all_paragraphs)
#         lookup="About the Smithsonian Conservation Biology Institute, (.*) Giant pandas"
#         description=re.findall(lookup, all_paragraphs)
#         description=description[0]
#         description=description.replace('.,','.')
#         print(description)
#     except:
#         description="not found"
    
#     entry={
#             'animal':animal,
#             'description':description}
#     df_entry=pd.DataFrame(entry, index=[0])
#     results=pd.concat([df_entry, results], axis=0)





