# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_33`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 68: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 98 frames exceeds threshold 90 frames [start=29, end=126].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (C) duration 110 frames exceeds threshold 90 frames [start=29, end=138].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [27–41], lower_priority='Action_ZoneBlock' annotated_start=29, effective_Action_ZoneBlock_start=42.
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (RG) duration 110 frames exceeds threshold 90 frames [start=29, end=138].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 107 frames exceeds threshold 90 frames [start=29, end=135].
> - Action 'Action_None' range [27-56] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-81] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-131] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-95] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-62] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-95] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-123] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-53] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-99] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-141] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-107] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-122] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-126] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [69-137] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [141-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [158-209] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-47] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-62] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-82] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-188] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-206] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-188] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-202] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-123] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-103] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-117] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-135] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-173] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-177] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-193] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-162] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-190] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.