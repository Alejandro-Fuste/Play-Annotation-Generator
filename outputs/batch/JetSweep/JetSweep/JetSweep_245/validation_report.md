# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_245`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_245/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 94 frames exceeds threshold 90 frames [start=25, end=118].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (LG) duration 94 frames exceeds threshold 90 frames [start=25, end=118].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 94 frames exceeds threshold 90 frames [start=25, end=118].
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [23–35], lower_priority='Action_ZoneBlock' annotated_start=25, effective_Action_ZoneBlock_start=36.
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 94 frames exceeds threshold 90 frames [start=25, end=118].
> - Action 'Action_None' range [23-218] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-226] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-72] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-166] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-77] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-226] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [228-238] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-200] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [45-205] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [207-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-96] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-108] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-226] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-235] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-75] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-156] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-194] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-214] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [25-99] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-177] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-50] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-40] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-147] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-79] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-86] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-239] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-163] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-183] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '42' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.