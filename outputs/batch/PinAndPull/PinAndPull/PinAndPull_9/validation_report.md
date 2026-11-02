# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PinAndPull_9`
- **Input XML**: `outputs/batch/PinAndPull/PinAndPull/PinAndPull_9/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PinAndPull.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 358 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 20: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Track ID '26' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '19' (Unknown) duration 97 frames exceeds threshold 90 frames [start=203, end=299].
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [201–211], lower_priority='Action_PullLeadBlock' annotated_start=203, effective_Action_PullLeadBlock_start=212.
> - Action 'Action_None' range [201-325] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-330] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-249] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-278] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-299] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-323] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-312] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-323] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-310] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [234-352] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-264] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-283] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-324] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-221] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-288] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-340] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-259] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-352] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-255] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-314] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-286] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-308] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-349] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-291] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-354] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-297] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-326] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-348] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [212-265] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [277-278] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-307] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-324] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-358] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-323] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-358] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-312] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-325] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-339] for track '24' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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