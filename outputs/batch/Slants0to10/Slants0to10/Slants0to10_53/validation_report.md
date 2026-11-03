# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_53`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 54: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Segment 'Action_PassBlock' for track '17' has invalid range: start=7, end=2. Clamping end to start.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [3–18], lower_priority='Action_PassBlock' annotated_start=7, effective_Action_PassBlock_start=19.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [3–18], lower_priority='Action_SnapReceive' annotated_start=3, effective_Action_SnapReceive_start=19.
> - Action 'Action_None' range [3-387] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [114-119] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-113] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-92] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-214] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [3-408] for track '4' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [3-292] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-393] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-277] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-349] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-356] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-361] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-321] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-280] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-319] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-122] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [3-290] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-419] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-111] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-173] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-113] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-202] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-25] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-30] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-67] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [69-72] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [3-17] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-31] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-34] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-290] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-323] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-337] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-8] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-35] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-57] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-104] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-14] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-38] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-55] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-78] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-89] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [100-213] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-43] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-136] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-280] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-305] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-321] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-333] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-331] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-404] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-173] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-419] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-169] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-251] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-319] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-387] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-396] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-352] for track '36' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.