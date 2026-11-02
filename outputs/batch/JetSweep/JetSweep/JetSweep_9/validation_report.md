# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_9`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_9/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 29 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [24–33], lower_priority='Action_ZoneBlock' annotated_start=25, effective_Action_ZoneBlock_start=34.
> - Action 'Action_None' range [24-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-170] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-170] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-115] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-129] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-166] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-74] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-95] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [44-163] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [166-169] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [172-180] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-146] for track '16' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [156-168] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-171] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [75-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-84] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-113] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-173] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-157] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-48] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-90] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-114] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-134] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-167] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-180] for track '27' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.