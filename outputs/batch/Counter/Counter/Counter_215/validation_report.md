# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_215`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_215/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 432: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [59–72], lower_priority='Action_DownBlock' annotated_start=62, effective_Action_DownBlock_start=73.
> - Action 'Action_None' range [59-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-136] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-144] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-239] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-112] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-115] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [62-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [105-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [130-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [137-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-106] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-148] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [159-167] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-112] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-213] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-152] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-216] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-102] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-151] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [62-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [62-73] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [62-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [115-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [120-122] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [124-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [140-141] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-191] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-230] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-173] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-229] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-238] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [141-173] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-219] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-170] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-236] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-239] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '32' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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