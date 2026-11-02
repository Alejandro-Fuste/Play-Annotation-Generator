# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_138`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_138/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 278: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [109–122], lower_priority='Action_ZoneBlock' annotated_start=110, effective_Action_ZoneBlock_start=123.
> - Action 'Action_None' range [109-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-165] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-185] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-234] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-163] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [110-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-185] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [110-161] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [171-175] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-181] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [110-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-194] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-160] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-170] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-164] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-41] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-50] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-94] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [109-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-145] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-151] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-269] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-176] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '18' has 1 frames without a visible bounding box.
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
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.