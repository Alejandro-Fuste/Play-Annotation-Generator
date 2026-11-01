# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_153`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_153/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '0' (LT) duration 94 frames exceeds threshold 90 frames [start=102, end=195].
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 94 frames exceeds threshold 90 frames [start=102, end=195].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 94 frames exceeds threshold 90 frames [start=102, end=195].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [99–111], lower_priority='Action_ZoneBlock' annotated_start=102, effective_Action_ZoneBlock_start=112.
> - Action 'Action_ZoneBlock' range [102-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [113-177] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-163] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-194] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [141-207] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [102-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [102-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-158] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-237] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-212] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-125] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-205] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-119] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-182] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-239] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [176-184] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-239] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [180-185] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-216] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-224] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '22' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.