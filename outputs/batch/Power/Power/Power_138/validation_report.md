# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_138`
- **Input XML**: `outputs/batch/Power/Power/Power_138/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 42 |
| Ball Tracks | 2 |
| CSV events parsed | 11 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Deduplicated duplicate event 'Action_DownBlock' at frame 172 for track '18'.
> - Action 'Action_PreSnap' range [4-284] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-459] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [464-469] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [472-473] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [475-476] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-68] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-309] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-29] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-74] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-330] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-344] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-446] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-358] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-298] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-373] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-329] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-353] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-402] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [422-424] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [432-435] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-429] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-80] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-123] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-286] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-422] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [424-439] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-25] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-31] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-355] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [359-388] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [392-405] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-410] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [418-434] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [439-442] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [449-467] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-6] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-25] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-103] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-103] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-171] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-427] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-138] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-273] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-464] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-285] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-321] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-344] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-347] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-351] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-357] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-387] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [390-479] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-364] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-385] for track '24' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-305] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-479] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-309] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-340] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-349] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-331] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [333-479] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-386] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [397-414] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-461] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [359-387] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-401] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [408-479] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [366-385] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-400] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [403-411] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [419-436] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-378] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-410] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [401-427] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [429-446] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [450-464] for track '36' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [420-446] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [425-433] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [457-462] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-479] for track '43' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.