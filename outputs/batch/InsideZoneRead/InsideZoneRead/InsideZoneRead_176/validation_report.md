# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_176`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_176/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 352: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [30–47], lower_priority='Action_ZoneBlock' annotated_start=33, effective_Action_ZoneBlock_start=48.
> - Action 'Action_None' range [30-217] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-227] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-111] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-157] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-196] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-228] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [231-268] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-250] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-167] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-224] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-8] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-148] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-247] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-252] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [251-256] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-269] for track '27' has 2 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.