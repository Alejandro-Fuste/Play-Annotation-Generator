# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_145`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_145/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 292: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-85] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-118] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-161] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-240] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-245] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-137] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-256] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-143] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-73] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-269] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-115] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-193] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '26' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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