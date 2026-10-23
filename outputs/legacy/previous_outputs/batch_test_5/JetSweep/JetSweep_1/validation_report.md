# TapeVision Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_1`
- **Input XML**: `outputs/batch_test_5/JetSweep/JetSweep_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 29 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [132–144], lower_priority='Action_ZoneBlock' annotated_start=133, effective_Action_ZoneBlock_start=145.
> - Action 'Action_None' range [193-309] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-285] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-315] for track '23' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.