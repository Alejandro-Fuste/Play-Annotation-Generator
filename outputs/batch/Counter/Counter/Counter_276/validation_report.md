# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_276`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_276/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 113 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 554: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '8' (RG) duration 107 frames exceeds threshold 90 frames [start=64, end=170].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [61–77], lower_priority='Action_PullLeadBlock' annotated_start=64, effective_Action_PullLeadBlock_start=78.
> - Action 'Action_None' range [61-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-125] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-121] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-212] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-73] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-135] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-191] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-215] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-254] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-48] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-67] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-245] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-97] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-175] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-250] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-130] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [193-202] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [212-241] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [64-94] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [102-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [64-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [91-137] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-148] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-159] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [64-123] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-101] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-119] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-94] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [78-109] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [113-164] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-43] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-46] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-171] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-152] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-181] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-213] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-262] for track '20' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-183] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-199] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-188] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-246] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-213] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-230] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-236] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-246] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-247] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-269] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.