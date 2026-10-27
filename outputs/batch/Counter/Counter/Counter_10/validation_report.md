# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_10`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_10/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 22: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Overlapping action conflict at frame 66 for track '3': 'Action_PullBlock' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
> - Validation warning: Action 'Action_DownBlock' for track '5' (LT) duration 93 frames exceeds threshold 90 frames [start=66, end=158].
> - Action 'Action_None' range [61-105] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-187] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [116-291] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [294-329] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-107] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-123] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-184] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-189] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-172] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-247] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-293] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-91] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [61-78] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-108] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-86] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-159] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [135-139] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-141] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-183] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-203] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-310] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-329] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-181] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-196] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-230] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-244] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-242] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-314] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-317] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-318] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-329] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-310] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-316] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-320] for track '36' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.