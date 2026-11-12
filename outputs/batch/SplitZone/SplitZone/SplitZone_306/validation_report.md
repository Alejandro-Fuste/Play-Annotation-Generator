# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_306`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_306/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 47 |
| Player Tracks | 47 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 113 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 146 frames exceeds threshold 90 frames [start=81, end=226].
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (RG) duration 146 frames exceeds threshold 90 frames [start=81, end=226].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (RT) duration 146 frames exceeds threshold 90 frames [start=81, end=226].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (C) duration 146 frames exceeds threshold 90 frames [start=81, end=226].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 146 frames exceeds threshold 90 frames [start=81, end=226].
> - Action 'Action_None' range [172-278] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-307] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [172-183] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-232] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-257] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-332] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-374] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-389] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-358] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-389] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-227] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-236] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-261] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-239] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-218] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-312] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-204] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-298] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [218-378] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-196] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-331] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-12] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-16] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-35] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-35] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-72] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-56] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-105] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-127] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-219] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-229] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-72] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-96] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-214] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-258] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-267] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-301] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-338] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-318] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-285] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-308] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-293] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-320] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-330] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-342] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-351] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-363] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-339] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-353] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-370] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-342] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-351] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [353-354] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-370] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-383] for track '46' has 1 frames without a visible bounding box.
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
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.