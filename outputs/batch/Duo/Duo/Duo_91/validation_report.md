# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_91`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_91/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 142 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 448 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 448 as fallback play end.
> - Action 'Action_PreSnap' range [0-41] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-61] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-448] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-259] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [330-370] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-379] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-390] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-401] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-69] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-93] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-106] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-388] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-249] for track '5' has 5 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [263-303] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-369] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-378] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-381] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-53] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-70] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-53] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-58] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-78] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-163] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-173] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-312] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-417] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-88] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-116] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [330-379] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-49] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-53] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-51] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-331] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-426] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [434-435] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-107] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-177] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-296] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-425] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-66] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-93] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-106] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-363] for track '18' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-89] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-105] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-309] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-448] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-37] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-394] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-227] for track '23' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-232] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-240] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-243] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-247] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-303] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-362] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-409] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-212] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-227] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-240] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-247] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-306] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-390] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [422-425] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [430-439] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [441-442] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-351] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-348] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-368] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-371] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-375] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [406-407] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [397-414] for track '29' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [421-427] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [430-431] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-402] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [416-417] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [426-428] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [437-440] for track '32' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.