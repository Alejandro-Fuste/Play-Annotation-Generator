# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_210`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_210/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 419: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 420: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - Row 420: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 420: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [98–118], lower_priority='Action_ZoneBlock' annotated_start=101, effective_Action_ZoneBlock_start=119.
> - Action 'Action_None' range [98-128] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-128] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [119-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-203] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [119-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-208] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-249] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-221] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-228] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-236] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-177] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-204] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-131] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-150] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-173] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '25' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.