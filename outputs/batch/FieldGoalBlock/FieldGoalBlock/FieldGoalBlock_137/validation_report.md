# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_137`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_137/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 121 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BlockKick' for track '13' has invalid range: start=81, end=59. Clamping end to start.
> - Action 'Action_None' range [46-148] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-236] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-163] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [46-156] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-176] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-156] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-165] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-207] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-220] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-236] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-136] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-165] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-239] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [46-154] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-165] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-186] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-34] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-68] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [70-79] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-88] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [46-158] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-218] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-230] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-237] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-59] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-28] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-54] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-22] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-34] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-45] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-181] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-29] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-48] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-61] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-57] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-162] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-227] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-74] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-89] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-128] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-110] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-128] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-158] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-188] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-98] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-143] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-217] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-106] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-122] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-101] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-113] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-128] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-152] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-149] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-154] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-181] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-223] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-182] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.