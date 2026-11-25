# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_210`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_210/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 422: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [50–60], lower_priority='Action_ZoneBlock' annotated_start=51, effective_Action_ZoneBlock_start=61.
> - Action 'Action_None' range [50-126] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-74] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-151] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-106] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-144] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [51-86] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-82] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-104] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-160] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-158] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-193] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-183] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-213] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-237] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-57] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-139] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-68] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-83] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-359] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-338] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [73-108] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-122] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-139] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-293] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-331] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-304] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-354] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-146] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-142] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-158] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-165] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-331] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-135] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-168] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-203] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [205-218] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-224] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-238] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-228] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-238] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-276] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-282] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-347] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-255] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-295] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-286] for track '38' has 2 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.