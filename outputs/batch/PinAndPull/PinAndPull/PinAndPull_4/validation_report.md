# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PinAndPull_4`
- **Input XML**: `outputs/batch/PinAndPull/PinAndPull/PinAndPull_4/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PinAndPull.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 328 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '19' (Unknown) duration 99 frames exceeds threshold 90 frames [start=81, end=179].
> - Action 'Action_None' range [78-123] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-124] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-133] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-147] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-118] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-135] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [140-153] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-263] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-269] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [112-138] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [142-157] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [160-165] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [169-328] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-223] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [98-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-154] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-86] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-105] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-200] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-140] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-156] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-173] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-221] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-112] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-205] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-220] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-104] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-92] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-183] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [78-84] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-113] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' for track '17' starts at frame 81, but the player has no visible bounding box on this frame.
> - Action 'Action_PullLeadBlock' range [81-83] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [87-97] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [125-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-110] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-253] for track '18' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-74] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [81-94] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [114-122] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [132-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [147-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-231] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [83-111] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [127-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-152] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-207] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-164] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-285] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-192] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-205] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-284] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-207] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-248] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-227] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [216-221] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-229] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-279] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-324] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.