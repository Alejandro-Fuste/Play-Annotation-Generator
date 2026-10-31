# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_6`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 12: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - Track ID '23' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [20–40], lower_priority='Action_PassBlock' annotated_start=27, effective_Action_PassBlock_start=41.
> - Action 'Action_None' range [20-104] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [120-209] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [211-212] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-104] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-21] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-34] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [38-40] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-51] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-74] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-144] for track '7' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [20-239] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-228] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-237] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-47] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-220] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-104] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [106-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [170-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-27] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [20-25] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-61] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-128] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-90] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 20, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [20-33] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [104-163] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-104] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-113] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-27] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-60] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [64-104] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-36] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-63] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-76] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-104] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-104] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-104] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-160] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-213] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-239] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-208] for track '36' has 2 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.