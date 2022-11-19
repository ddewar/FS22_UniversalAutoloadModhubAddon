#!/usr/bin/env python3

#python -m pip install beautifulsoup4 
#pip3 install lxml beautifulsoup4  

import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup

class ModHubObject:
    def __init__(self):
        self.enableRearLoading = False
        self.enableSideLoading = False
        self.isBaleTrailer = False
        self.isTimberTrailer = False
        self.isBoxTrailer = False
        self.isCurtainTrailer = False
        self.noLoadingIfFolded = False
        self.noLoadingIfUnfolded = False
        self.noLoadingIfCovered = False
        self.noLoadingIfUncovered = False
        self.rearUnloadingOnly = False
        self.frontUnloadingOnly = False
        self.disableAutoStrap = False
        self.disableHeightLimit = False
        self.zonesOverlap = False
        self.showDebug = False
        self.horizontalLoading = False

    def options_list(self):
        return {
            'enableRearLoading': 'Rear Loading',
            'enableSideLoading': 'Side Loading',
            'isBaleTrailer': 'Bale Trailer',
            'isTimberTrailer': 'Timber Trailer',
            'isBoxTrailer': 'Box Trailer',
            'isCurtainTrailer': 'Curtain Trailer',
            'noLoadingIfFolded': 'No Loading When Folded',
            'noLoadingIfUnfolded': 'No Loading When Unfolded',
            'noLoadingIfCovered': 'No Loading When Coverd',
            'noLoadingIfUncovered': 'No Loading When Uncovered',
            'rearUnloadingOnly': 'Read Unloading Only',
            'frontUnloadingOnly': 'Front Unloading Only',
            'disableAutoStrap': 'Autostrap Disabled',
            'disableHeightLimit': 'Height Limit Disabled',
            'zonesOverlap': 'Overlapping Zones',
            'showDebug': 'Showing Debug',
            'horizontalLoading': 'Horizontal Loading',
        }

    def tableRow(self):
        return f'[{self.title}]({self.url}) | {self.author} | {self.number_areas} | {self.options()}' + '\n'

    def options(self):
        options = []
        for k,v in self.options_list().items():
            if getattr(self, k):
                options.append(v)
        return ', '.join(options)

xmlFile = ET.parse('config/SupportedVehicles.xml')
readMeRawData = 'readMeRawData.md'

with open(readMeRawData, 'w') as out:
    out.write('Title | Author | Loading Areas | Options' + '\n'  + '---|---|:---:|---' + '\n')
    for x in xmlFile.getroot()[0]:
        if 'modHubId' in x.attrib:
            mho = ModHubObject()
            mho.modFileName = x.attrib['configFileName']
            mho.modHubId = x.attrib['modHubId']
            print(f'Getting ModHub info for {mho.modHubId}')

            mho.url = f'https://www.farming-simulator.com/mod.php?mod_id={mho.modHubId}&title=fs2022'
            page = requests.get(mho.url)

            soup = BeautifulSoup(page.content, "html.parser")

            if not soup.find("h2", "column title-label"):
                print(f'Skipping {mho.modHubId}')
                continue
            mho.title = soup.find("h2", "column title-label").text
            mho.category = soup.find("div", "table table-game-info").findAll('div', "table-row")[2].findAll("div")[1].text
            mho.author = soup.find("div", "table table-game-info").findAll('div', "table-row")[3].findAll("div")[1].text
            mho.number_areas = len(x.findall('loadingArea'))
            options = x.find('options')
            for opt in mho.options_list():
                if opt in options.attrib:
                    if options.attrib[opt]:
                        setattr(mho, opt, True)

            out.write(mho.tableRow())
