# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_326`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_326/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '0' (TE) duration 119 frames exceeds threshold 90 frames [start=51, end=169].
> - Validation warning: Action 'Action_PullBlock' for track '1' (LG) duration 119 frames exceeds threshold 90 frames [start=51, end=169].
> - Validation warning: Action 'Action_DownBlock' for track '6' (C) duration 119 frames exceeds threshold 90 frames [start=51, end=169].
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [48–63], lower_priority='Action_DownBlock' annotated_start=51, effective_Action_DownBlock_start=64.
> - Validation warning: Action 'Action_DownBlock' for track '9' (RG) duration 119 frames exceeds threshold 90 frames [start=51, end=169].
> - Action 'Action_DownBlock' range [51-127] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [132-137] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-247] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-373] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [64-169] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-301] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-96] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-95] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-294] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-73] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-86] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-419] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [48-203] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-418] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-27] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-69] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-88] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-34] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-65] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [68-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-95] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-108] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [105-111] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-116] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-290] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-311] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-153] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-163] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-244] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-248] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-419] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-194] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-393] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-262] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-247] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-273] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-370] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-370] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-396] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-413] for track '37' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.