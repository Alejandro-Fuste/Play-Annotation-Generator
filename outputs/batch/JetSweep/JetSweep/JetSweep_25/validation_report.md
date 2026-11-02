# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_25`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_25/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 29 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [44–55], lower_priority='Action_ZoneBlock' annotated_start=53, effective_Action_ZoneBlock_start=56.
> - Action 'Action_None' range [44-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [70-177] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [179-208] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-72] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-165] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-197] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [44-105] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [44-108] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-78] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-130] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-66] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-84] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-67] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-71] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-140] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-167] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-197] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-203] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.