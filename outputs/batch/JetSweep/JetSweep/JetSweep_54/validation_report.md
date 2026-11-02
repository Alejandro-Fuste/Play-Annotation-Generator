# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_54`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_54/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 110: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [70–79], lower_priority='Action_ZoneBlock' annotated_start=72, effective_Action_ZoneBlock_start=80.
> - Action 'Action_None' range [70-196] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-211] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-137] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [97-199] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-231] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-202] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-207] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-197] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-164] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [70-97] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-159] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-202] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-79] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-192] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-216] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-223] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [70-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-105] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-121] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-127] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-98] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-222] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-186] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-202] for track '26' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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