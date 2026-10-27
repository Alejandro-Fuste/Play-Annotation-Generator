# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_29`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_29/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '11' (RG) duration 94 frames exceeds threshold 90 frames [start=60, end=153].
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [56–60], lower_priority='Action_DownBlock' annotated_start=60, effective_Action_DownBlock_start=61.
> - Validation warning: Action 'Action_DownBlock' for track '15' (RT) duration 97 frames exceeds threshold 90 frames [start=60, end=156].
> - Action 'Action_None' range [56-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-204] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-113] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-138] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-145] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-168] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-134] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-197] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-204] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [68-103] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [104-131] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-70] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' for track '11' starts at frame 60, but the player has no visible bounding box on this frame.
> - Action 'Action_PullBlock' range [60-60] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [79-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [83-94] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [126-153] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-67] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-74] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [61-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [60-151] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [60-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [68-108] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [136-156] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-181] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-201] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-103] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [92-99] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-210] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-26] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-44] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-55] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-60] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-124] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-62] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-75] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-101] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-108] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-143] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-129] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-206] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-146] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-204] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-167] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-181] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.