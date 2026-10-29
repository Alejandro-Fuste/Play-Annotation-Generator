# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_76`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_76/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 28 |
| Ball Tracks | 2 |
| CSV events parsed | 16 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 358 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
> - Action 'Action_PreSnap' range [0-136] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-337] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-325] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-331] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [275-308] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-314] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-274] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-357] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-307] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-310] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-317] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-333] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-351] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-308] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-314] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-220] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-298] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-306] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-264] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-268] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-330] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-347] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-358] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-219] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-235] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-358] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-215] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-226] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-268] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [275-283] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [286-304] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-333] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-27] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [275-307] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-328] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-343] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-355] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-56] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-86] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-92] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-188] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-242] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-215] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-306] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-312] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-315] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-316] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-333] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-350] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-312] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-318] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-355] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-358] for track '29' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.