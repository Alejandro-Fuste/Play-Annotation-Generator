# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_3`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 8: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [79–92], lower_priority='Action_ZoneBlock' annotated_start=81, effective_Action_ZoneBlock_start=93.
> - Action 'Action_None' range [79-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-226] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-115] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [122-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [129-130] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-151] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [158-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [119-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [138-185] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [191-207] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-215] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '23' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.