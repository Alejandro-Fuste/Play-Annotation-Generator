# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_120`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_120/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 242: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [1–10], lower_priority='Action_ZoneBlock' annotated_start=4, effective_Action_ZoneBlock_start=11.
> - Action 'Action_None' range [1-73] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-91] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-87] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-133] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-166] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-192] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-205] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-77] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-127] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-135] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-195] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-103] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [20-77] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-36] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-97] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-171] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [47-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [116-164] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-191] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-205] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-104] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-21] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-77] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [84-210] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-15] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-81] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-122] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-126] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-156] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-33] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-110] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-127] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-197] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [78-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-187] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-197] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-185] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-195] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-185] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-183] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-196] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '35' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.