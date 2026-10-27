# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_196`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_196/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '1' (OLB1) duration 93 frames exceeds threshold 90 frames [start=97, end=189].
> - Validation warning: Action 'Action_DownBlock' for track '5' (WR2) duration 93 frames exceeds threshold 90 frames [start=97, end=189].
> - Validation warning: Action 'Action_DownBlock' for track '6' (DE1) duration 93 frames exceeds threshold 90 frames [start=97, end=189].
> - Validation warning: Action 'Action_DownBlock' for track '9' (CB1) duration 93 frames exceeds threshold 90 frames [start=97, end=189].
> - Action 'Action_None' range [94-162] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [97-143] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-221] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-143] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-177] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-219] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-248] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-215] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-186] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [97-189] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-258] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-254] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-211] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [97-145] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-242] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [137-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-151] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-139] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-254] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-242] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-166] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-187] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-219] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-229] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-261] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-236] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-269] for track '26' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.