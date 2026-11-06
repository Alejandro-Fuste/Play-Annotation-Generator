# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_100`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_100/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallSnap' for track '14' has invalid range: start=25, end=21. Clamping end to start.
> - Action 'Action_ZoneBlock' range [14-84] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-111] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-121] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-78] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-180] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [14-32] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-42] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-49] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-94] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [43-47] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-132] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-46] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-62] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-68] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-133] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-36] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-169] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-26] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-40] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-28] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [58-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [147-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [172-174] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-76] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-80] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-17] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-80] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-44] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-148] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-30] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-157] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-53] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-144] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-86] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-114] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-147] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-92] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-111] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-180] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-142] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-155] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [157-163] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-147] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-157] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-180] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-170] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '32' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.