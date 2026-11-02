# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_162`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_162/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [77–92], lower_priority='Action_ZoneBlock' annotated_start=79, effective_Action_ZoneBlock_start=93.
> - Action 'Action_None' range [77-135] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-143] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-154] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-154] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-154] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-154] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-155] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-154] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-154] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-160] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [79-92] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [94-143] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-158] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-154] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-173] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-144] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [156-232] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [234-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [242-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-92] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-171] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-162] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-243] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-160] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-193] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-175] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-217] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-229] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-216] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-269] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '38' has 1 frames without a visible bounding box.
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
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.