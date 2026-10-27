# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_305`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_305/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 110 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '17' (C) duration 96 frames exceeds threshold 90 frames [start=44, end=139].
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [41–55], lower_priority='Action_DownBlock' annotated_start=44, effective_Action_DownBlock_start=56.
> - Validation warning: Action 'Action_PullBlock' for track '18' (LG) duration 96 frames exceeds threshold 90 frames [start=44, end=139].
> - Validation warning: Action 'Action_DownBlock' for track '20' (RG) duration 96 frames exceeds threshold 90 frames [start=44, end=139].
> - Action 'Action_None' range [41-209] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-243] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-251] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-246] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-241] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-193] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [41-243] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-248] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [90-230] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-235] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-266] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [41-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-135] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-244] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-273] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-135] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-166] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [41-51] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [56-57] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [60-64] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [73-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [106-107] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [113-139] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-252] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [44-139] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [140-152] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-173] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-126] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [128-184] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [44-50] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [88-96] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [98-133] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [135-139] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '20' starts at frame 140, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [140-144] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-193] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-12] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-21] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-32] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [44-45] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [49-112] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [118-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-215] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [217-224] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-164] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-177] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-116] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-130] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-227] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-122] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-181] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-185] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-299] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.