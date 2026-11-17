# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_276`
- **Input XML**: `outputs/batch/Power/Power/Power_276/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 552: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '3' (DT1) duration 103 frames exceeds threshold 90 frames [start=127, end=229].
> - Validation warning: Action 'Action_PullBlock' for track '12' (RT) duration 103 frames exceeds threshold 90 frames [start=127, end=229].
> - Action 'Action_PreSnap' range [13-203] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-215] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-223] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-329] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-227] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-261] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-203] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-207] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-274] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-289] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [127-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [228-229] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-246] for track '3' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-236] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-326] for track '4' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-146] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-197] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-225] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [127-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [171-173] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [184-185] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [187-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-176] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-228] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-258] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-307] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-315] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-324] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-168] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-310] for track '8' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-248] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-253] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-191] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-279] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-167] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-219] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-271] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [127-214] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-304] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-319] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-166] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-192] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-220] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [127-135] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [199-200] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [202-209] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-44] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-107] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-188] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-203] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-163] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-273] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-171] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-228] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-208] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-211] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-302] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-321] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-327] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-299] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-224] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-267] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-329] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-267] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-293] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-275] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-280] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-271] for track '30' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.