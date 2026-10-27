# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Dagger_46`
- **Input XML**: `outputs/batch/Dagger/Dagger/Dagger_46/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Dagger.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 328 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 46: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 46: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [191–196], lower_priority='Action_PassBlock' annotated_start=194, effective_Action_PassBlock_start=197.
> - Action 'Action_None' range [191-296] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-300] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-197] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-278] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [191-273] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-328] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-301] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BreakInside' range [204-235] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-310] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-328] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-30] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-66] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-139] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-201] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-220] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [197-200] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-37] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-47] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-51] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ClearToEdge' range [218-241] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-289] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-301] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-305] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-308] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-304] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-328] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-324] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-328] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-324] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-328] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-328] for track '19' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.