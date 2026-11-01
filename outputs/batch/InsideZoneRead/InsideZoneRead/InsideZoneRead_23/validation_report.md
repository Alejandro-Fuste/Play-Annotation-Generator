# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_23`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_23/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 48: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_BallCarry' for track '18' has invalid range: start=130, end=120. Clamping end to start.
> - Segment 'Action_BlockSecondLevel' for track '20' has invalid range: start=120, end=114. Clamping end to start.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [92–102], lower_priority='Action_ZoneBlock' annotated_start=94, effective_Action_ZoneBlock_start=103.
> - Action 'Action_None' range [92-222] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-151] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-216] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-243] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-223] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-240] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-225] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-240] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-114] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-234] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-250] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-265] for track '27' has 1 frames without a visible bounding box.
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