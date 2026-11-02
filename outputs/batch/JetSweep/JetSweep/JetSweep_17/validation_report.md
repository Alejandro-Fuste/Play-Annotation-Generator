# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_17`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 29 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [37–51], lower_priority='Action_ZoneBlock' annotated_start=40, effective_Action_ZoneBlock_start=52.
> - Action 'Action_None' range [37-102] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [65-165] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [167-188] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [190-193] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [195-197] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-176] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [37-173] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-116] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-162] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-74] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [40-78] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-203] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-210] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [69-106] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-71] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [75-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-53] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-198] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-162] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-165] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '29' has 1 frames without a visible bounding box.
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