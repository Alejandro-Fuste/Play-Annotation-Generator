# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_163`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_163/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 110 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 539 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (C) duration 224 frames exceeds threshold 90 frames [start=316, end=539].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (LT) duration 224 frames exceeds threshold 90 frames [start=316, end=539].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 224 frames exceeds threshold 90 frames [start=316, end=539].
> - Action 'Action_None' range [313-511] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [322-362] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-399] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-488] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [492-498] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-508] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [511-527] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [534-537] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [316-394] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-28] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-341] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-367] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-378] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-412] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [419-420] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [316-344] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [347-349] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-344] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [338-482] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [488-520] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-370] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-354] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-337] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-349] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-361] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-412] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [420-539] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-34] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-41] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-63] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-68] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-26] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-29] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-312] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [313-480] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-513] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [520-526] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [534-535] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [316-346] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [373-374] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [378-381] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-238] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-244] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-258] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-271] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-275] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-361] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-367] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-378] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-488] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [490-496] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [499-505] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [508-510] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [520-523] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [525-531] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-375] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-384] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-370] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-388] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-505] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-454] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-449] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [465-467] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [459-475] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [481-486] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-501] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [528-529] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [533-537] for track '34' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.