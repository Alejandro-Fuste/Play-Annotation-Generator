# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_65`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_65/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 46, Column 'Secure Catch': Single text entry 'OOB' could not be parsed as a frame number.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 110: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [91–104], lower_priority='Action_RunBlock' annotated_start=97, effective_Action_RunBlock_start=105.
> - Action 'Action_None' range [91-278] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-292] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-221] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-153] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-158] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-158] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-187] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-186] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-240] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-160] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-174] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-193] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-202] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [97-136] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [142-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [158-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [97-134] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [136-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [150-299] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [97-215] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [97-299] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-193] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-273] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-299] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-290] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-270] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-289] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-271] for track '31' has 2 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.