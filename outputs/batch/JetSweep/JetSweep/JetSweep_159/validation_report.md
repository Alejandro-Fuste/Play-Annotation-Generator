# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_159`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_159/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [63–75], lower_priority='Action_ZoneBlock' annotated_start=65, effective_Action_ZoneBlock_start=76.
> - Action 'Action_None' range [63-225] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [227-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-213] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-105] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-212] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [218-220] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-212] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-222] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-206] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [63-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-113] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-231] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [233-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [65-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-184] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [31-39] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [42-52] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [54-58] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [92-132] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [136-215] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-75] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-213] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-127] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-214] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-177] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-216] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-233] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.