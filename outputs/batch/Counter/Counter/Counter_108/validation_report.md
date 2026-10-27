# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_108`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_108/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 218: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 218: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '0' (RT) duration 125 frames exceeds threshold 90 frames [start=117, end=241].
> - Validation warning: Action 'Action_PullBlock' for track '2' (LG) duration 125 frames exceeds threshold 90 frames [start=117, end=241].
> - Validation warning: Action 'Action_DownBlock' for track '8' (RG) duration 125 frames exceeds threshold 90 frames [start=117, end=241].
> - Segment 'Action_BallSnap' for track '15' has invalid range: start=111, end=19. Clamping end to start.
> - Segment 'Action_DownBlock' for track '15' has invalid range: start=117, end=19. Clamping end to start.
> - Action 'Action_None' range [242-318] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-164] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-194] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [117-139] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [143-180] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [182-183] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-325] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-186] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [117-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [162-163] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-328] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-184] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-143] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [117-190] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-324] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-193] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-157] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [151-195] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [230-255] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [258-326] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-216] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-137] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-203] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-133] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-148] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-177] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-186] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-327] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-184] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-191] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-324] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-222] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-212] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-314] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-261] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-266] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-298] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-317] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-291] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-291] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-308] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-314] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-280] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-329] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-303] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-318] for track '31' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.