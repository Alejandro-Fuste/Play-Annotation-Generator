# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_313`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_313/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 31 |
| Ball Tracks | 1 |
| CSV events parsed | 22 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '24' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '16' (C) duration 92 frames exceeds threshold 90 frames [start=30, end=121].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [27–42], lower_priority='Action_DownBlock' annotated_start=30, effective_Action_DownBlock_start=43.
> - Validation warning: Action 'Action_PullBlock' for track '19' (RG) duration 92 frames exceeds threshold 90 frames [start=30, end=121].
> - Validation warning: Action 'Action_DownBlock' for track '21' (LT) duration 92 frames exceeds threshold 90 frames [start=30, end=121].
> - Action 'Action_None' range [27-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-80] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-75] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-84] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-88] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-122] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-180] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [73-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-160] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-146] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-78] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-129] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [27-58] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-57] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-170] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [30-121] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [122-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [43-121] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [30-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-52] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-98] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [30-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-180] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [30-94] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [160-168] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-84] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-156] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-114] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-136] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-180] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [163-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-178] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '31' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.