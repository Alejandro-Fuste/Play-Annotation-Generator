# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_15`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 27 |
| Action Segments inferred | 112 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 32: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [38–54], lower_priority='Action_ZoneBlock' annotated_start=40, effective_Action_ZoneBlock_start=55.
> - Action 'Action_None' range [38-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [40-102] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-176] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-185] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-155] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-170] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-184] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-57] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-71] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-100] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-165] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-187] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [71-196] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [198-205] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [207-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-59] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-99] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-171] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-183] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-57] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-87] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-190] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-177] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-201] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-177] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-190] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-56] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-99] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-107] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-59] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-95] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-57] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-70] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-56] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-70] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-99] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [103-188] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-57] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-100] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-53] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-57] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-99] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-100] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-99] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-162] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-164] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-177] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-184] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-208] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '29' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.