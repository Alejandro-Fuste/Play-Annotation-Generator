# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_193`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_193/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 388: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [23–32], lower_priority='Action_ZoneBlock' annotated_start=24, effective_Action_ZoneBlock_start=33.
> - Action 'Action_None' range [23-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-68] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-77] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [41-168] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [170-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-94] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-158] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-48] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-53] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-173] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-173] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-37] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-89] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [90-180] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-100] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-159] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-113] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-147] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-166] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '26' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.