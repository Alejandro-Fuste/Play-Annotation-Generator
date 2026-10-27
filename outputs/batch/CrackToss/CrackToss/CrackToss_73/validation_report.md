# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_73`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_73/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 249 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 161 targets track ID '212', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 148: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - Row 148: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 249 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '5' (LT) duration 147 frames exceeds threshold 90 frames [start=103, end=249].
> - Segment 'Action_BallSnap' for track '18' has invalid range: start=100, end=31. Clamping end to start.
> - Action 'Action_None' range [100-241] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [100-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-183] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-235] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-245] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-249] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [134-204] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [207-208] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-121] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-140] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-152] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-158] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-225] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-213] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-232] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [100-158] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-218] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-236] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-203] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-232] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-108] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-187] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-222] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [108-133] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-249] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-112] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-24] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-99] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-73] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-80] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-139] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-220] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [103-126] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [130-154] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-209] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-168] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-195] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-211] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-139] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-236] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-249] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-237] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '31' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.