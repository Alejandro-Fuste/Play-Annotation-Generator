# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_115`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_115/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 232: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [3–18], lower_priority='Action_ZoneBlock' annotated_start=6, effective_Action_ZoneBlock_start=19.
> - Action 'Action_None' range [3-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-150] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [3-62] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-36] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-131] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-51] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [19-27] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-33] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-40] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [42-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [145-150] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-48] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-66] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-75] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-82] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-150] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [90-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '27' has 1 frames without a visible bounding box.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.