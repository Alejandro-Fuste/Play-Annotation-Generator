# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_7`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_7/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 16: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 98 frames exceeds threshold 90 frames [start=127, end=224].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (LG) duration 98 frames exceeds threshold 90 frames [start=127, end=224].
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (RT) duration 98 frames exceeds threshold 90 frames [start=127, end=224].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 98 frames exceeds threshold 90 frames [start=127, end=224].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [124–141], lower_priority='Action_ZoneBlock' annotated_start=127, effective_Action_ZoneBlock_start=142.
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 98 frames exceeds threshold 90 frames [start=127, end=224].
> - Action 'Action_None' range [124-155] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-170] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-197] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-177] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [180-207] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-146] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-220] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [172-281] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [285-294] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [299-307] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [309-311] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [128-170] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-316] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-158] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [171-224] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-329] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-298] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-197] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '26' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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