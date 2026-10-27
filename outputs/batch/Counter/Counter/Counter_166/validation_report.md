# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_166`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_166/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 28 |
| Ball Tracks | 1 |
| CSV events parsed | 18 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_DownBlock' for track '8' has invalid range: start=97, end=95. Clamping end to start.
> - Validation warning: Action 'Action_PullBlock' for track '10' (C) duration 96 frames exceeds threshold 90 frames [start=97, end=192].
> - Validation warning: Action 'Action_DownBlock' for track '12' (QB) duration 96 frames exceeds threshold 90 frames [start=97, end=192].
> - Action 'Action_None' range [96-127] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-135] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-144] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-153] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-244] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-135] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-139] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-160] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [136-216] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [218-234] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [96-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-132] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [97-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [146-151] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [154-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '10' starts at frame 193, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [193-193] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-29] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-115] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-216] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [97-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [135-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [163-164] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [167-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [171-174] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-38] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-108] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [128-162] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [147-187] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-252] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-289] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [161-218] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-244] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-260] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-274] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-279] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-285] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-299] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-233] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-273] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-282] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-268] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-285] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-277] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.