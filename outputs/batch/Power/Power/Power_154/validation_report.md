# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_154`
- **Input XML**: `outputs/batch/Power/Power/Power_154/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 310: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '5' (LT) duration 93 frames exceeds threshold 90 frames [start=181, end=273].
> - Validation warning: Action 'Action_DownBlock' for track '7' (LG) duration 93 frames exceeds threshold 90 frames [start=181, end=273].
> - Validation warning: Action 'Action_DownBlock' for track '8' (RG) duration 93 frames exceeds threshold 90 frames [start=181, end=273].
> - Action 'Action_PreSnap' range [32-341] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-369] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-266] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-257] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-330] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-381] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-155] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-160] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-287] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-352] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-389] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-293] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-321] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-181] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [181-204] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-307] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [181-269] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [343-375] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-38] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-269] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-278] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-411] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [413-419] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [421-449] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-267] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-282] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-429] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [431-439] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [447-449] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-355] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-359] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-368] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-371] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-361] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-213] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-223] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-253] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-359] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-96] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-187] for track '14' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-220] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-43] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-222] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-243] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-264] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-249] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-264] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-285] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-315] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-336] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-300] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-331] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [333-342] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-278] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-286] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-280] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-292] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-339] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-353] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-297] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-316] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-343] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-353] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-366] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-373] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-294] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-302] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-308] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-379] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-449] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-401] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-345] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-341] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-318] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-359] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-375] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-339] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-368] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-442] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-346] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-419] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [362-363] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [362-363] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-366] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-378] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [442-444] for track '37' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.