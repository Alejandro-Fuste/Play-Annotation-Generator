# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_225`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_225/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 452: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_LeadBlock' for track '1' (TE) duration 95 frames exceeds threshold 90 frames [start=81, end=175].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (LT) duration 95 frames exceeds threshold 90 frames [start=81, end=175].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (LG) duration 95 frames exceeds threshold 90 frames [start=81, end=175].
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (RT) duration 95 frames exceeds threshold 90 frames [start=81, end=175].
> - Action 'Action_BallCarry' range [110-213] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-138] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-226] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-225] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-114] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [122-124] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-127] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-128] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-122] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-211] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-231] for track '26' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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