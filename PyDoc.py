import requests as req
import json


url = 'http://URL:PORT/'
logonInfo = {'password': 'Password', 
             'clientType': '', 
             'auth': 'secEnterprise', 
             'userName': 'User'
            }
biprwsLogon = 'biprws/logon/long/'
documentLocation = 'biprws/raylight/v1/documents/16057/'
a = {
            'Accept':'application/json',
            'Content-Type':'application/json'
         }

d = str.encode(json.dumps(logonInfo))

r = req.get(url+'biprws/logon/long', headers = a)
l = req.post(url+'biprws/logon/long',d, headers = a)
responseData = l.json()
#print(r.json())


logonToken = responseData['logonToken']

headers = {
            'X-SAP-LogonToken'  : '"'+logonToken+'"',
           'Accept':'application/json',
           'Content-Type':'application/json',
           #'Accept-Language'   : 'locale',
           #'X-SAP-PVL'         : 'contentLocale'
          }
# 
#openDoc = req.get('http://URL:PORT/biprws/raylight/v1/documents/16057',headers = headers)
#print(openDoc.json())

#see list of prompt
#refreshDoc = req.get(url + documentLocation + 'parameters?refresh=true' , headers = headers)
#print(json.dumps(refreshDoc.json(),indent = 2))

prompt = {
  "parameters": {
    "parameter": [
      {
        "@optional": "false",
        "@type": "sapVariable",
        "@dpId": "DP0",
        "@primary": "true",
        "id": 0,
        "technicalName": "YUPM0001",
        "name": "Fiscal Year/Period",
        "answer": {
          "@constrained": "false",
          "@type": "Text",
          "@keyType": "Text",
          "info": {
            "@cardinality": "Single",
            "@keepLastValues": "true",
            "lov": {
              "@hierarchical": "true",
              "@nodeSelection": "Any",
              "@partial": "false",
              "@refreshable": "true",
              "@searchable": "true",
              "@mandatorySearch": "false",
              "@searchScopes": "Values,Keys",
              "@searchTargets": "Database",
              "id": "UNIVERSELOV_DS0.:M:STR:YUPM0001",
              "updated": "2019-04-14T01:08:26.000Z",
              "values": {
                "value": [
                  {
                    "@id": "2019002",
                    "$": "February 2019"
                  }
                ]
              },
              "columns": {
                "@mappingId": 0,
                "column": [
                  {
                    "@id": 0,
                    "@type": "String",
                    "$": "YUPM0001"
                  }
                ]
              }
            },
            "previous": {
              "value": [
                {
                  "@id": "2019002",
                  "$": "February 2019"
                }
              ]
            }
          },
          "values": {
            "value": [
              {
                "@id": "2019002",
                    "$": "February 2019"
              }
            ]
          }
        }
      },
      {
        "@optional": "true",
        "@type": "sapVariable",
        "@dpId": "DP0",
        "@primary": "true",
        "id": 1,
        "technicalName": "YUPO0001",
        "name": "Company Code",
        "answer": {
          "@constrained": "true",
          "@type": "Text",
          "@keyType": "Text",
          "info": {
            "@cardinality": "Single",
            "@keepLastValues": "true",
            "lov": {
              "@hierarchical": "true",
              "@nodeSelection": "Any",
              "@partial": "false",
              "@refreshable": "true",
              "@searchable": "true",
              "@mandatorySearch": "false",
              "@searchScopes": "Values,Keys",
              "@searchTargets": "Database",
              "id": "UNIVERSELOV_DS0.:M:STR:YUPO0001",
              "updated": "2019-04-14T01:08:26.000Z",
              "values": {
                "value": [
                  {
                    "@id": "0HIER_NODE/YMMI",
                    "@final": "false",
                    "$": "MMI Consolidation"
                  }
                ]
              },
              "columns": {
                "@mappingId": 0,
                "column": [
                  {
                    "@id": 0,
                    "@type": "String",
                    "$": "YUPO0001"
                  }
                ]
              }
            }
          }
        }
      }
    ]
  }
}



refreshData = req.put(url + documentLocation + 'parameters?refresh=true' , data = json.dumps(prompt), headers = headers)
#refresh.status_code

refreshDocument = req.put(url + documentLocation,headers = headers)
#refreshDocument.status_code

headers = {
            'X-SAP-LogonToken'  : '"'+logonToken+'"',
           'Accept':'application/json',
           'Content-Type':'application/json',
          }

logOff = req.get(url + 'logoff', headers = headers)

logOff.status_code
