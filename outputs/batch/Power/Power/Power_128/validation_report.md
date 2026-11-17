# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_128`
- **Input XML**: `outputs/batch/Power/Power/Power_128/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 258: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 258: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [21-216] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-212] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-216] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-197] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [131-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [142-181] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-119] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-133] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-144] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-230] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-249] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-298] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-177] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-172] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-213] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-249] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-256] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-33] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-195] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-267] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-299] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-251] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-136] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-224] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-208] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-194] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-198] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-229] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-246] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-277] for track '24' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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