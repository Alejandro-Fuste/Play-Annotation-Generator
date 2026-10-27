# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_277`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_277/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 119 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 556: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 556: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - Row 556: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '4' (LT) duration 95 frames exceeds threshold 90 frames [start=20, end=114].
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [17–31], lower_priority='Action_PullLeadBlock' annotated_start=20, effective_Action_PullLeadBlock_start=32.
> - Validation warning: Action 'Action_DownBlock' for track '14' (LG) duration 95 frames exceeds threshold 90 frames [start=20, end=114].
> - Segment 'Action_BallCarry' for track '20' has invalid range: start=68, end=37. Clamping end to start.
> - Action 'Action_None' range [17-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-141] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [144-180] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [17-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [20-95] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-118] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-108] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-141] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-166] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-177] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-91] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-120] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-137] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-54] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-61] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-42] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-76] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-173] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [17-28] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [30-31] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [44-71] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [73-95] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [97-106] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [109-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-150] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [164-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-73] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [20-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [101-110] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [112-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-145] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-157] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-172] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-48] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-77] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-116] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-147] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-157] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-79] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-94] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-150] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [20-93] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [104-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-105] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-46] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-53] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-113] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-78] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-94] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [99-102] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-126] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-180] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-180] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-180] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '31' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '34' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.